from langchain import PromptTemplate,FewShotPromptTemplate
import json


example_prompt = PromptTemplate.from_template("example type: {example_type}\ninput text: {input_text}\noutput: {output}\nreasoning: {reasoning}")

examples = [
    {
        "example_type": "right example",
        "input_text": "Aug  3 06:20:35 combo ftpd[28839]: connection from 211.107.232.1 () at Wed Aug  3 06:20:35 2005",
        "output": json.dumps({"IP": ["211.107.232.1"], "URL": [], "memory": {"Memory available": "", "Memory total": "", "apg memory": ""}}),
        "reasoning": "This is a right example because 211.107.232.1 is an IP address, and there is no URL and memory mentioned in the input text.",
    },
    {
        "example_type": "right example",
        "input_text": "Aug  4 07:00:29 combo sshd(pam_unix)[31672]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=arx58.internetdsl.tpnet.pl",
        "output": json.dumps({"IP": [],"URL": ["arx58.internetdsl.tpnet.pl"],"memory": {"Memory available": "", "Memory total": "", "apg memory": ""}}),
        "reasoning": "This is a right example because arx58.internetdsl.tpnet.pl is an url, and there is no IP and memory mentioned in the input text.",
    },
    {
        "example_type": "right example",
        "input_text": "Aug  7 06:52:07 combo ftpd[16258]: connection from 82.53.83.190 (host190-83.pool8253.interbusiness.it) at Sun Aug  7 06:52:07 2005",
        "output": json.dumps({"IP": ["82.53.83.190"],"URL": ["host190-83.pool8253.interbusiness.it"],"memory": {"Memory available": "", "Memory total": "", "apg memory": ""}}),
        "reasoning": "This is a right example because 82.53.83.190 is an IP address, and host190-83.pool8253.interbusiness.it is an URL. There is no memory mentioned in the input text.",
    },
    {
        "example_type": "right example",
        "input_text": "Jun  9 06:06:20 combo kernel: Memory: 125312k/129720k available (1540k kernel code, 3860k reserved, 599k data, 144k init, 0k highmem)\nJun  9 06:06:21 combo kernel: agpgart: Maximum main memory to use for agp memory: 93M",
        "output": json.dumps({"IP": [],"URL": [],"memory": {"Memory available": "125312k", "Memory total": "129720k", "apg memory": "93M"}}),
        "reasoning": "This is a right example because Memory: 125312k/129720k and agp memory: 93M are memory mentioned in the input text. There is no IP and URL mentioned in the input text.",
    },
    {
        "example_type": "wrong example",
        "input_text": "Jan  9 17:35:55 combo ftpd[6505]: connection from 60.45.101.89 (p15025-ipadfx01yosida.nagano.ocn.ne.jp) at Mon Jan  9 17:35:55 2006",
        "output": json.dumps({"IP": ["60.45.101.89","p15025-ipadfx01yosida.nagano.ocn.ne.jp"],"URL": [],"memory": {"Memory available": "", "Memory total": "", "apg memory": ""}}),
        "reasoning": "this is a wrong example because 60.45.101.89 is an IP address and p15025-ipadfx01yosida.nagano.ocn.ne.jp is an URL.",
    },
    {
        "example_type": "wrong example",
        "input_text": "Jul  9 22:53:19 combo ftpd[24085]: connection from 206.196.21.129 (host129.206.196.21.maximumasp.com) at Sat Jul  9 22:53:19 2005",
        "output": json.dumps({"IP": [],"URL": ["206.196.21.129 (host129.206.196.21.maximumasp.com)"],"memory": {"Memory available": "", "Memory total": "", "apg memory": ""}}),
        "reasoning": "this is a wrong example because 206.196.21.129 is a IP and host129.206.196.21.maximumasp.com is a URL,it should be seprate as an IP and an URL.",
    },
    {
        "example_type": "wrong example",
        "input_text": "Jul  9 22:53:22 combo ftpd[24073]: connection from 206.196.21.129 (host129.206.196.21.maximumasp.com) at Sat Jul  9 22:53:22 2005\nJul 10 03:55:15 combo ftpd[24513]: connection from 217.187.83.139 () at Sun Jul 10 03:55:15 2005",
        "output": json.dumps({"IP": ["206.196.21.129"],"URL": ["host129.206.196.21.maximumasp.com"],"memory": {"Memory available": "", "Memory total": "", "apg memory": ""}}),
        "reasoning": "this is a wrong example because 217.187.83.139 is also an IP,and it isn't been extracted",
    },
    {
        "example_type": "wrong example",
        "input_text": "Oct  1 06:50:49 combo sshd(pam_unix)[12386]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=llekm-static-203.200.147.8.vsnl.net.in",
        "output": json.dumps({"IP": ["203.200.147.8"],"URL": [],"memory": {"Memory available": "", "Memory total": "", "apg memory": ""}}),
        "reasoning": "this is a wrong example because 203.200.147.8 is a part of url llekm-static-203.200.147.8.vsnl.net.in, it should not be seperated as an IP",
    },
    {
        "example_type": "wrong example",
        "input_text": "Nov 12 12:21:24 combo ftpd[32401]: connection from 64.27.5.9 (merton.whererwerunning.com) at Sat Nov 12 12:21:24 2005",
        "output": json.dumps({"IP": ["64.27.5.9"],"URL": ["merton.whererwerunning.com","whererwerunning.com"],"memory": {"Memory available": "", "Memory total": "", "apg memory": ""}}),
        "reasoning": "this is a wrong example because whererwerunning.com is a part of url merton.whererwerunning.com, it should not be seperated.",
    },
    {
        "example_type": "wrong example",
        "input_text": "Feb  2 11:34:17 combo sshd(pam_unix)[3965]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=c-69-248-142-135.hsd1.nj.comcast.net",
        "output": json.dumps({"IP": ["c-69-248-142-135.hsd1.nj.comcast.net"],"URL": [],"memory": {"Memory available": "", "Memory total": "", "apg memory": ""}}),
        "reasoning": "this is a wrong example because c-69-248-142-135.hsd1.nj.comcast.net is an url",
    },        
]

print(example_prompt.invoke(examples[0]).to_string())


prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="please extract all the IP, URL and memory from the input log file::{input_text}",
    input_variables=["input_text"],
)

print(prompt.invoke("").to_string())


def read_log_file(file_path):
    """read log file and return its content"""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        log_content = f.read()
    return log_content

text = read_log_file("D:\Desktop\Orange stage MFE\orange stage\ServerLog\log-ex\data\small data\Linux_0.txt")

# print(
#     prompt.invoke({f'"input_text": {text}'}).to_string()
# )