import os
import time
import sys
import json

import pandas as pd
import evaluate
from rouge_score import rouge_scorer, scoring

app_dir = sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.dos_data.dos_log import Dos_Test_Logs
from data.dos_data.dos_baseline import Dos_Test_Baselines
from dos_prompt import Dos_Prompt_Context
from llms.infer import llm_infer

llm_model_names = ['gemini', 'claude', 'llama', 'mistral', 'mistral_s']
result_form = pd.DataFrame(columns=['LLM Model', 'rouge1', 'rouge2', 'rougeL', 'rougeLsum'])

#compute ROUGE score
rouge = evaluate.load('rouge')
# scorer = rouge_scorer.RougeScorer(['rougeLsum'], use_stemmer=True)

for llm_name in llm_model_names:
    model_outputs = []
    baselines = []
    for log, baseline in zip(Dos_Test_Logs, Dos_Test_Baselines):
        prompt = prompt = f"{Dos_Prompt_Context} \n {log} \n Output:"
        output = llm_infer(llm_name, prompt)

        model_outputs.append(output.replace(' ', '').replace('\t', '').replace('\n', ''))
        baselines.append(baseline.replace(' ', '').replace('\t', '').replace('\n', ''))

        # prediction = '\n'.join(model_outputs)
        # target = '\n'.join(baselines)
        # score =scorer.score(target, prediction)
        score = rouge.compute(predictions=model_outputs, references=baselines)

        result_form.loc[len(result_form)] = [llm_name, f"{score['rouge1']:0.2f}", f"{score['rouge2']:0.2f}", f"{score['rougeL']:0.2f}", f"{score['rougeLsum']:0.2f}"]

print(result_form)