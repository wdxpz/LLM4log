import vertexai

from vertexai.generative_models import GenerationConfig, GenerativeModel

# TODO(developer): Update and un-comment below line
project_id = "log-extraction"
vertexai.init(project=project_id, location="us-central1")

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
        "url": {
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
    "required": ["url", "IP", "memory"],
}


prompt = """Given a document, your task is to extract the text value of the following entities: {url(domain)}, {IP}, {compuation resources(memory, cpu)}
- The contents must only include text strings found in the document.
- The contents only apear in response one time. Please list them in different catagories.
Feb 19 11:29:58 combo sshd(pam_unix)[5386]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=222.168.14.22 
Feb 19 21:28:43 combo sshd(pam_unix)[5447]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=211.96.97.37  user=root
Feb 19 21:28:43 combo sshd(pam_unix)[5443]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=211.96.97.37  user=root
Feb 19 21:28:43 combo sshd(pam_unix)[5446]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=211.96.97.37  user=root
Feb 19 21:28:43 combo sshd(pam_unix)[5442]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=211.96.97.37  user=root
Feb 19 21:28:43 combo sshd(pam_unix)[5448]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=211.96.97.37  user=root
Feb 19 21:28:44 combo sshd(pam_unix)[5451]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=211.96.97.37  user=root
Feb 19 21:28:44 combo sshd(pam_unix)[5452]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=211.96.97.37  user=root
Feb 19 21:28:44 combo sshd(pam_unix)[5457]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=211.96.97.37  user=root
Feb 19 21:28:44 combo sshd(pam_unix)[5454]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=211.96.97.37  user=root
Feb 19 21:28:45 combo sshd(pam_unix)[5459]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=211.96.97.37  user=root
Feb 20 07:24:30 combo sshd(pam_unix)[5626]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=210.14.28.60  user=root
Feb 20 07:24:30 combo sshd(pam_unix)[5628]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=210.14.28.60  user=root
Feb 20 07:24:30 combo sshd(pam_unix)[5617]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=210.14.28.60  user=root
Feb 20 07:24:30 combo sshd(pam_unix)[5624]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=210.14.28.60  user=root
Feb 20 07:24:30 combo sshd(pam_unix)[5614]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=210.14.28.60  user=root
Feb 20 07:24:30 combo sshd(pam_unix)[5618]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=210.14.28.60  user=root
Feb 20 07:24:30 combo sshd(pam_unix)[5616]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=210.14.28.60  user=root
Feb 20 07:24:30 combo sshd(pam_unix)[5625]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=210.14.28.60  user=root
Feb 20 07:24:30 combo sshd(pam_unix)[5627]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=210.14.28.60  user=root
Feb 20 07:24:30 combo sshd(pam_unix)[5615]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=210.14.28.60  user=root
Feb 20 07:36:03 combo ftpd[5647]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5640]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5642]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5643]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5641]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5645]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5644]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5648]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5646]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5634]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5637]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5638]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5636]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5639]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:03 combo ftpd[5635]: connection from 219.145.93.74 () at Mon Feb 20 07:36:03 2006 
Feb 20 07:36:04 combo ftpd[5649]: connection from 219.145.93.74 () at Mon Feb 20 07:36:04 2006 
Feb 20 07:36:04 combo ftpd[5650]: connection from 219.145.93.74 () at Mon Feb 20 07:36:04 2006 
Feb 20 07:36:06 combo ftpd[5651]: connection from 219.145.93.74 () at Mon Feb 20 07:36:06 2006 
Feb 20 07:36:07 combo ftpd[5652]: connection from 219.145.93.74 () at Mon Feb 20 07:36:07 2006 
Feb 20 12:14:13 combo unix_chkpwd[5702]: check pass; user unknown
Feb 20 12:14:13 combo sshd(pam_unix)[5688]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:14 combo unix_chkpwd[5703]: check pass; user unknown
Feb 20 12:14:14 combo sshd(pam_unix)[5686]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:15 combo unix_chkpwd[5706]: check pass; user unknown
Feb 20 12:14:15 combo sshd(pam_unix)[5690]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:17 combo unix_chkpwd[5708]: check pass; user unknown
Feb 20 12:14:17 combo sshd(pam_unix)[5694]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:18 combo unix_chkpwd[5711]: check pass; user unknown
Feb 20 12:14:18 combo sshd(pam_unix)[5692]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:18 combo unix_chkpwd[5712]: check pass; user unknown
Feb 20 12:14:18 combo sshd(pam_unix)[5696]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:23 combo unix_chkpwd[5724]: check pass; user unknown
Feb 20 12:14:23 combo sshd(pam_unix)[5698]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:23 combo unix_chkpwd[5725]: check pass; user unknown
Feb 20 12:14:23 combo sshd(pam_unix)[5700]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:24 combo unix_chkpwd[5726]: check pass; user unknown
Feb 20 12:14:24 combo sshd(pam_unix)[5704]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:28 combo unix_chkpwd[5727]: check pass; user unknown
Feb 20 12:14:28 combo sshd(pam_unix)[5707]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:29 combo unix_chkpwd[5728]: check pass; user unknown
Feb 20 12:14:29 combo sshd(pam_unix)[5709]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:29 combo unix_chkpwd[5729]: check pass; user unknown
Feb 20 12:14:29 combo sshd(pam_unix)[5715]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:30 combo unix_chkpwd[5730]: check pass; user unknown
Feb 20 12:14:30 combo sshd(pam_unix)[5714]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:30 combo unix_chkpwd[5731]: check pass; user unknown
Feb 20 12:14:30 combo sshd(pam_unix)[5718]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:31 combo unix_chkpwd[5732]: check pass; user unknown
Feb 20 12:14:31 combo sshd(pam_unix)[5720]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 20 12:14:32 combo unix_chkpwd[5733]: check pass; user unknown
Feb 20 12:14:32 combo sshd(pam_unix)[5722]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=vedgi-gw.rosprint.net 
Feb 22 01:55:44 combo ftpd[5772]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5773]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5774]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5778]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5775]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5777]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5776]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5779]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5762]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5767]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5766]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5765]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5764]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5760]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5770]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5761]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5771]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5768]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5759]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5769]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5763]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5780]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 01:55:44 combo ftpd[5781]: connection from 210.212.240.242 () at Wed Feb 22 01:55:44 2006 
Feb 22 11:46:37 combo sshd(pam_unix)[5989]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=203186089173.ctinets.com  user=root
Feb 22 11:46:37 combo sshd(pam_unix)[5992]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=203186089173.ctinets.com  user=root
Feb 22 11:46:38 combo sshd(pam_unix)[5991]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=203186089173.ctinets.com  user=root
Feb 22 11:46:38 combo sshd(pam_unix)[5995]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=203186089173.ctinets.com  user=root
Feb 22 11:46:38 combo sshd(pam_unix)[5996]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=203186089173.ctinets.com  user=root
Feb 22 11:46:39 combo sshd(pam_unix)[6001]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=203186089173.ctinets.com  user=root
Feb 22 11:46:39 combo sshd(pam_unix)[5997]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=203186089173.ctinets.com  user=root
Feb 22 11:46:41 combo sshd(pam_unix)[6005]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=203186089173.ctinets.com  user=root
Feb 22 11:46:41 combo sshd(pam_unix)[6004]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=203186089173.ctinets.com  user=root
Feb 22 11:46:42 combo sshd(pam_unix)[6003]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=203186089173.ctinets.com  user=root
Feb 22 13:26:34 combo sshd(pam_unix)[6028]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=220.194.58.127  user=root
Feb 22 13:26:34 combo sshd(pam_unix)[6022]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=220.194.58.127  user=root
Feb 22 13:26:34 combo sshd(pam_unix)[6027]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=220.194.58.127  user=root
Feb 22 13:26:34 combo sshd(pam_unix)[6020]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=220.194.58.127  user=root
Feb 22 13:26:34 combo sshd(pam_unix)[6029]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=220.194.58.127  user=root
Feb 22 13:26:34 combo sshd(pam_unix)[6030]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=220.194.58.127  user=root
Feb 22 13:26:34 combo sshd(pam_unix)[6031]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=220.194.58.127  user=root
Feb 22 13:26:34 combo sshd(pam_unix)[6032]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=220.194.58.127  user=root
Feb 22 13:26:34 combo sshd(pam_unix)[6026]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=220.194.58.127  user=root
Feb 22 13:26:34 combo sshd(pam_unix)[6021]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=220.194.58.127  user=root
Feb 22 23:41:37 combo ftpd[6043]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6048]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6042]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6044]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6041]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6046]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6050]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6049]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6051]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6054]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6045]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6055]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6047]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6052]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6053]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6056]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6057]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6058]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6059]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:37 combo ftpd[6060]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:37 2006 
Feb 22 23:41:38 combo ftpd[6061]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:38 2006 
Feb 22 23:41:38 combo ftpd[6062]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:38 2006 
Feb 22 23:41:38 combo ftpd[6063]: connection from 24.229.9.65 (24.229.9.65.res-cmts.sm.ptd.net) at Wed Feb 22 23:41:38 2006 
Feb 23 12:02:26 combo sshd(pam_unix)[6064]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=80.34.110.175  user=fax
Feb 23 12:02:26 combo sshd(pam_unix)[6070]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=175.red-80-34-110.staticip.rima-tde.net  user=fax
Feb 23 12:02:26 combo sshd(pam_unix)[6072]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=175.red-80-34-110.staticip.rima-tde.net  user=fax
Feb 23 12:02:26 combo sshd(pam_unix)[6066]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=175.red-80-34-110.staticip.rima-tde.net  user=fax
Feb 23 12:02:26 combo sshd(pam_unix)[6067]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=175.red-80-34-110.staticip.rima-tde.net  user=fax
Feb 23 12:02:26 combo sshd(pam_unix)[6073]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=175.red-80-34-110.staticip.rima-tde.net  user=fax
Feb 23 13:54:46 combo unix_chkpwd[6096]: check pass; user unknown
Feb 23 13:54:46 combo sshd(pam_unix)[6076]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66.50.123.66 
Feb 23 13:54:47 combo unix_chkpwd[6097]: check pass; user unknown
Feb 23 13:54:47 combo sshd(pam_unix)[6078]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 13:54:47 combo unix_chkpwd[6098]: check pass; user unknown
Feb 23 13:54:47 combo unix_chkpwd[6099]: check pass; user unknown
Feb 23 13:54:47 combo sshd(pam_unix)[6080]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 13:54:47 combo sshd(pam_unix)[6094]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 13:54:47 combo unix_chkpwd[6100]: check pass; user unknown
Feb 23 13:54:47 combo sshd(pam_unix)[6082]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 13:54:47 combo unix_chkpwd[6101]: check pass; user unknown
Feb 23 13:54:47 combo sshd(pam_unix)[6084]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 13:54:49 combo unix_chkpwd[6102]: check pass; user unknown
Feb 23 13:54:49 combo sshd(pam_unix)[6086]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 13:54:50 combo unix_chkpwd[6103]: check pass; user unknown
Feb 23 13:54:50 combo sshd(pam_unix)[6087]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 13:54:50 combo unix_chkpwd[6104]: check pass; user unknown
Feb 23 13:54:50 combo sshd(pam_unix)[6090]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 13:54:51 combo unix_chkpwd[6105]: check pass; user unknown
Feb 23 13:54:51 combo sshd(pam_unix)[6092]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 18:10:47 combo unix_chkpwd[6126]: check pass; user unknown
Feb 23 18:10:47 combo sshd(pam_unix)[6108]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 18:10:47 combo unix_chkpwd[6127]: check pass; user unknown
Feb 23 18:10:47 combo sshd(pam_unix)[6109]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 18:10:47 combo unix_chkpwd[6128]: check pass; user unknown
Feb 23 18:10:47 combo sshd(pam_unix)[6110]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 18:10:48 combo unix_chkpwd[6129]: check pass; user unknown
Feb 23 18:10:48 combo sshd(pam_unix)[6112]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 18:10:48 combo unix_chkpwd[6130]: check pass; user unknown
Feb 23 18:10:48 combo sshd(pam_unix)[6114]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 18:10:48 combo unix_chkpwd[6131]: check pass; user unknown
Feb 23 18:10:48 combo sshd(pam_unix)[6117]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 18:10:48 combo unix_chkpwd[6132]: check pass; user unknown
Feb 23 18:10:48 combo sshd(pam_unix)[6119]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 18:10:48 combo unix_chkpwd[6133]: check pass; user unknown
Feb 23 18:10:48 combo sshd(pam_unix)[6121]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 18:10:48 combo unix_chkpwd[6134]: check pass; user unknown
Feb 23 18:10:48 combo sshd(pam_unix)[6106]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 18:10:48 combo unix_chkpwd[6135]: check pass; user unknown
Feb 23 18:10:48 combo sshd(pam_unix)[6124]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=66-50-123-66.prtc.net 
Feb 23 20:41:54 combo ftpd[6136]: connection from 89.52.108.101 () at Thu Feb 23 20:41:54 2006 
Feb 23 20:41:54 combo ftpd[6137]: connection from 89.52.108.101 (P6c65.p.pppool.de) at Thu Feb 23 20:41:54 2006 
Feb 23 22:52:04 combo ftpd[6138]: connection from 89.52.108.101 (P6c65.p.pppool.de) at Thu Feb 23 22:52:04 2006 
Feb 24 00:39:00 combo ftpd[6139]: connection from 89.52.108.101 (P6c65.p.pppool.de) at Fri Feb 24 00:39:00 2006 
Feb 24 00:39:12 combo ftpd[6140]: connection from 89.52.108.101 (P6c65.p.pppool.de) at Fri Feb 24 00:39:12 2006 
Feb 24 01:20:17 combo ftpd[6142]: connection from 84.102.20.91 (91.20.102-84.rev.gaoland.net) at Fri Feb 24 01:20:17 2006 
Feb 24 01:20:17 combo ftpd[6141]: connection from 84.102.20.91 (91.20.102-84.rev.gaoland.net) at Fri Feb 24 01:20:17 2006 
Feb 24 01:20:17 combo ftpd[6144]: connection from 84.102.20.91 (91.20.102-84.rev.gaoland.net) at Fri Feb 24 01:20:17 2006 
Feb 24 01:20:17 combo ftpd[6143]: connection from 84.102.20.91 (91.20.102-84.rev.gaoland.net) at Fri Feb 24 01:20:17 2006 
Feb 24 01:20:17 combo ftpd[6145]: connection from 84.102.20.91 (91.20.102-84.rev.gaoland.net) at Fri Feb 24 01:20:17 2006 
Feb 24 01:20:17 combo ftpd[6146]: connection from 84.102.20.91 (91.20.102-84.rev.gaoland.net) at Fri Feb 24 01:20:17 2006 
Feb 24 01:20:17 combo ftpd[6147]: connection from 84.102.20.91 (91.20.102-84.rev.gaoland.net) at Fri Feb 24 01:20:17 2006 
Feb 24 01:20:20 combo ftpd[6148]: connection from 84.102.20.91 (91.20.102-84.rev.gaoland.net) at Fri Feb 24 01:20:20 2006 
Feb 24 01:20:20 combo ftpd[6149]: connection from 84.102.20.91 (91.20.102-84.rev.gaoland.net) at Fri Feb 24 01:20:20 2006 
Feb 24 01:20:21 combo ftpd[6148]: ANONYMOUS FTP LOGIN FROM 84.102.20.91, 91.20.102-84.rev.gaoland.net (anonymous)
"""

model = GenerativeModel("gemini-1.5-pro-001")

response = model.generate_content(
    prompt,
    generation_config=GenerationConfig(
        response_mime_type="application/json", response_schema=response_schema
    ),
)

print(response.text)