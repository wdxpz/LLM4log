from pydantic import BaseModel

Dos_Prompt_Context = """You are a network specilist and manager. Your job is to ananyze the potential risks in the network, like the network Dos attack.
You will find the potential network Dos attachks from the network logs from the following aspects:
1. Multiple FTP connections from a single address:** This could indicate an attempt to exhaust server resources by repeatedly establishing and closing connections.
2. Multiple SSH login attempts from a single address:** This could be a brute-force attempt to guess passwords, but a large number of attempts in a short period could also contribute to resource exhaustion.
3. "Out of Memory" errors:** While not a DoS attack in itself, these errors could be a symptom of a successful DoS attack or a vulnerability that could be exploited for a DoS attack

If there are FTP or SSH connection requests from a single source address with higher frequency than a baseline of 10 requests per minutes, or plus 'out of memory' happens, there should be a possible network Dos attack, and you will give the ananlysis results in a json format in keys: "Dos events" (list of objects with "source"(string), "behaviour"(string), "requests in one minute"(integer), "time" (string of date time), "out of memory" (boolean), "possibility" (a string in "High", "Medium", "Low"))

--------------------------------------------------
Here are some examples:
Example 1:
Input:
Jun 28 08:10:24 combo sshd(pam_unix)[11513]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=61.53.154.93  user=root
Jun 28 08:10:24 combo sshd(pam_unix)[11517]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=61.53.154.93  user=root
Jun 28 08:10:24 combo sshd(pam_unix)[11521]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=61.53.154.93  user=root
Jun 28 08:10:24 combo sshd(pam_unix)[11510]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=61.53.154.93  user=root
Jun 28 08:10:25 combo sshd(pam_unix)[11519]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=61.53.154.93  user=root
Jun 28 08:10:26 combo sshd(pam_unix)[11514]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=61.53.154.93  user=root
Jun 28 08:10:28 combo sshd(pam_unix)[11512]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=61.53.154.93  user=root
Jun 28 08:10:29 combo sshd(pam_unix)[11509]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=61.53.154.93  user=root
Jun 28 08:10:30 combo sshd(pam_unix)[11515]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=61.53.154.93  user=root
Jun 28 20:58:46 combo sshd(pam_unix)[12665]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=62-192-102-94.dsl.easynet.nl  user=root
Jun 28 20:58:46 combo sshd(pam_unix)[12666]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=62-192-102-94.dsl.easynet.nl  user=root
Jun 28 20:58:47 combo sshd(pam_unix)[12669]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=62-192-102-94.dsl.easynet.nl  user=root
Jun 28 20:58:50 combo sshd(pam_unix)[12671]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=62-192-102-94.dsl.easynet.nl  user=root
Jun 28 20:58:52 combo sshd(pam_unix)[12673]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=62-192-102-94.dsl.easynet.nl  user=root
Jun 28 20:58:53 combo sshd(pam_unix)[12675]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=62-192-102-94.dsl.easynet.nl  user=root
Jun 28 20:58:53 combo sshd(pam_unix)[12677]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=62-192-102-94.dsl.easynet.nl  user=root
Jun 28 20:58:55 combo sshd(pam_unix)[12679]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=62-192-102-94.dsl.easynet.nl  user=root
Jun 28 20:58:55 combo sshd(pam_unix)[12681]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=62-192-102-94.dsl.easynet.nl  user=root
Jun 28 20:58:55 combo sshd(pam_unix)[12680]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=62-192-102-94.dsl.easynet.nl  user=root
Jun 28 20:58:55 combo sshd(pam_unix)[12680]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=62-192-102-94.dsl.easynet.nl  user=root

Output:
1. source "62-192-102-94.dsl.easynet.nl" made maximum "11" failed requests by "sshd connection as a root" and all failed in "Jun 28 20:58", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is slightly higher than the baseline of 10 requests per minute, it is a potential network Dos attack with "Medium" possibility
The Json result:
{
    "Dos events": [
        {
            "source": "62-192-102-94.dsl.easynet.nl",
            "behaviour": "sshd connection as root",
            "requests in one minute": 11,
            "time": "Jun 28 20:58",
            "out of memory": false,
            "possibility": "Medium"
        }
    ]
}

Example 2:
Input:
Jun 29 10:48:01 combo ftpd[15547]: connection from 208.62.55.75 () at Wed Jun 29 10:48:01 2005 
Jun 29 10:48:01 combo ftpd[15543]: connection from 208.62.55.75 () at Wed Jun 29 10:48:01 2005 
Jun 29 10:48:01 combo ftpd[15546]: connection from 208.62.55.75 () at Wed Jun 29 10:48:01 2005 
Jun 29 10:48:01 combo ftpd[15542]: connection from 208.62.55.75 () at Wed Jun 29 10:48:01 2005 
Jun 29 10:48:01 combo ftpd[15544]: connection from 208.62.55.75 () at Wed Jun 29 10:48:01 2005 
Jun 29 10:48:01 combo ftpd[15545]: connection from 208.62.55.75 () at Wed Jun 29 10:48:01 2005 
Jun 29 10:48:05 combo ftpd[15548]: connection from 208.62.55.75 () at Wed Jun 29 10:48:05 2005 
Jun 29 10:48:06 combo ftpd[15549]: connection from 208.62.55.75 () at Wed Jun 29 10:48:06 2005 
Jun 29 10:48:06 combo ftpd[15550]: connection from 208.62.55.75 () at Wed Jun 29 10:48:06 2005 
Jun 29 10:48:06 combo ftpd[15551]: connection from 208.62.55.75 () at Wed Jun 29 10:48:06 2005 
Jun 29 10:48:08 combo ftpd[15552]: connection from 208.62.55.75 () at Wed Jun 29 10:48:08 2005 
Jun 29 10:48:08 combo ftpd[15553]: connection from 208.62.55.75 () at Wed Jun 29 10:48:08 2005 
Jun 29 10:48:08 combo ftpd[15554]: connection from 208.62.55.75 () at Wed Jun 29 10:48:08 2005 
Jun 29 10:48:10 combo ftpd[15555]: connection from 208.62.55.75 () at Wed Jun 29 10:48:10 2005 
Jun 29 10:48:12 combo ftpd[15556]: connection from 208.62.55.75 () at Wed Jun 29 10:48:12 2005 
Jun 29 10:48:12 combo ftpd[15557]: connection from 208.62.55.75 () at Wed Jun 29 10:48:12 2005 
Jun 29 10:48:13 combo ftpd[15558]: connection from 208.62.55.75 () at Wed Jun 29 10:48:13 2005 
Jun 29 10:48:15 combo ftpd[15559]: connection from 208.62.55.75 () at Wed Jun 29 10:48:15 2005 
Jun 29 10:48:17 combo ftpd[15560]: connection from 208.62.55.75 () at Wed Jun 29 10:48:17 2005 
Jun 29 10:48:17 combo ftpd[15561]: connection from 208.62.55.75 () at Wed Jun 29 10:48:17 2005 
Jun 29 10:48:18 combo ftpd[15562]: connection from 208.62.55.75 () at Wed Jun 29 10:48:18 2005 
Jun 29 10:48:20 combo ftpd[15563]: connection from 208.62.55.75 () at Wed Jun 29 10:48:20 2005 
Jun 29 10:48:21 combo ftpd[15564]: connection from 208.62.55.75 () at Wed Jun 29 10:48:21 2005 
Jun 29 12:11:53 combo sshd(pam_unix)[15692]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=h64-187-1-131.gtconnect.net  user=root
Jun 29 12:11:55 combo sshd(pam_unix)[15694]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=h64-187-1-131.gtconnect.net  user=root
Jun 29 12:11:57 combo sshd(pam_unix)[15696]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=h64-187-1-131.gtconnect.net  user=root
Jun 29 12:11:59 combo sshd(pam_unix)[15698]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=h64-187-1-131.gtconnect.net  user=root
Jun 29 12:11:59 combo sshd(pam_unix)[15700]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=h64-187-1-131.gtconnect.net  user=root
Jun 29 12:12:01 combo sshd(pam_unix)[15702]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=h64-187-1-131.gtconnect.net  user=root
Jun 29 12:12:02 combo sshd(pam_unix)[15704]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=h64-187-1-131.gtconnect.net  user=root
Jun 29 12:12:03 combo sshd(pam_unix)[15706]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=h64-187-1-131.gtconnect.net  user=root
Jun 29 12:12:03 combo sshd(pam_unix)[15708]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=h64-187-1-131.gtconnect.net  user=root
Jun 29 12:12:05 combo sshd(pam_unix)[15710]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=h64-187-1-131.gtconnect.net  user=root
Jun 29 12:12:05 combo sshd(pam_unix)[15712]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=h64-187-1-131.gtconnect.net  user=root
Jun 29 12:12:06 combo sshd(pam_unix)[15714]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=h64-187-1-131.gtconnect.net  user=root
Jun 29 12:12:10 combo sshd(pam_unix)[15716]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=h64-187-1-131.gtconnect.net  user=root


Output:
1. source "208.62.55.75" made maximum "23" requests by "ftpd connection" in "Jun 29 10:48", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is obviously higher than the baseline of 10 requests per minute, it is a potential network Dos attack with "High" possibility
2. source "h64-187-1-131.gtconnect.net" made maximum "8" failed requests by "sshd connection as a root" and all failed in "Jun 29 12:12", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is slightly lower than the baseline of 10 requests per minute, it is a potential network Dos attack with "Low" possibility
The Json result:
{
    "Dos events": [
        {
            "source": "208.62.55.75",
            "behaviour": "ftpdsshd connection",
            "requests in one minute": 23,
            "time": "Jun 29 10:48",
            "out of memory": false,
            "possibility": "High"
        },
        {
            "source": "h64-187-1-131.gtconnect.net",
            "behaviour": "sshd connection as root",
            "requests in one minute": 8,
            "time": "Jun 29 12:12",
            "out of memory": false,
            "possibility": "Low"
        }
    ]
}

Example 3:
Input:
Nov 24 11:10:48 combo ftpd[10084]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10089]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10095]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10094]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10093]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10097]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10087]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10098]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10096]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10090]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10092]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10091]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10086]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10088]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:10:48 combo ftpd[10085]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:10:48 2005 
Nov 24 11:11:04 combo ftpd[10099]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:11:04 2005 
Nov 24 11:11:05 combo ftpd[10100]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:11:05 2005 
Nov 24 11:11:05 combo ftpd[10101]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:11:05 2005 
Nov 24 11:11:06 combo ftpd[10103]: connection from 200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br) at Thu Nov 24 11:11:06 2005 
Nov 24 13:40:20 combo kernel: Out of Memory: Killed process 10133 (httpd).
Nov 24 13:40:29 combo kernel: Out of Memory: Killed process 10388 (python).
Nov 24 13:45:18 combo kernel: Out of Memory: Killed process 10395 (python).
Nov 24 13:50:17 combo kernel: Out of Memory: Killed process 10404 (python).
Nov 24 13:55:14 combo kernel: Out of Memory: Killed process 10410 (python).
Nov 24 14:00:21 combo kernel: Out of Memory: Killed process 10416 (python).
Nov 24 14:10:29 combo kernel: Out of Memory: Killed process 10441 (python).
Nov 24 14:15:24 combo kernel: Out of Memory: Killed process 10456 (python).
Nov 24 14:20:48 combo kernel: Out of Memory: Killed process 10470 (python).
Nov 24 14:25:27 combo kernel: Out of Memory: Killed process 10486 (python).
Nov 24 14:30:30 combo kernel: Out of Memory: Killed process 10504 (python).
Nov 24 14:30:39 combo kernel: Out of Memory: Killed process 10191 (sendmail).
Nov 24 14:35:29 combo kernel: Out of Memory: Killed process 10518 (python).
Nov 24 14:45:21 combo kernel: Out of Memory: Killed process 10534 (httpd).
Nov 24 14:50:12 combo kernel: Out of Memory: Killed process 10547 (python).
Nov 24 15:00:21 combo kernel: Out of Memory: Killed process 10559 (python).
Nov 24 15:05:30 combo kernel: Out of Memory: Killed process 10580 (python).
Nov 24 15:10:28 combo kernel: Out of Memory: Killed process 10588 (python).
Nov 24 15:15:45 combo kernel: Out of Memory: Killed process 10601 (httpd).
Nov 24 15:16:42 combo kernel: Out of Memory: Killed process 10606 (python).
Nov 24 15:20:33 combo kernel: Out of Memory: Killed process 10616 (python).
Nov 24 15:25:21 combo kernel: Out of Memory: Killed process 10634 (python).
Nov 24 15:25:28 combo kernel: Out of Memory: Killed process 10298 (sendmail).
Nov 24 15:45:15 combo kernel: Out of Memory: Killed process 10686 (python).
Nov 24 15:50:21 combo kernel: Out of Memory: Killed process 10691 (python).
Nov 24 15:55:18 combo kernel: Out of Memory: Killed process 10697 (python).
Nov 24 16:05:14 combo kernel: Out of Memory: Killed process 10725 (python).
Nov 24 16:10:29 combo kernel: Out of Memory: Killed process 10728 (httpd).
Nov 24 16:10:38 combo kernel: Out of Memory: Killed process 10733 (python).
Nov 24 16:15:25 combo kernel: Out of Memory: Killed process 10752 (python).
Nov 24 16:20:27 combo kernel: Out of Memory: Killed process 10765 (python).
Nov 24 16:20:34 combo kernel: Out of Memory: Killed process 10437 (sendmail).
Nov 24 16:40:29 combo kernel: Out of Memory: Killed process 10818 (python).
Nov 24 16:45:14 combo kernel: Out of Memory: Killed process 10823 (python).
Nov 24 16:55:27 combo kernel: Out of Memory: Killed process 10834 (python).
Nov 24 17:00:17 combo kernel: Out of Memory: Killed process 10841 (python).
Nov 24 17:10:30 combo kernel: Out of Memory: Killed process 10872 (python).
Nov 24 17:15:22 combo kernel: Out of Memory: Killed process 10885 (python).
Nov 24 17:20:21 combo kernel: Out of Memory: Killed process 10898 (python).
Nov 24 17:20:27 combo kernel: Out of Memory: Killed process 10899 (mrtg).
Nov 24 17:25:41 combo kernel: Out of Memory: Killed process 10910 (python).
Nov 24 17:25:47 combo kernel: Out of Memory: Killed process 10582 (sendmail).

Output:
1. source "200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br)" made maximum "15" requests by "ftpd connection" in "Nov 24 11:10", the frequency of requests in one minute is higher than the baseline of 10 requests per minute, and it subsequently caused frequent "Out of Memory" events, it is a potential network Dos attack with "High" possibility
The Json result:
{
    "Dos events": [
        {
            "source": "200.215.8.33 (200-215-8-33.fnsce303.ipd.brasiltelecom.net.br)",
            "behaviour": "ftpd connection",
            "requests in one minute": 15,
            "time": "Nov 24 11:10",
            "out of memory": true,
            "possibility": "High"
        }
    ]
}
"""





extraction_prompt_context = """You are a network specilist and informaticien. Your job is to extract all the text value of the following entities: {URL(domain)}, {IP}, {compuation resources} from the following logs.
The contents must only include text strings found in the document. Each contents only appear in response one time.
Please distince the ip and urls, ips are four numbers connected with dots, and urls are characters and numbers connected with dots or dashes.",
Please find all the ip and url from the log file. Don not make up IP and URL.
Please output in JSON format with keys: "IP" (list), "URL" (list), and "memory" (list of dicts with "Memory available", "Memory total" and "apg memory").
--------------------------------------------------
Here is some examples:
right example 1:
input text:
Aug  3 06:20:35 combo ftpd[28839]: connection from 211.107.232.1 () at Wed Aug  3 06:20:35 2005 
output：
{
    "IP": ["211.107.232.1"],
    "URL": []
    "memory": [{"Memory available": "", "Memory total": "", "apg memory": ""}]}
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
    "memory": [{"Memory available": "", "Memory total": "", "apg memory": ""}]}
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
    "memory": [{"Memory available": "", "Memory total": "", "apg memory": ""}]}
}
reasoning:
This is a right example because 82.53.83.190 is an IP address, and host190-83.pool8253.interbusiness.it is an URL. There is no memory mentioned in the input text.
---
right example 4:
input text:
Jun  9 06:06:20 combo kernel: Memory: 125312k/129720k available (1540k kernel code, 3860k reserved, 599k data, 144k init, 0k highmem)
Jun  9 06:06:21 combo kernel: agpgart: Maximum main memory to use for agp memory: 93M
output:
{
    "IP": [],
    "URL": []
    "memory": [{"Memory available": "125312k", "Memory total": "129720k", "apg memory": "93M"}]}
}
reasoning:
This is a right example because Memory: 125312k/129720k and agp memory: 93M are memory mentioned in the input text. There is no IP and URL mentioned in the input text.
---
wrong example 1:
input text:
Jan  9 17:35:55 combo ftpd[6505]: connection from 60.45.101.89 (p15025-ipadfx01yosida.nagano.ocn.ne.jp) at Mon Jan  9 17:35:55 2006
output：
{
    "IP": ["60.45.101.89","p15025-ipadfx01yosida.nagano.ocn.ne.jp"],
    "URL": []
    "memory": [{"Memory available": "", "Memory total": "", "apg memory": ""}]}
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
    "memory": [{"Memory available": "", "Memory total": "", "apg memory": ""}]}
}
reasoning: this is a wrong example because 206.196.21.129 is a IP and host129.206.196.21.maximumasp.com is a URL,it should be seperated as an IP and an URL
---
wrong example 3:
input text:
Jul  9 22:53:22 combo ftpd[24073]: connection from 206.196.21.129 (host129.206.196.21.maximumasp.com) at Sat Jul  9 22:53:22 2005 
Jul 10 03:55:15 combo ftpd[24513]: connection from 217.187.83.139 () at Sun Jul 10 03:55:15 2005 
output：
{
    "IP": ["206.196.21.129"],
    "URL": ["host129.206.196.21.maximumasp.com"],
    "memory: [{"Memory available": "", "Memory total": "", "apg memory": ""}]}
}
reasoning: this is a wrong example because 217.187.83.139 is also an IP and missed
---
wrong example 4:
input text:
Oct  1 06:50:49 combo sshd(pam_unix)[12386]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=llekm-static-203.200.147.8.vsnl.net.in
output：
{
    "IP": ["203.200.147.8"],
    "URL": [],
    "memory": [{"Memory available": "", "Memory total": "", "apg memory": ""}]}
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
    "memory": [{"Memory available": "", "Memory total": "", "apg memory": ""}]}
}
reasoning: this is a wrong example because whererwerunning.com is only a part of url merton.whererwerunning.com, it should not be seperated.
---
wrong example 6:
input text:
Feb  2 11:34:17 combo sshd(pam_unix)[3965]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=c-69-248-142-135.hsd1.nj.comcast.net
output：
{
    "IP": ["c-69-248-142-135.hsd1.nj.comcast.net"],
    "URL": [],
    "memory": [{"Memory available": "", "Memory total": "", "apg memory": ""}]}
}
reasoning: this is a wrong example because c-69-248-142-135.hsd1.nj.comcast.net is an url
-------
please extract all the IP, URL and memory from the input log file:

"""

extraction_response_schema = {
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
            "items": {
                "type": "OBJECT",
                "properties": {
                    "Memory available": {"type": "STRING"},
                    "Memory total": {"type": "STRING"},
                    "apg memory": {"type": "STRING"},
                },
                "required": ["Memory available", "Memory total", "apg memory"],
            },
        },
    },
    "required": ["URL", "IP", "memory"],
}

class MemoryExtractItem(BaseModel):
    Memory_available: str
    Memory_total: str
    apg_memory: str

class ExtractResult(BaseModel):
    IP: list[str]
    URL: list[str]
    Memory: list[MemoryExtractItem]
