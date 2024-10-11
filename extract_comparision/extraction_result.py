"""
this file includes extraction results from data/splited_data/18-128*1024/Linux_0.txt by different LLMs
"""

import json
# Compare Result:


# *************************Gmini pro 1.5 on 1st chunk:*************************
# total_tokens: 72371
# total_billable_characters: 124419

# time cost: 53.80514407157898

gemini_pro_1_5_result = {"IP": ["127.0.0.1", "63.126.79.67", "63.126.79.69", "63.126.79.70", "63.126.79.71", "63.126.79.72", "63.126.79.73", "63.126.79.75", "63.126.79.80", "63.126.79.81", "63.126.79.82", "63.126.79.83", "63.126.79.84", "63.126.79.85", "63.126.79.87", "63.126.79.89", "63.126.79.90", "63.126.79.95", "63.126.79.100", "63.126.79.105", "63.126.79.110", "63.126.79.115", "63.126.79.120", "63.126.79.125", "67.170.148.126", "211.233.12.249", "218.188.2.4", "202.101.42.106", "220-135-151-1.hinet-ip.hinet.net", "209.184.7.130", "222.33.90.199", "218.188.2.4", "211.46.241.200", "218.38.14.205", "61.218.67.60", "212.5.120.141", "61.153.202.254", "65.35.73.251", "24.54.76.216", "82.252.162.81", "70.242.75.179", "209.152.168.249", "200.60.37.201", "218.22.3.51", "218.69.108.57", "210.118.170.95", "210.245.165.136"], "URL": ["www.scyld.com/network/vortex.html", "http://smartmontools.sourceforge.net/", "itsc.iasi.astral.ro", "unknown.sagonet.net", "mail.net-star.com.tw", "host-141.STSK.macomnet.net", "under-eepc58.kaist.ac.kr", "220-135-151-1.hinet-ip.hinet.net", "24-54-76-216.bflony.adelphia.net", "211.46.224.253", "lns-vlq-45-tou-82-252-162-81.adsl.proxad.net", "adsl-70-242-75-179.dsl.ksc2mo.swbell.net", "251-73.35-65.tampabay.res.rr.com", "061092085098.ctinets.com", "d211-116-254-214.rev.krline.net", "massive.merukuru.org", "n219076184117.netvigator.com", "ip-216-69-169-168.ip.secureserver.net"], "memory": [{"Memory available": "125312k", "Memory total": "129720k", "apg memory": "93M"}, {"Memory available": "125312k", "Memory total": "129720k", "apg memory": "93M"}]} 

# *************************claude-3-5-sonnet@20240620 on 1st chunk:*************************
# time cost: 24.335509538650513
# {
#   "id": "msg_vrtx_0169Wm3Mzt1qbtprHEvvZ9hB",
#   "content": [
#     {
#       "text": "Here is the extracted information in JSON format:\n\n{\n    \"IP\": [\n        \"211.107.232.1\",\n        \"82.53.83.190\",\n        \"206.196.21.129\",\n        \"217.187.83.139\",\n        \"64.27.5.9\",\n        \"209.184.7.130\",\n        \"222.33.90.199\",\n        \"61.218.67.60\",\n        \"212.5.120.141\",\n        \"222.33.90.199\",\n        \"65.35.73.251\",\n        \"210.245.165.136\",\n        \"218.69.108.57\",\n        \"24.54.76.216\",\n        \"210.118.170.95\"\n    ],\n    \"URL\": [\n        \"arx58.internetdsl.tpnet.pl\",\n        \"host190-83.pool8253.interbusiness.it\",\n        \"host129.206.196.21.maximumasp.com\",\n        \"merton.whererwerunning.com\",\n        \"c-69-248-142-135.hsd1.nj.comcast.net\",\n        \"p15025-ipadfx01yosida.nagano.ocn.ne.jp\",\n        \"llekm-static-203.200.147.8.vsnl.net.in\",\n        \"mail.net-star.com.tw\",\n        \"host-141.STSK.macomnet.net\",\n        \"24-54-76-216.bflony.adelphia.net\",\n        \"lns-vlq-45-tou-82-252-162-81.adsl.proxad.net\",\n        \"251-73.35-65.tampabay.res.rr.com\",\n        \"n219076184117.netvigator.com\",\n        \"massive.merukuru.org\"\n    ],\n    \"memory\": [\n        {\n            \"Memory available\": \"125312k\",\n            \"Memory total\": \"129720k\", \n            \"apg memory\": \"93M\"\n        }\n    ]\n}",
#       "type": "text"
#     }
#   ],
#   "model": "claude-3-5-sonnet-20240620",
#   "role": "assistant",
#   "stop_reason": "end_turn",
#   "stop_sequence": null,
#   "type": "message",
#   "usage": {
#     "input_tokens": 63763,
#     "output_tokens": 520
#   }
# }
result_str = "{\n    \"IP\": [\n        \"211.107.232.1\",\n        \"82.53.83.190\",\n        \"206.196.21.129\",\n        \"217.187.83.139\",\n        \"64.27.5.9\",\n        \"209.184.7.130\",\n        \"222.33.90.199\",\n        \"61.218.67.60\",\n        \"212.5.120.141\",\n        \"222.33.90.199\",\n        \"65.35.73.251\",\n        \"210.245.165.136\",\n        \"218.69.108.57\",\n        \"24.54.76.216\",\n        \"210.118.170.95\"\n    ],\n    \"URL\": [\n        \"arx58.internetdsl.tpnet.pl\",\n        \"host190-83.pool8253.interbusiness.it\",\n        \"host129.206.196.21.maximumasp.com\",\n        \"merton.whererwerunning.com\",\n        \"c-69-248-142-135.hsd1.nj.comcast.net\",\n        \"p15025-ipadfx01yosida.nagano.ocn.ne.jp\",\n        \"llekm-static-203.200.147.8.vsnl.net.in\",\n        \"mail.net-star.com.tw\",\n        \"host-141.STSK.macomnet.net\",\n        \"24-54-76-216.bflony.adelphia.net\",\n        \"lns-vlq-45-tou-82-252-162-81.adsl.proxad.net\",\n        \"251-73.35-65.tampabay.res.rr.com\",\n        \"n219076184117.netvigator.com\",\n        \"massive.merukuru.org\"\n    ],\n    \"memory\": [\n        {\n            \"Memory available\": \"125312k\",\n            \"Memory total\": \"129720k\", \n            \"apg memory\": \"93M\"\n        }\n    ]\n}"
claude_3_5_sonnet_result = json.loads(result_str)

# *************************claude-3-opus@20240229 on 1st chunk:*************************
# time cost: 69.64145612716675
# {
#   "id": "msg_vrtx_01Thsg5m2gNDxs5Su44wx1Ay",
#   "content": [
#     {
#       "text": "Here is the output in JSON format with the requested keys:\n\n{\n    \"IP\": [\n        \"63.126.79.67\",\n        \"63.126.79.69\", \n        \"63.126.79.70\",\n        \"63.126.79.71\",\n        \"63.126.79.72\",\n        \"63.126.79.73\",\n        \"63.126.79.75\",\n        \"63.126.79.80\",\n        \"63.126.79.81\",\n        \"63.126.79.82\",\n        \"63.126.79.83\",\n        \"63.126.79.84\",\n        \"63.126.79.85\",\n        \"63.126.79.87\",\n        \"63.126.79.89\",\n        \"63.126.79.90\",\n        \"63.126.79.95\",\n        \"63.126.79.100\",\n        \"63.126.79.105\",\n        \"63.126.79.110\",\n        \"63.126.79.115\",\n        \"63.126.79.120\",\n        \"63.126.79.125\",\n        \"127.0.0.1\",\n        \"211.107.232.1\",\n        \"82.53.83.190\",\n        \"206.196.21.129\",\n        \"217.187.83.139\",\n        \"209.184.7.130\",\n        \"212.5.120.141\",\n        \"65.35.73.251\",\n        \"222.33.90.199\",\n        \"61.218.67.60\",\n        \"218.188.2.4\",\n        \"61.153.202.254\",\n        \"211.233.12.249\",\n        \"218.38.14.205\",\n        \"24.54.76.216\",\n        \"82.252.162.81\",\n        \"65.166.159.14\",\n        \"67.170.148.126\",\n        \"210.245.165.136\",\n        \"61.092.085.098\",\n        \"202.101.42.106\",\n        \"220.135.151.1\",\n        \"217.60.212.66\",\n        \"219.076.184.117\",\n        \"209.152.168.249\",\n        \"200.60.37.201\",\n        \"218.22.3.51\",\n        \"218.69.108.57\",\n        \"210.118.170.95\"\n    ],\n    \"URL\": [\n        \"arx58.internetdsl.tpnet.pl\",\n        \"host190-83.pool8253.interbusiness.it\",\n        \"p15025-ipadfx01yosida.nagano.ocn.ne.jp\",\n        \"host129.206.196.21.maximumasp.com\",\n        \"itsc.iasi.astral.ro\",\n        \"host-141.STSK.macomnet.net\",\n        \"251-73.35-65.tampabay.res.rr.com\",\n        \"mail.net-star.com.tw\",\n        \"llekm-static-203.200.147.8.vsnl.net.in\",\n        \"c-69-248-142-135.hsd1.nj.comcast.net\",\n        \"merton.whererwerunning.com\",\n        \"unknown.sagonet.net\",\n        \"under-eepc58.kaist.ac.kr\",\n        \"24-54-76-216.bflony.adelphia.net\",\n        \"lns-vlq-45-tou-82-252-162-81.adsl.proxad.net\",\n        \"ip-216-69-169-168.ip.secureserver.net\",\n        \"adsl-70-242-75-179.dsl.ksc2mo.swbell.net\",\n        \"061092085098.ctinets.com\",\n        \"d211-116-254-214.rev.krline.net\",\n        \"n219076184117.netvigator.com\",\n        \"massive.merukuru.org\"\n    ],\n    \"memory\": [\n        {\n            \"Memory available\": \"125312k\",\n            \"Memory total\": \"129720k\",\n            \"apg memory\": \"93M\"\n        }\n    ]\n}\n\nReasoning:\nI extracted all the IP addresses, URLs, and memory information from the provided log file, following these rules:\n- IP addresses are in the format of 4 numbers separated by dots\n- URLs are strings of characters and numbers separated by dots or dashes\n- Memory information includes \"Memory available\", \"Memory total\", and \"agp memory\" values\n- Each IP, URL, and memory dict is only included once in the output\n- The output is in valid JSON format with the requested keys",
#       "type": "text"
#     }
#   ],
#   "model": "claude-3-opus-20240229",
#   "role": "assistant",
#   "stop_reason": "end_turn",
#   "stop_sequence": null,
#   "type": "message",
#   "usage": {
#     "input_tokens": 63762,
#     "output_tokens": 1160
#   }
# }
result_str = "{\n    \"IP\": [\n        \"63.126.79.67\",\n        \"63.126.79.69\", \n        \"63.126.79.70\",\n        \"63.126.79.71\",\n        \"63.126.79.72\",\n        \"63.126.79.73\",\n        \"63.126.79.75\",\n        \"63.126.79.80\",\n        \"63.126.79.81\",\n        \"63.126.79.82\",\n        \"63.126.79.83\",\n        \"63.126.79.84\",\n        \"63.126.79.85\",\n        \"63.126.79.87\",\n        \"63.126.79.89\",\n        \"63.126.79.90\",\n        \"63.126.79.95\",\n        \"63.126.79.100\",\n        \"63.126.79.105\",\n        \"63.126.79.110\",\n        \"63.126.79.115\",\n        \"63.126.79.120\",\n        \"63.126.79.125\",\n        \"127.0.0.1\",\n        \"211.107.232.1\",\n        \"82.53.83.190\",\n        \"206.196.21.129\",\n        \"217.187.83.139\",\n        \"209.184.7.130\",\n        \"212.5.120.141\",\n        \"65.35.73.251\",\n        \"222.33.90.199\",\n        \"61.218.67.60\",\n        \"218.188.2.4\",\n        \"61.153.202.254\",\n        \"211.233.12.249\",\n        \"218.38.14.205\",\n        \"24.54.76.216\",\n        \"82.252.162.81\",\n        \"65.166.159.14\",\n        \"67.170.148.126\",\n        \"210.245.165.136\",\n        \"61.092.085.098\",\n        \"202.101.42.106\",\n        \"220.135.151.1\",\n        \"217.60.212.66\",\n        \"219.076.184.117\",\n        \"209.152.168.249\",\n        \"200.60.37.201\",\n        \"218.22.3.51\",\n        \"218.69.108.57\",\n        \"210.118.170.95\"\n    ],\n    \"URL\": [\n        \"arx58.internetdsl.tpnet.pl\",\n        \"host190-83.pool8253.interbusiness.it\",\n        \"p15025-ipadfx01yosida.nagano.ocn.ne.jp\",\n        \"host129.206.196.21.maximumasp.com\",\n        \"itsc.iasi.astral.ro\",\n        \"host-141.STSK.macomnet.net\",\n        \"251-73.35-65.tampabay.res.rr.com\",\n        \"mail.net-star.com.tw\",\n        \"llekm-static-203.200.147.8.vsnl.net.in\",\n        \"c-69-248-142-135.hsd1.nj.comcast.net\",\n        \"merton.whererwerunning.com\",\n        \"unknown.sagonet.net\",\n        \"under-eepc58.kaist.ac.kr\",\n        \"24-54-76-216.bflony.adelphia.net\",\n        \"lns-vlq-45-tou-82-252-162-81.adsl.proxad.net\",\n        \"ip-216-69-169-168.ip.secureserver.net\",\n        \"adsl-70-242-75-179.dsl.ksc2mo.swbell.net\",\n        \"061092085098.ctinets.com\",\n        \"d211-116-254-214.rev.krline.net\",\n        \"n219076184117.netvigator.com\",\n        \"massive.merukuru.org\"\n    ],\n    \"memory\": [\n        {\n            \"Memory available\": \"125312k\",\n            \"Memory total\": \"129720k\",\n            \"apg memory\": \"93M\"\n        }\n    ]\n}"
claude_3_opus_result = json.loads(result_str)

# *************************LLAMA 3.1 405B on 1st chunk:*************************
# time cost: 191.97198605537415
# {\n    "IP": [\n        "209.184.7.130",\n        "218.188.2.4",\n        "211.46.241.200",\n        "222.33.90.199",\n        "61.218.67.60",\n        "212.5.120.141",\n        "65.35.73.251",\n        "218.38.14.205",\n        "61.153.202.254",\n        "211.233.12.249",\n        "202.101.42.106",\n        "220-135-151-1.hinet-ip.hinet.net",\n        "218.188.2.4",\n        "061092085098.ctinets.com",\n        "d211-116-254-214.rev.krline.net",\n        "24.54.76.216",\n        "82.252.162.81",\n        "adsl-70-242-75-179.dsl.ksc2mo.swbell.net",\n        "n219076184117.netvigator.com",\n        "209.152.168.249",\n        "218.22.3.51",\n        "218.69.108.57",\n        "massive.merukuru.org",\n        "210.118.170.95"\n    ],\n    "URL": [\n        "itsc.iasi.astral.ro",\n        "unknown.sagonet.net",\n        "under-eepc58.kaist.ac.kr",\n        "mail.net-star.com.tw",\n        "host-141.STSK.macomnet.net",\n        "251-73.35-65.tampabay.res.rr.com",\n        "lns-vlq-45-tou-82-252-162-81.adsl.proxad.net",\n        "24-54-76-216.bflony.adelphia.net",\n        "ip-216-69-169-168.ip.secureserver.net",\n        "200.60.37.201",\n        "210.245.165.136",\n        "65.166.159.14"\n    ],\n    "memory": [\n        {\n            "Memory available": "125312k",\n            "Memory total": "129720k",\n            "apg memory": "93M"\n        }\n    ]\n}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
result_str = """{\n    "IP": [\n        "209.184.7.130",\n        "218.188.2.4",\n        "211.46.241.200",\n        "222.33.90.199",\n        "61.218.67.60",\n        "212.5.120.141",\n        "65.35.73.251",\n        "218.38.14.205",\n        "61.153.202.254",\n        "211.233.12.249",\n        "202.101.42.106",\n        "220-135-151-1.hinet-ip.hinet.net",\n        "218.188.2.4",\n        "061092085098.ctinets.com",\n        "d211-116-254-214.rev.krline.net",\n        "24.54.76.216",\n        "82.252.162.81",\n        "adsl-70-242-75-179.dsl.ksc2mo.swbell.net",\n        "n219076184117.netvigator.com",\n        "209.152.168.249",\n        "218.22.3.51",\n        "218.69.108.57",\n        "massive.merukuru.org",\n        "210.118.170.95"\n    ],\n    "URL": [\n        "itsc.iasi.astral.ro",\n        "unknown.sagonet.net",\n        "under-eepc58.kaist.ac.kr",\n        "mail.net-star.com.tw",\n        "host-141.STSK.macomnet.net",\n        "251-73.35-65.tampabay.res.rr.com",\n        "lns-vlq-45-tou-82-252-162-81.adsl.proxad.net",\n        "24-54-76-216.bflony.adelphia.net",\n        "ip-216-69-169-168.ip.secureserver.net",\n        "200.60.37.201",\n        "210.245.165.136",\n        "65.166.159.14"\n    ],\n    "memory": [\n        {\n            "Memory available": "125312k",\n            "Memory total": "129720k",\n            "apg memory": "93M"\n        }\n    ]\n}"""
llama_3_1_405B_result = json.loads(result_str)


# *************************Mistral Large 2407 on 1st chunk:*************************
# #only almost 1/3 of 128k input text
# time cost: 74.60944819450378
# ```json
mistral_large_result = {
    "IP": [
        "127.0.0.1",
        "63.126.79.67",
        "63.126.79.69",
        "63.126.79.70",
        "63.126.79.71",
        "63.126.79.72",
        "63.126.79.73",
        "63.126.79.75",
        "63.126.79.80",
        "63.126.79.81",
        "63.126.79.82",
        "63.126.79.83",
        "63.126.79.84",
        "63.126.79.85",
        "63.126.79.87",
        "63.126.79.89",
        "63.126.79.90",
        "63.126.79.95",
        "63.126.79.100",
        "63.126.79.105",
        "63.126.79.110",
        "63.126.79.115",
        "63.126.79.120",
        "63.126.79.125",
        "209.184.7.130",
        "127.0.0.1",
        "127.0.0.1"
    ],
    "URL": [
        "itsc.iasi.astral.ro",
        "unknown.sagonet.net",
        "unknown.sagonet.net",
        "unknown.sagonet.net"
    ],
    "memory": [
        {
            "Memory available": "125312k",
            "Memory total": "129720k",
            "apg memory": "93M"
        }
    ]
}

results = {
    "gemini_pro_1_5": gemini_pro_1_5_result,
    "claude_3_5_sonnet_20240620": claude_3_5_sonnet_result,
    "claude_3_opus_20240229": claude_3_opus_result,
    "llama_3_1_405B": llama_3_1_405B_result,
    "mistral_large": mistral_large_result

}