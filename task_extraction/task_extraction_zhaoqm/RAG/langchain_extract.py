import re
import json
import torch
from typing import Optional, List
from langchain_core.pydantic_v1 import BaseModel, Field
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain import HuggingFacePipeline
from langchain.schema.runnable import RunnablePassthrough
from langchain import PromptTemplate



model_path = "QwenQwen-1_8B-Chat"
# ---------------------------- 加载LLM ----------------------------------------- #
tokenizer = AutoTokenizer.from_pretrained(model_path,
                                          device_map="auto",
                                          trust_remote_code=True,
                                          torch_dtype=torch.float16)

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    # torch_dtype=torch.float16,
    trust_remote_code=True,
    device_map="auto",
)

pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    return_full_text=True,
)

llm = HuggingFacePipeline(pipeline=pipeline)


# ---------------------------- 定义需要提取信息的schema ---------------------------- #
class Person(BaseModel):
    """Information about a person."""
    name: Optional[str] = Field(..., description="人物的名字")
    birth_date: Optional[str] = Field(..., description="出生日期")
    birth_place: Optional[str] = Field(..., description="出生地点")
    spouse: Optional[str] = Field(..., description="配偶，妻子或丈夫")
    university: Optional[str] = Field(..., description="毕业的学校")


class People(BaseModel):
    """Identifying information about all people in a text."""
    people: List[Person]
    
    
    
# ---------------------------- 自定义解析函数 ------------------------------------ #
def extract_json(message: str) -> List[dict]:
    pattern = r"{([^{}]+)}"
    matches = re.findall(pattern, message, re.DOTALL)

    try:
        return [json.loads("{" + match.strip() + "}") for match in matches]
    except Exception:
        raise ValueError(f"Failed to parse: {message}")
    
# ---------------------------- 构造提示模板和chain ------------------------------ #
template = '''
你是信息抽取专家，从文本中只提取出schema中的相关信息。
结果按照schema的json格式输出。

schema：
{schema}

文本：
{text}
'''
prompt = PromptTemplate(template=template, input_variables=["text"], partial_variables={"schema": People.schema()})

chain = (
        {"text": RunnablePassthrough()}
        | prompt
        | llm
        | extract_json
)

# ---------------------------- 多实体文本测试 --------------------------------- #
text = "刘德华（Andy Lau），1961年9月27日出生于中国香港，华语影视男演员、流行乐歌手、电影制片人、作词人。" \
       "郭德纲，1973年1月18日出生于中国天津市，祖籍中国山西省，中国内地相声演员、导演、编剧、歌手、演员、主持人、北京德云社创始人。" \
       "沈腾，1979年10月23日出生于黑龙江省齐齐哈尔市，毕业于解放军艺术学院。"

result = chain.invoke(text)
