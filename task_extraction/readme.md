**this directory includes works by Zhao QiMing**


extract ip,url from server log with vertex ai : gemini-1.5-pro

# environtment setup

Different from openAI api or other api using `api key`, Gemini api need set `gcloud cli` to authentication.

## gcloud setting

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

Due to the network problem, sometimes google service is not stable, run `test-vertextapi-connection.py` to test the connection of vertextai api(default model is Gemini-1.5-flash). 

```bash
python test-vertexapi-connection.py
```

If there is no problem of connection, and experiment get no response, the request may limited by the [quota](https://console.cloud.google.com/apis/api/aiplatform.googleapis.com/quotas) (filte for model Gemini-1.5-pro)).


## vertext ai api setting

install vertex ai api SDK

```bash
pip install google-cloud-aiplatform==1.59.0 loguru==0.7.2
```

# preposting data

The example log file is `data/Linux.txt` , using [vertex AI studio](https://console.cloud.google.com/vertex-ai/studio) count the file are split into 1152k=1.152M tokens

For the standard result, we manually extracted the IP and URL list and corrected with regular expression. The final standard result is `data/human_evaluation.json` . This result doesn't contain the counts.

Althought Gemini-1.5-pro support context windows up to 2M tokens, it performs bad with a large number of tokens, thus we splite the file into small chunks.

To get the chunked file and corresponding standard result, run `generate_data.py`, in which you should define the log file path, save path, large standard result, chunk size. Then you can get the chunked log file and correponding manual/re  extraction/count result.

## bad log file encoding

In processing the log file, there is a problem:

```bash
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xef in position 70072: unexpected end of data
```

Identifiy the position of bad encoding:

```bash
Jun 13 11:55:04 combo rpc.statd[1636]: gethostbyname error for ^X���^X���^Z���^Z���%8x%8x%8x%8x%8x%8x%8x%8x%8x%62716x%hn%51859x%hn\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220
```

just ignore the error:

```python
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        log_content = f.read()
```

# experiment

run extract with vertex ai use the command:

```bash
python run.py -c "config/config.yaml" -m "this is a comment for experiment" -l debug
```

this will extract the IP, URL, computational consomation and evaluate, the missed case and bad will save in the json file

* `-c` config file path
* `-m` comments for experiment
* `-l` logger print level

# model parameters and prompt consturction

model parameters and prompts are stored in `prompt.py`/`prompt_test.py`

## model parameters

in dict `parameters`

* `temperature` : control the diversity of out put token, smaller for less diversity, $\frac{e^\frac{x_{i}}{T}}{\sum\limits_{j=1}^{V}e^{\frac{x^{j}}{T}}}$
* `top-p`: generature tokens from the given probability range(0.8 means chose token from total probability of 0.8 )

## prompt

prompt are constructed with 4 parts:

- `system_instruction` : description of log information extraction task
- `context`: log information extraction example(0/1/few shot)
- `input data`: chunked log file
- `reponse_schema`: json schema to control the output in json format

system instruction are used in initing the model but seems the same when we move it into context

## safty config

Response candidate content has no parts (and thus no text). The candidate is likely blocked by the safety filters.

[vertex ai safty setting](https://ai.google.dev/gemini-api/docs/safety-settings)

try code in google document

```python
from google.generativeai.types import HarmCategory, HarmBlockThreshold

model = genai.GenerativeModel(model_name='gemini-1.5-flash')
response = model.generate_content(
    ['Do these look store-bought or homemade?', img],
    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    }
)
```

get error:

```python
ValueError: <HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: 10> is not a valid HarmCategory
```

using vertex sdk solved the problem:

```python
from vertexai.generative_models import (
    GenerativeModel,
    GenerationConfig,
    # GenerationResponse,
    HarmCategory,
    HarmBlockThreshold,
)

safety_config = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
}

    response = model.generate_content(
        contents=f"{prompt}, {document}",
        generation_config=GenerationConfig(
            **parameters,
            response_mime_type="application/json",
            response_schema=response_schema,
        ),
        safety_settings=safety_config,
    )
```

## prompt analyse

### instruction

> You are a network specilist and informaticien.
>
> Your job is to extract all the text value of the following entities: {URL(domain)}, {IP}, {compuation resources} from a log file.

Role play and Task description

> The contents must only include text strings found in the document.
>
> Each contents only appear in response one time.
>
> Please list them in different catagories.

Reduce Hallucination, LLM sometimes make up data.

Reduce repeat, sometimes LLM repeat several tokens(fall into cycle).

Reduce misclassification of IP and URL.

> The resulst should be in JSON format verified the response schema.
>
> Please distince the ip and urls, ips are all numbers and dots, and urls are strings,numbers and dots.",

verify the json schema and telling the specific rules to reduce misclassification

> Please find all the ip and url from the log file.
>
> Don not make up IP and URL, they are real values from the log file.

improve recall and precision, reduce miss case and make up.

### examples

```
Here is some examples:
right example 1:
input text:
Aug  3 06:20:35 combo ftpd[28839]: connection from 211.107.232.1 () at Wed Aug  3 06:20:35 2005
Aug  3 06:20:35 combo ftpd[28839]: connection from 211.107.232.1 () at Wed Aug  3 06:20:35 2005
Aug  3 06:20:35 combo ftpd[28839]: connection from 211.107.232.1 () at Wed Aug  3 06:20:35 2005
output:
{
    "IP": [{"IP": "211.107.232.1", "count": "3"}],
    "URL": [],
    "memory": {"Memory available": "", "Memory total": "", "apg memory": "","count":""}
}
reasoning:
This is a right example because 211.107.232.1 is an IP address,appear 3 times, and there is no URL and memory mentioned in the input text.
---
right example 2:
input text:
Aug  4 07:00:29 combo sshd(pam_unix)[31674]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl 
Aug  4 07:00:29 combo sshd(pam_unix)[31675]: check pass; user unknown
Aug  4 07:00:29 combo sshd(pam_unix)[31675]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl 
Aug  4 07:00:29 combo sshd(pam_unix)[31676]: check pass; user unknown
output:
{
    "IP": [],
    "URL": [{"URL": "arx58.internetdsl.tpnet.pl","count":"2"}],
    "memory": {"Memory available": "", "Memory total": "", "apg memory": "","count":""}
}
reasoning:
This is a right example because arx58.internetdsl.tpnet.pl is an url,appear 2 times, and there is no IP and memory mentioned in the input text.
---
right example 3:
input text:
Aug  7 06:52:07 combo ftpd[16258]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005
Aug  7 06:52:07 combo ftpd[16258]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005
Aug  7 06:52:07 combo ftpd[16258]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005
Aug  7 06:52:07 combo ftpd[16258]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005
Aug  7 06:52:07 combo ftpd[16258]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005
output:
{
    "IP": [{"IP":"82.53.83.190","count":"5"}],
    "URL": [{"URL":"host190-83.pool8253.interbusiness.it","count":"5"}],
    "memory": {"Memory available": "", "Memory total": "", "apg memory": "","count":""}
}
reasoning:
This is a right example because 82.53.83.190 is an IP address,appear 5 times, and host190-83.pool8253.interbusiness.it is an URL,appear 5 times. There is no memory mentioned in the input text.
---
right example 4:
input text:
Jun  9 06:06:20 combo kernel: Memory: 125312k/129720k available (1540k kernel code, 3860k reserved, 599k data, 144k init, 0k highmem)
Jun  9 06:06:21 combo kernel: agpgart: Maximum main memory to use for agp memory: 93M
output:
{
    "IP": [],
    "URL": []
    "memory": {"Memory available": "125312k", "Memory total": "129720k", "apg memory": "93M","count":"1"}
}
reasoning:
This is a right example because Memory: 125312k/129720k and agp memory: 93M are memory mentioned in the input text. There is no IP and URL mentioned in the input text.
---
wrong example 1:
input text:
Jan  9 17:35:55 combo ftpd[6505]: connection from 60.45.101.89 (p15025-ipadfx01yosida.nagano.ocn.ne.jp) at Mon Jan  9 17:35:55 2006
Jan  9 17:35:55 combo ftpd[6505]: connection from 60.45.101.89 (p15025-ipadfx01yosida.nagano.ocn.ne.jp) at Mon Jan  9 17:35:55 2006
Jan  9 17:35:55 combo ftpd[6505]: connection from 60.45.101.89 (p15025-ipadfx01yosida.nagano.ocn.ne.jp) at Mon Jan  9 17:35:55 2006
Jan  9 17:35:55 combo ftpd[6505]: connection from 60.45.101.89 (p15025-ipadfx01yosida.nagano.ocn.ne.jp) at Mon Jan  9 17:35:55 2006
output:
{
    "IP": [{"IP":"60.45.101.89","count":"4"},{"IP":"p15025-ipadfx01yosida.nagano.ocn.ne.jp","count":"4"}],
    "URL": []
    "memory": {"Memory available": "", "Memory total": "", "apg memory": "","count":""}
}
reasoning: this is a wrong example because 60.45.101.89 is an IP address,appear 4 times, p15025-ipadfx01yosida.nagano.ocn.ne.jp is an URL,appear 4 times. There is no memory mentioned in the input text.
---
wrong example 2:
input text:
Jul  9 22:53:19 combo ftpd[24085]: connection from 206.196.21.129 (host129.206.196.21.maximumasp.com) at Sat Jul  9 22:53:19 2005  
output:
{
    "IP": [],
    "URL": [{"URL":"206.196.21.129 (host129.206.196.21.maximumasp.com)","count":"1"}],
    "memory": {"Memory available": "", "Memory total": "", "apg memory": "","count":""}
}
reasoning: this is a wrong example because 206.196.21.129 is a IP and host129.206.196.21.maximumasp.com is a URL,it should be seprate as an IP and an URL
---
wrong example 3:
input text:
Jul  9 22:53:22 combo ftpd[24073]: connection from 206.196.21.129 (host129.206.196.21.maximumasp.com) at Sat Jul  9 22:53:22 2005
Jul  9 22:53:22 combo ftpd[24073]: connection from 206.196.21.129 (host129.206.196.21.maximumasp.com) at Sat Jul  9 22:53:22 2005 
Jul 10 03:55:15 combo ftpd[24513]: connection from 217.187.83.139 () at Sun Jul 10 03:55:15 2005 
output:
{
    "IP": [{"IP":"206.196.21.129","count":"2"}],
    "URL": [{"URL":"host129.206.196.21.maximumasp.com","count":"2"}],
    "memory: {"Memory available": "", "Memory total": "", "apg memory": "","count":""}
}
reasoning: this is a wrong example because 217.187.83.139 is also an IP and appear 2 times
---
wrong example 4:
input text:
Oct  1 06:50:49 combo sshd(pam_unix)[12386]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=llekm-static-203.200.147.8.vsnl.net.in
Oct  1 06:50:49 combo sshd(pam_unix)[12386]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=llekm-static-203.200.147.8.vsnl.net.in
output:
{
    "IP": [{"IP":"203.200.147.8","count":"2"}],
    "URL": [{"URL":"llekm-static-203.200.147.8.vsnl.net.in","count":"2"}],
    "memory": {"Memory available": "", "Memory total": "", "apg memory": "","count":""}
}
reasoning: this is a wrong example because 203.200.147.8 is a part of url llekm-static-203.200.147.8.vsnl.net.in, it should not be seperated as an IP
---
wrong example 5:
input text:
Nov 12 12:21:24 combo ftpd[32401]: connection from 64.27.5.9 (merton.whererwerunning.com) at Sat Nov 12 12:21:24 2005 
output:
{
    "IP": [{"IP":"64.27.5.9","count":"1"}],
    "URL": [{"URL":"merton.whererwerunning.com","count":"1"},[{"URL":"whererwerunning.com","count":"1"}],
    "memory": {"Memory available": "", "Memory total": "", "apg memory": "","count":""}
}
reasoning: this is a wrong example because whererwerunning.com is a part of url merton.whererwerunning.com, it should not be seperated.
---
wrong example 6:
input text:
Feb  2 11:34:17 combo sshd(pam_unix)[3965]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=c-69-248-142-135.hsd1.nj.comcast.net
output:
{
    "IP": [{"IP":"c-69-248-142-135.hsd1.nj.comcast.net","count":"1"}],
    "URL": [],
    "memory": {"Memory available": "", "Memory total": "", "apg memory": "","count":""}
}
reasoning: this is a wrong example because c-69-248-142-135.hsd1.nj.comcast.net is an url
-------
wrong example 7:
input text:
Aug  6 07:23:59 combo ftpd[10159]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
Aug  6 07:23:59 combo ftpd[10156]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
Aug  6 07:23:59 combo ftpd[10170]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
Aug  6 07:23:59 combo ftpd[10162]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
Aug  6 07:23:59 combo ftpd[10168]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
output:
{
    "IP": [{"IP":"211.107.232.1","count":"3"}],
    "URL": [],
    "memory": {"Memory available": "", "Memory total": "", "apg memory": "","count":""}
}
reasoning: this is a wrong example because 211.107.232.1 appear 5 times but extract 3 times
```

some wrong examples are added for correct the bad case in experiment.
