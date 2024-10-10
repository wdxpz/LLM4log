from langchain_community.chat_models import ChatTongyi,tongyi
from typing import Optional
from langchain_core.pydantic_v1 import BaseModel, Field
# export DASHSCOPE_API_KEY="your-api-key"

tongyi_chat = ChatTongyi(model="qwen-plus-0806", temperature=0.2, top_k=50)
llm = tongyi(model="qwen-plus-0806", temperature=0.2, top_k=50)

message = [
    (
        "system",
        """You are a network specilist and informaticien. Your job is to extract all the text value of the following entities: {URL(domain)}, {IP}, {compuation resources} from a log file.
The contents must only include text strings found in the document.Each contents only appear in response one time. Please list them in different catagories.
The resulst should be in JSON format verified the response schema.Please distince the ip and urls, ips are all numbers and dots, and urls are strings,numbers and dots.",
Please find all the ip and url from the log file. Don not make up IP and URL, they are real values from the log file.""",
    ),
    ("user", " "),
]

class extraction(BaseModel):
    '''extraction IP,URL and memory resources from log file'''
    


chain = 