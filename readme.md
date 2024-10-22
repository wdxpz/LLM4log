# Requirement and Environtment 

## docker container for dev environment
It will be convenitent to build docker container to set up the environment for development
### build docker image
```
$ cd LLM4LOG/docker
$ docker build -t llm4log:latest .
```
### start container
```
$ cd LLM4LOG
$ docker compose up -d
```
### enter dev environment
After the container is up, you can enter the dev environment either by bash or other dev tools, like visual studio code
  - bash
  ```
  $ docker exec -it llm4log:latest bash
  ```
  - visual studio code
    * choose `Open a Remote Window` at the left-bottom corner
    * choose `Attach to Running Container...` from the pop-up list and choose container `/llm4log`
    * choose project directory `/app`
    * then, you can edit and debug the project source codes

## gcloud setting
Different from openAI api or other api using `api key`, Gemini api need set `gcloud cli` to authentication.

 https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal

1. install gcloud cli
2. gcloud init and install components

```bash
gcloud init
gcloud components update
gcloud components install beta
```

3. set account and project

```bash
gcloud auth application-default login
```

if need, switch the account and project:

https://stackoverflow.com/questions/46770900/how-to-change-the-project-in-gcp-using-cli-commands

```bash
gcloud auth list # accout list
# account 1 
# account 2
gcloud config set account `ACCOUNT`
gcloud projects list
# project 1
# project 2
gcloud config set project `PROJECT ID`
```

The use of api need specific the project in the google cloud account.

## test running

Due to the network problem, sometimes google service is not stable, run [test.ipynb](llm4extract/extraction/test.ipynb)  to test the connection of vertextai api(default model is Gemini-1.5-flash).

If there is no problem of connection, and experiment get no response, the request may limited by the [quota](https://console.cloud.google.com/apis/api/aiplatform.googleapis.com/quotas) (filte for model Gemini-1.5-pro)).

# Project Structure
Here is the project structure:

```bash
————————————
|-- config
|-- data
|-- docker
|-- llm4dos
|-- llm4extract
    |-- comparision
    |-- extraction
|-- llms
|-- .gitignore
|-- docker-compose.yml
|-- readme.md
```
## config

```yaml
dataset:
  log_file: "/data/Linux.txt"
project:
  PROJECT_ID : "log-analysis-433902"
  # LOCATION : "us-central1"
  LOCATION : "asia-east1"
inference:
  save_path: "result"
  chunk_size: 128*1024
test:
  llm_result_file: "/result/result_2024-09-03_14-46-46_192k file1_counts/inference_output/output0.json"
  re_result_file: "/data/splited data/12-192x1024/new_result_human_Linux_1.json"
  human_result_file: "/data/splited data/12-192x1024/new_result_human_Linux_1.json"
comment: "192k file1 count"
gemini:
  MODEL_ID : "gemini-1.5-pro"
  LOCATION : "asia-east1"
  temperature: 0.2
  top_p : 0.8
  top_k : 32
  candidate_count : 1
  max_output_tokens : 8192
llama:
claude:
mistral:
```

dataset
    - `log_file`: input server log file path

inference
    - `save_path`: save folder path for inference result
    - `chunk_size`: chunk size for spliting the log file, 192k=192*1024
    - `count`:  count or extract result with llm
    - `prompt`: prompt file path

test
    - `llm_result_file`: inference result file path
    - `re_result_file`: regular expression result file path
    - `human_result_file`: human evaluation result file path

- `comment`: experiment comments, shows in the result file name

model(`gemini`, `llama`, `claude`, `mistral`):
    - `PROJECT_ID`: google cloud project id
    - `LOCATION`: google cloud location
    - `MODEL_NAME`: model name, `gemini-1.5-pro` for this project
    - `temperature` : control the diversity of out put token, smaller for less diversity, $\frac{e^\frac{x_{i}}{T}}{\sum\limits_{j=1}^{V}e^{\frac{x^{j}}{T}}}$
    - `top_p` (nucleus): The cumulative probability cutoff for token selection. Lower values mean sampling from a smaller, more top-weighted nucleus(0.8 means chose token from total probability of 0.8)
    - `top_k`: Sample from the k most likely next tokens at each step. Lower k focuses on higher probability tokens. Some models may not need this parameter
    - `candidate_count`: Number of candidates to generate, some models may not need this parameter
    - `max_output_tokens`: The maximum number of output tokens to generate per message, some models may not need this parameter

> google project ID setting see [google cloud vertext ai](https://console.cloud.google.com/vertex-ai)


## data

In data folder:

```bash
├── Linux.txt
├── splited data
├── result-re_Linux.json
├── count_human_evaluation.json
├── count_result-re_Linux.json
├── human_evaluation.json
└── dos_data

```

The original log file is `data/Linux.txt` , using count the file are split into 1152k=1.152M tokens

`splited data` saved the chunked log file, each folder include splited log files,regular expression result and human evaluation result.

`count_human_evaluation.json` and `count_result-re_Linux.json` are the standard result, they are manually extracted and count with regular expression.

`human_evaluation.json` and `result-re_Linux.json` are the standard result, they are manually extracted.

`dos_data` saved the data for dos attatck event analsysis.
  * `dos_prompt.py`: the designed prompt to query llm for json output of dos attack event analysis, including instrution, reasoning chain and few-shots(example) in-context-learning 
  * `dos_log.py`: 4 chunks of logs from `Linux.txt` for testing llm outputs follwing the designed prompt
  * `dos_baseline.py`: the baseline of 4 chunks of logs in `dos_log.py` to compare llm's outputs

## docker
files needed to build the container for dev environment.
  * `Dockerfile`: docker build file
  * `requirements`: required python packages

## llm4dos
files to do dos attack analysis by llm
  * `dos_analyze.py`: compare different models' behavious on dos attack analysis based on designed prompt, metrics `rouge` ([`rouge1`, `rouge2`, `rougeL`]) of each model will be evaluated 
  **just finished codes, not tested yet**

## llm4extract
files to do extraction of entity(IP/URL) and entity appearence times, please find detailed description in [extraction readme](llm4extract/extraction/readme.md)

## llms
  * `infer.py`: an encapusulated interface `llm_infer` to call a specific llm model for inference
  * `claude.py`, `gemimi.py`, `llama.py`, `mistral.py`: call different llms via google cloud vertex ai platform to do the inference
  * `mistral_small`: call `mistralai/Mistral-Small-Instruct-2409` from huggingface to do the inference, 
  **huggingface access token is required for the 1st run to cache the model to local disk, which will be located in /root/.cache/huggingface**


## `docker-compose.yml`
docker compose file to launch the llm4log container as the dev environment
* `volumes`: different directory mapping from local disk to container
  - /app: the dir for project files in the container
  - /root/.cache/huggingface: the dir to cache models from huggingface in the container
* `deploy`: settings to utilize local gpu resoureces, **comment it if no gpu resource**.

