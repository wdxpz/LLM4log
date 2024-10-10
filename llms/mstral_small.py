from transformers import LlamaTokenizerFast, MistralForCausalLM
import torch
from huggingface_hub import login

import evaluate
from rouge_score import rouge_scorer, scoring

hf_access_token = "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"
login(token=hf_access_token)

model_name = 'mistralai/Mistral-Small-Instruct-2409'

device = "cuda"
model = MistralForCausalLM.from_pretrained('mistralai/Mistral-Small-Instruct-2409', 
                                           device_map='auto', 
                                           torch_dtype=torch.bfloat16,
                                           local_files_only=True,
                                           load_in_4bit=True,)
# model = model.to(device)

tokenizer = LlamaTokenizerFast.from_pretrained('mistralai/Mistral-Small-Instruct-2409')
tokenizer.pad_token = tokenizer.eos_token


import os
import sys
app_dir = sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import global_config
from utils.utiles import file_chunks
from example_prompt import context, context2, Dos_Baselines, response_schema, ExtractResult

Log_Trunc_Index = 1

config = global_config()
content = file_chunks(config.dataset.log_file, 32*1024)[Log_Trunc_Index]

context = """please extract all ip address or url link and their appeared times from this file, return the results in json file for downloading, the json body has 3 fields for each ip address or url link, 1st field is the content of ip address or url link in string, 2nd field the type of the content which is ip or url, 3rd field is appearance times of the ip address or url link in integer. 
Do not miss any ip address or url link! Do not give me the python scripts or any other kinds of codes, just give me the json result! 
==============================================
an example:

2024-08-04 123.127.23.1
2024-08-04 123.127.23.2
2024-08-03 123.127.23.1
2024-08-05 123.127.23.1
2024-08-04 https://www.baidu.com
2024-08-04 https://www.baidu.com/weihu

returned json body:
[
    {
        "content": "123.127.23.1",
        "type": "ip",
        "appearances": 3
    },
    {
        "content": "123.127.23.2",
        "type": "ip",
        "appearances": 1
    },
    {
        "content": "https://www.baidu.com",
        "type": "url",
        "appearances": 2
    }
]

"""
prompt = f"{context2} \n {content} \n Output:"
# prompt = "How often does the letter r occur in Mistral?"
# prompt = "how to analyze if there are Dos attack in a system log by LLM?"

messages = [
    {"role": "user", "content": prompt},
 ]

model_input = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt").to(device)
gen = model.generate(model_input, max_new_tokens=4096)
dec = tokenizer.batch_decode(gen)
print(dec)

#compute ROUGE score
# rouge = evaluate.load('rouge')
scorer = rouge_scorer.RougeScorer(['rougeLsum'], use_stemmer=True)

prediction = dec.trim(' ').trim('\n').trim('\t')
target = Dos_Baselines[Log_Trunc_Index].trim(' ').trim('\n').trim('\t')
original_rouge_score = scorer.score(target, prediction)