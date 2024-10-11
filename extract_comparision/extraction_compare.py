"""
according to https://artificialanalysis.ai/
1. GPT-4o(Aug '24): 77.2 (not integrated in GCP, 128K context)
2. Claude 3.5 Sonnet: 76.9 (OK, 2M context)
3. GPT-4o(May '24): 76.7 (not integrated in GCP, 128K context)
4. Mistral Large 2: 73 (not integrated in GCP, 128K context)
5. Llama 3.1 405B: 71.9 (OK, 128K context)
6. Gemini 1.5 Pro: 71.5 (OK, 2M context)
7. Claude 3 Opus: 70.3 (OK, 2M context)
8. Mistral Large: 56.1 (OK, 34.6k context)

free model from huggingface
1. Mistral Small (Sep '24): 60.4
1. Llama 31. 8B: 53.1 

extraction result on 1st 128k chunk
                    LLM Model IP precesion IP recall URL precision URL recall
0              gemini_pro_1_5         0.96      0.94          0.94       0.85
1  claude_3_5_sonnet_20240620         0.64      0.19          0.50       0.35
2      claude_3_opus_20240229         0.87      0.96          0.67       0.70
3              llama_3_1_405B         0.74      0.36          0.75       0.45
4               mistral_large         1.00      0.53          1.00       0.10
"""
import os
import time
import sys
import json
app_dir = sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd

import vertexai
from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    HarmBlockThreshold,
    HarmCategory,
    Part,
)

import httpx
import google.auth
from google.auth.transport.requests import Request

from anthropic import AnthropicVertex



from llms.gemini import complete_gemini
from llms.claude import complete_claude
from llms.mistral import complete_mistral
from llms.llama import complete_llama
from config.config import global_config
from task_extraction.utils.utiles import file_chunks
from example_prompt import extraction_prompt_context as context
from example_prompt import extraction_response_schema as response_schema
from example_prompt import ExtractResult



config = global_config()
content = file_chunks(config.dataset.log_file, eval(config.inference.chunk_size))[0]
prompt = f"{context} \n {content} \n"

PROJECT_ID = config.project.PROJECT_ID

ENABLE_GMINI = False
ENABLE_CLAUDE = False
ENABLE_LLAMA = False
ENABLE_MISTRAL = False
COMPARE_RESULTS = True


if ENABLE_GMINI:
    print("\n"+"*"*25+f"{config.gemini.MODEL_ID} on 1st chunk:"+"*"*25)
    start_time = time.time()
    # Prompt the model to generate content
    try:
        result = complete_gemini(prompt, response_schema)
    except Exception as e:
        print(f"Error! {str(e)}")
    duration = time.time()-start_time
    
    print(f"time cost: {duration}")
    print(f"\n{result}")

if ENABLE_CLAUDE:
    start_time = time.time()
    print("\n"+"*"*25+f"{config.claude.MODEL_ID} on 1st chunk:"+"*"*25)
    try:
        result = complete_claude(prompt)
    except Exception as e:
        print(f"Error! {str(e)}")
    duration = time.time()-start_time 
    print(f"time cost: {duration}")
    print(result)

if ENABLE_LLAMA:
    start_time = time.time()
    print("\n"+"*"*25+f"{config.llama.MODEL_ID}on 1st chunk:"+"*"*25)
    try:
        result = complete_llama(prompt)
    except Exception as e:
        print(f"Error! {str(e)}")
    duration = time.time()-start_time 
    print(f"time cost: {duration}")
    print(result)

if ENABLE_MISTRAL:
    print("\n"+"*"*25+f"{config.mistral.MODEL_ID} {config.mistral.MODEL_VERSION} on 1st chunk:"+"*"*25)
    start_time = time.time()
    try:
        result = complete_mistral(prompt[:int(len(prompt)*32768.0/78581.0)])
    except Exception as e:
        print(f"Error! {str(e)}")
    duration = time.time()-start_time
    print(f"time cost: {duration}")
    print(result)


def extraction_precison_and_recall(results, base_line_file):
    with open(base_line_file, "r") as f:
        base_line_s = f.read()
    
    base_line = json.loads(base_line_s)
    ip_list = set(base_line['IP'])
    ip_num = len(ip_list)
    url_list = set(base_line['URL'])
    url_num=len(url_list)
    result_form = pd.DataFrame(columns=['LLM Model', 'IP precesion', 'IP recall', 'URL precision', 'URL recall'])
    for llm_model, result in results.items():
        extract_ip_list = set(result['IP'])
        extract_ip_num = len(extract_ip_list)*1.0
        correct_ip_list = extract_ip_list & ip_list
        correct_ip_num = len(correct_ip_list)*1.0

        extract_url_list = set(result['URL'])
        extract_url_num = len(extract_url_list)*1.0
        corret_url__list = extract_url_list & url_list
        correct_url_num = len(corret_url__list)*1.0
        result_form.loc[len(result_form)] = [llm_model, f"{correct_ip_num/extract_ip_num:0.2f}", f"{correct_ip_num/ip_num:0.2f}", f"{correct_url_num/extract_url_num:0.2f}", f"{correct_url_num/url_num:0.2f}"]

    print(result_form)

if COMPARE_RESULTS:
    from extraction_result import results
    extraction_precison_and_recall(results, "/app/data/splited_data/18-128x1024/result_huaman_Linux_0.json")