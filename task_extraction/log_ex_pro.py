import datetime
import os
import vertexai
from vertexai.generative_models import (
    GenerativeModel,
    GenerationConfig,
    # GenerationResponse,
    HarmCategory,
    HarmBlockThreshold,
)

# from google.generativeai.types import HarmCategory, HarmBlockThreshold
from loguru import logger
from utils.utiles import (
    file_chunks,
    merge_json_files,
)






def get_response(
    model,
    prompt,
    document,
    file_name,
    parameters,
    response_schema=None,
    safety_config=None,
):
    """get response from model
    model: GenerativeModel object
    prompt: str, prompt for model
    document: str, document to generate response for
    file_name: str, name of output file
    """
    response = model.generate_content(
        contents=f"{prompt}, {document}",
        generation_config=GenerationConfig(
            **parameters,
            response_mime_type="application/json",
            response_schema=response_schema,
        ),
        safety_settings=safety_config,
    )
    write_response(response.text, file_name)


def write_response(response, filename):
    """write response to file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response)
    logger.info(f"Generated response in {filename}")


def vertexai_init(PROJECT_ID, LOCATION, MODEL_NAME, system_instruction):
    """initialize vertex ai model
    PROJECT_ID:vertext ai module init
    LOCATION:vertext ai module init
    MODEL_NAME:generative model init
    system_instruction:generative model init
    """
    vertexai.init(project=PROJECT_ID, location=LOCATION)

    logger.info("initial the model")
    logger.info(f"Project ID: {PROJECT_ID}")
    logger.info(f"Location: {LOCATION}")
    logger.info(f"Model Name: {MODEL_NAME}")
    # model initialization
    model = GenerativeModel(
        MODEL_NAME,
        system_instruction=system_instruction,
    )
    logger.info(f"Model system_instrcution {system_instruction}")
    return model


if __name__ == "__main__":
    system_instruction = [
    "you are a network specilist and informaticien.",
    "your job is to extract all the text value of the following entities: {URL(domain)}, {IP}, {compuation resources} from a log file.",
    "the contents must only include text strings found in the document.",
    "each contents only appear in response one time. Please list them in different catagories.",
    "the resulst should be in JSON format verified the response schema.",
    "please distince the ip and urls, ips are all numbers and dots, and urls are strings,numbers and dots.",
    "please find all the ip and url from the log file",
    "don not make up IP and URL, they are real values from the log file."
    ]

    parameters = {
        "temperature": 0,
        "top_p": 0.8,
        # "top_k": 40
    }

    # response_schema = {
    #     "type": "ARRAY",
    #     "items": {
    #         "type": "OBJECT",
    #         "properties": {
    #             "Item type": {
    #                 "type": "STRING",
    #                 "enum": ["IP", "URL", "Memory"],
    #             },
    #             "Item content": {"type": "STRING"},
    #         },
    #         "required": ["Item type", "Item content"],
    #     },
    # }

    response_schema = {
        "type": "OBJECT",
        "properties": {
            "URL": {
                "type": "ARRAY",
                "items": {"type": "STRING"},
            },
            "IP": {
                "type": "ARRAY",
                "items": {"type": "STRING"},
            },
            "memory": {
                "type": "ARRAY",
                "items": {"type": "STRING"},
            },
        },
        "required": ["URL", "IP", "memory"],
    }

    prompt = """right example 1:
input text:
Aug  3 06:20:35 combo ftpd[28839]: connection from 211.107.232.1 () at Wed Aug  3 06:20:35 2005 
output：
{
    "IP": ["211.107.232.1"],
    "URL": []
    "memory": []
}
reasoning:
This is a right example because 211.107.232.1 is an IP address, and there is no URL and memory mentioned in the input text.
---
right example 2:
input text:
Aug  4 07:00:29 combo sshd(pam_unix)[31672]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl 
output：
{
    "IP": [],
    "URL": ["arx58.internetdsl.tpnet.pl"]
    "memory": []
}
reasoning:
This is a right example because arx58.internetdsl.tpnet.pl is an url, and there is no IP and memory mentioned in the input text.
---
right example 3:
input text:
Aug  7 06:52:07 combo ftpd[16258]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
output：
{
    "IP": ["82.53.83.190"],
    "URL": ["host190-83.pool8253.interbusiness.it"]
    "memory": []
}
reasoning:
This is a right example because 82.53.83.190 is an IP address, and host190-83.pool8253.interbusiness.it is an URL. There is no memory mentioned in the input text.
---
wrong example 1:
input text:
Jan  9 17:35:55 combo ftpd[6505]: connection from 60.45.101.89 (p15025-ipadfx01yosida.nagano.ocn.ne.jp) at Mon Jan  9 17:35:55 2006
output：
{
    "IP": ["60.45.101.89","p15025-ipadfx01yosida.nagano.ocn.ne.jp"],
    "URL": []
    "memory": []
}
reasoning: this is a wrong example because 60.45.101.89 is an IP address and p15025-ipadfx01yosida.nagano.ocn.ne.jp is an URL
---
wrong example 2:
input text:
Jul  9 22:53:19 combo ftpd[24085]: connection from 206.196.21.129 (host129.206.196.21.maximumasp.com) at Sat Jul  9 22:53:19 2005  
output：
{
    "IP": [],
    "URL": ["206.196.21.129 (host129.206.196.21.maximumasp.com)"],
    "memory": []
}
reasoning: this is a wrong example because 206.196.21.129 is a IP and host129.206.196.21.maximumasp.com is a URL.
---
wrong example 3:
input text:
Jul  9 22:53:22 combo ftpd[24073]: connection from 206.196.21.129 (host129.206.196.21.maximumasp.com) at Sat Jul  9 22:53:22 2005 
Jul 10 03:55:15 combo ftpd[24513]: connection from 217.187.83.139 () at Sun Jul 10 03:55:15 2005 
output：
{
    "IP": ["206.196.21.129"],
    "URL": ["host129.206.196.21.maximumasp.com"],
    "memory: []
}
reasoning: this is a wrong example because 217.187.83.139 is also an IP
---
wrong example 4:
input text:
Oct  1 06:50:49 combo sshd(pam_unix)[12386]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=llekm-static-203.200.147.8.vsnl.net.in
output：
{
    "IP": ["203.200.147.8"],
    "URL": [],
    "memory": []
}
reasoning: this is a wrong example because 203.200.147.8 is a part of url llekm-static-203.200.147.8.vsnl.net.in, it should not be seperated as an IP
---
wrong example 5:
input text:
Nov 12 12:21:24 combo ftpd[32401]: connection from 64.27.5.9 (merton.whererwerunning.com) at Sat Nov 12 12:21:24 2005 
output：
{
    "IP": ["64.27.5.9"],
    "URL": ["merton.whererwerunning.com","whererwerunning.com"],
    "memory": []
}
reasoning: this is a wrong example because whererwerunning.com is a part of url merton.whererwerunning.com, it should not be seperated.
-------
please extract all the IP, URL and memory from the input log file:"""
    # prompt = """Given a document, your task is to extract the text value of the following entities: {URL(domain)}, {IP}, {compuation resources(memory, cpu)}
    # The IPs are consist of pure numbers and dots, and the URLs are consist of letters, numbers, and special characters.
    # - The contents must only include text strings found in the document.
    # - The contents only apear in response one time. Please list them in different catagories.
    # - The resulst should be in JSON format.
    # Attention that IP are all numbers and dots, and URL are strings,numbers and dots!!!
    # if there are any letters in the extract text, please treat the text as URL
    # if there are no letters in the extract text, please treat the text as IP
    # "206-248-137-78.dsl.teksavvy.com" is an URL, "202.101.42.106" is an IP,
    # don't class a IP into a category of URL and don't class a URL into a category of IP
    # Attention that the result must be the string include in the document!!!
    
    # ----------------------------------------------------------------------------------------------
    # "IP":["206-248-137-78.dsl.teksavvy.com"] is wrong!Don't consider "206-248-137-78.dsl.teksavvy.com" as IP.
    # "URL":["206-248-137-78.dsl.teksavvy.com"] is correct.
    # "URL":["202.101.42.106"] is wrong!Don't consider "202.101.42.106" as URL.
    # "IP":["202.101.42.106"] is correct.
    # -----------------------------------------------------------------------------------------------          
    # example:
    # Aug  3 04:03:17 combo su(pam_unix)[27339]: session closed for user cyrus
    # Aug  3 04:03:18 combo logrotate: ALERT exited abnormally with [1]
    # Aug  3 04:09:50 combo su(pam_unix)[28565]: session opened for user news by (uid=0)
    # Aug  3 04:09:51 combo su(pam_unix)[28565]: session closed for user news
    # Aug  3 06:20:34 combo ftpd[28835]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28827]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28823]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28834]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28832]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28824]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28825]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28821]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28831]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28826]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28828]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28829]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28822]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28833]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:34 combo ftpd[28830]: connection from 211.107.232.1 () at Wed Aug  3 06:20:34 2005 
    # Aug  3 06:20:35 combo ftpd[28836]: connection from 211.107.232.1 () at Wed Aug  3 06:20:35 2005 
    # Aug  3 06:20:35 combo ftpd[28839]: connection from 211.107.232.1 () at Wed Aug  3 06:20:35 2005 
    # Aug  3 06:20:35 combo ftpd[28838]: connection from 211.107.232.1 () at Wed Aug  3 06:20:35 2005 
    # Aug  3 06:20:35 combo ftpd[28837]: connection from 211.107.232.1 () at Wed Aug  3 06:20:35 2005 
    # Aug  3 06:20:36 combo ftpd[28842]: connection from 211.107.232.1 () at Wed Aug  3 06:20:36 2005 
    # Aug  3 06:20:36 combo ftpd[28841]: connection from 211.107.232.1 () at Wed Aug  3 06:20:36 2005 
    # Aug  3 06:20:36 combo ftpd[28840]: connection from 211.107.232.1 () at Wed Aug  3 06:20:36 2005 
    # Aug  4 04:03:35 combo su(pam_unix)[31009]: session opened for user cyrus by (uid=0)
    # Aug  4 04:03:36 combo su(pam_unix)[31009]: session closed for user cyrus
    # Aug  4 04:03:37 combo logrotate: ALERT exited abnormally with [1]
    # Aug  4 04:09:30 combo su(pam_unix)[31380]: session opened for user news by (uid=0)
    # Aug  4 04:09:31 combo su(pam_unix)[31380]: session closed for user news
    # Aug  4 07:00:29 combo sshd(pam_unix)[31672]: check pass; user unknown
    # Aug  4 07:00:29 combo sshd(pam_unix)[31672]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl 
    # Aug  4 07:00:29 combo sshd(pam_unix)[31674]: check pass; user unknown
    # Aug  4 07:00:29 combo sshd(pam_unix)[31674]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl 
    # Aug  4 07:00:29 combo sshd(pam_unix)[31675]: check pass; user unknown
    # Aug  4 07:00:29 combo sshd(pam_unix)[31675]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl 
    # Aug  4 07:00:29 combo sshd(pam_unix)[31676]: check pass; user unknown
    # Aug  4 07:00:29 combo sshd(pam_unix)[31676]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl 
    # Aug  4 07:00:29 combo sshd(pam_unix)[31677]: check pass; user unknown
    # Aug  4 07:00:29 combo sshd(pam_unix)[31677]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl 
    # Aug  4 07:00:29 combo sshd(pam_unix)[31678]: check pass; user unknown
    # Aug  4 07:00:29 combo sshd(pam_unix)[31673]: check pass; user unknown
    # Aug  4 07:00:29 combo sshd(pam_unix)[31682]: check pass; user unknown
    # Aug  4 07:00:29 combo sshd(pam_unix)[31683]: check pass; user unknown
    # Aug  4 07:00:29 combo sshd(pam_unix)[31673]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl 
    # Aug  4 07:00:29 combo sshd(pam_unix)[31678]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl 
    # Aug  4 07:00:29 combo sshd(pam_unix)[31682]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl 
    # Aug  4 07:00:29 combo sshd(pam_unix)[31683]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl 
    # Aug  4 07:00:29 combo sshd(pam_unix)[31690]: check pass; user unknown
    # Aug  4 07:00:29 combo sshd(pam_unix)[31690]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl 
    # Aug  4 11:01:11 combo sshd(pam_unix)[32057]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=202.96.242.5  user=root
    # Aug  5 04:05:42 combo su(pam_unix)[1430]: session opened for user cyrus by (uid=0)
    # Aug  5 04:05:42 combo su(pam_unix)[1430]: session closed for user cyrus
    # Aug  5 04:05:43 combo logrotate: ALERT exited abnormally with [1]
    # Aug  5 04:12:12 combo su(pam_unix)[2703]: session opened for user news by (uid=0)
    # Aug  5 04:12:13 combo su(pam_unix)[2703]: session closed for user news
    # Aug  5 05:01:30 combo login(pam_unix)[25160]: bad username [   ]
    # Aug  5 05:01:30 combo login[25160]: FAILED LOGIN 1 FROM (null) FOR    , Authentication failure
    # Aug  5 05:01:30 combo login(pam_unix)[25160]: bad username []
    # Aug  5 05:01:30 combo login[25160]: FAILED LOGIN 2 FROM (null) FOR , Authentication failure
    # Aug  5 05:02:30 combo udev[2877]: removing device node '/udev/vcs2'
    # Aug  5 05:02:30 combo udev[2878]: removing device node '/udev/vcsa2'
    # Aug  5 05:02:30 combo udev[2887]: creating device node '/udev/vcs2'
    # Aug  5 05:02:30 combo udev[2888]: creating device node '/udev/vcsa2'
    # Aug  5 05:02:30 combo udev[2895]: removing device node '/udev/vcs2'
    # Aug  5 05:02:30 combo udev[2903]: removing device node '/udev/vcsa2'
    # Aug  5 05:02:31 combo udev[2900]: creating device node '/udev/vcs2'
    # Aug  5 05:02:31 combo udev[2908]: creating device node '/udev/vcsa2'
    # Aug  5 12:03:56 combo sshd(pam_unix)[3501]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=202.96.242.5  user=root
    # Aug  5 12:04:13 combo sshd(pam_unix)[3504]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=202.96.242.5  user=root
    # Aug  6 04:03:29 combo su(pam_unix)[5193]: session opened for user cyrus by (uid=0)
    # Aug  6 04:03:30 combo su(pam_unix)[5193]: session closed for user cyrus
    # Aug  6 04:03:30 combo logrotate: ALERT exited abnormally with [1]
    # Aug  6 04:11:21 combo su(pam_unix)[9843]: session opened for user news by (uid=0)
    # Aug  6 04:11:22 combo su(pam_unix)[9843]: session closed for user news
    # Aug  6 07:23:59 combo ftpd[10159]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10156]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10170]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10162]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10168]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10166]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10155]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10167]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10160]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10165]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10164]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10161]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10169]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10153]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10163]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10157]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10158]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10154]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  6 07:23:59 combo ftpd[10152]: connection from 211.107.232.1 () at Sat Aug  6 07:23:59 2005 
    # Aug  7 04:03:36 combo su(pam_unix)[12320]: session opened for user cyrus by (uid=0)
    # Aug  7 04:03:37 combo su(pam_unix)[12320]: session closed for user cyrus
    # Aug  7 04:03:39 combo cups: cupsd shutdown succeeded
    # Aug  7 04:03:45 combo cups: cupsd startup succeeded
    # Aug  7 04:03:57 combo syslogd 1.4.1: restart.
    # Aug  7 04:03:57 combo logrotate: ALERT exited abnormally with [1]
    # Aug  7 04:09:31 combo su(pam_unix)[12914]: session opened for user news by (uid=0)
    # Aug  7 04:09:32 combo su(pam_unix)[12914]: session closed for user news
    # Aug  7 06:52:07 combo ftpd[16258]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16249]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16254]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16259]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16257]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16256]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16260]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16255]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16248]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16244]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16243]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16247]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16242]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16252]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16241]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16250]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
    # Aug  7 06:52:07 combo ftpd[16253]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005 
            
    # output:
    # {"URL":["arx58.internetdsl.tpnet.pl", "host190-83.pool8253.interbusiness.it"],
    # "IP":["211.107.232.1", "202.96.242.5", "82.53.83.190"],
    # "memory":["125312k/129720k available",],
    # }
    # -------
    # here is the file:

    # """

    safety_config = {
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    }
    # save path
    current_datetime = datetime.datetime.now()
    date_time_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = f"result/result_{date_time_str}"
    os.makedirs(folder_name, exist_ok=True)

    # TODO(developer): Update and un-comment below line
    PROJECT_ID = "log-extraction"
    LOCATION = "asia-east1"
    MODEL_NAME = "gemini-1.5-pro"

    logger.add(f"{folder_name}/log.txt")

    model = vertexai_init(PROJECT_ID, LOCATION, MODEL_NAME, system_instruction)

    logger.info(f"prompt: {prompt}")

    # chunks file into a list
    document = file_chunks("data/Linux.txt", 728*728) # 728 * 728

    # save extracted json to file
    for i, j in enumerate(document):
        save_path = os.path.join(folder_name, f"output{i}.json")
        get_response(
            model, prompt, j, save_path, parameters, response_schema, safety_config
        )

    merge_json_files(folder_name, f"{folder_name}/merged_output.json")
