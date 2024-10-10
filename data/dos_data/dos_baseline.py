#TODO: merge 8 and 9 as one High potential risk
# [0:2] from "Linux_1.txt", [3] from "Linux_6.txt"
Dos_Test_Baselines = [
    """1. source "210.118.170.95" made maximum "13" requests by "ftpd connection" in "Jun 25 19:25", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is slightly higher than the baseline of 10 requests per minute, it is a potential network Dos attack with "Medium" possibility
    2. source "61.53.154.93" made maximum "9" requests by "sshd login as root" and all failed in "Jun 28 08:10", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is slightly lower than the baseline of 10 requests per minute, it is a potential network Dos attack with "Low" possibility
    3. source "62-192-102-94.dsl.easynet.nl" made maximum "10" requests by "sshd login as root" and all failed in "Jun 28 20:58", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is just equal to the baseline of 10 requests per minute, it is a potential network Dos attack with "medium" possibility
    4. source "211.115.206.155" made maximum "5" requests by "sshd login with empty logname" and all failed in "Jun 28 21:42", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is slightly lower than the baseline of 10 requests per minute, it is a potential network Dos attack with "Low" possibility
    5. source "61.74.96.178" made maximum "23" requests by "ftpd connection" in "Jun 29 03:22", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is obviously higher than the baseline of 10 requests per minute, it is a potential network Dos attack with "High" possibility
    6. source "csnsu.nsuok.edu" made maximum "10" requests by "sshd login as root" and all failed in "Jun 29 10:08", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is just equal to the baseline of 10 requests per minute, it is a potential network Dos attack with "Medium" possibility
    7. source "208.62.55.75" made maximum "23" requests by "ftpd connection" in "Jun 29 10:48", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is obviously higher than the baseline of 10 requests per minute, it is a potential network Dos attack with "High" possibility
    8. source "h64-187-1-131.gtconnect.net" made maximum "5" requests by "sshd login as root" and all failed in "Jun 29 12:11", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is slightly lower than the baseline of 5 requests per minute, it is a potential network Dos attack with "Low" possibility
    9. source "h64-187-1-131.gtconnect.net" made maximum "8" requests by "sshd login as root" and all failed in "Jun 29 12:12", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is slightly lower than the baseline of 8 requests per minute, it is a potential network Dos attack with "Low" possibility
    10. source "210.223.97.117" made maximum "7" requests by "ftpd connection" in "Jun 29 14:44", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is slightly lower than the baseline of 10 requests per minute, it is a potential network Dos attack with "Low" possibility
    The Json result:
    {
        "Dos events": [
            {
                "source": "210.118.170.95",
                "behaviour": "ftpd connection",
                "requests in one minute": 13,
                "time": "Jun 25 19:25",
                "out of memory": false,
                "possibility": "Medium"
            },
            {
                "source": "61.53.154.93",
                "behaviour": "sshd login as root",
                "requests in one minute": 9,
                "time": "Jun 28 08:10",
                "out of memory": false,
                "possibility": "Low"
            },
            {
                "source": "62-192-102-94.dsl.easynet.nl",
                "behaviour": "sshd login as root",
                "requests in one minute": 10,
                "time": "Jun 28 20:58",
                "out of memory": false,
                "possibility": "Medium"
            },
            {
                "source": "211.115.206.155",
                "behaviour": "sshd login with empty logname",
                "requests in one minute": 5,
                "time": "Jun 28 21:42",
                "out of memory": false,
                "possibility": "Low"
            },
            {
                "source": "61.74.96.178",
                "behaviour": "ftpd connection",
                "requests in one minute": 23,
                "time": "Jun 29 03:22",
                "out of memory": false,
                "possibility": "High"
            },
            {
                "source": "csnsu.nsuok.edu",
                "behaviour": "sshd login as root",
                "requests in one minute": 10,
                "time": "Jun 29 10:08",
                "out of memory": false,
                "possibility": "Medium"
            },
            {
                "source": "208.62.55.75",
                "behaviour": "ftpd connection",
                "requests in one minute": 23,
                "time": "Jun 29 10:48",
                "out of memory": false,
                "possibility": "High"
            },
            {
                "source": "h64-187-1-131.gtconnect.net",
                "behaviour": "sshd login as root",
                "requests in one minute": 5,
                "time": "Jun 29 12:11",
                "out of memory": false,
                "possibility": "Low"
            },
            {
                "source": "h64-187-1-131.gtconnect.net",
                "behaviour": "sshd login as root",
                "requests in one minute": 8,
                "time": "Jun 29 12:12",
                "out of memory": false,
                "possibility": "Low"
            },
            {
                "source": "210.223.97.117",
                "behaviour": "ftpd connection",
                "requests in one minute": 7,
                "time": "Jun 29 14:44",
                "out of memory": false,
                "possibility": "Low"
            },
        ]
    }""",

    """1. source "biblioteka.wsi.edu.pl" made maximum "8" requests by "sshd login with empty logname" and all failed in "Jun 30 12:48", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is slightly lower than the baseline of 10 requests per minute, it is a potential network Dos attack with "Low" possibility
    2. source "60.30.224.116" made maximum "10" requests by "sshd login as root" and all failed in "Jun 30 19:03", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is just equal to the baseline of 10 requests per minute, it is a potential network Dos attack with "Medium" possibility
    3. source "195.129.24.210" made maximum "5" requests by "sshd login as root" and all failed in "Jun 30 20:16", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is slightly lower than the baseline of 10 requests per minute, it is a potential network Dos attack with "Medium" possibility
    4. source "163.27.187.39" made maximum "23" requests by "klogind" and all failed in "Jun 30 20:53", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is obviously higher than the baseline of 10 requests per minute, it is a potential network Dos attack with "High" possibility
    5. source "60.30.224.116" made maximum "10" requests by "sshd login as root" and all failed in "Jul  1 00:21", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is just equal to the baseline of 10 requests per minute, it is a potential network Dos attack with "Medium" possibility
    The Json result:
    {
        "Dos events": [
            {
                "source": "biblioteka.wsi.edu.pl",
                "behaviour": "sshd login with empty logname",
                "requests in one minute": 8,
                "time": "Jun 30 12:48",
                "out of memory": false,
                "possibility": "Low"
            },
            {
                "source": "60.30.224.116",
                "behaviour": "sshd login as root",
                "requests in one minute": 10,
                "time": "Jun 30 19:03",
                "out of memory": false,
                "possibility": "Medium"
            },
            {
                "source": "195.129.24.210",
                "behaviour": "sshd login as root",
                "requests in one minute": 10,
                "time": "Jun 30 20:16",
                "out of memory": false,
                "possibility": "Medium"
            },
            {
                "source": "60.30.224.116",
                "behaviour": "klogind",
                "requests in one minute": 10,
                "time": "Jul  1 00:21",
                "out of memory": false,
                "possibility": "Medium"
            },
        ]
    }""",

    """1. source "202.82.200.188" made maximum "22" requests by "ftpd connection" in "Jul  1 07:57", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is obviously higher than the baseline of 10 requests per minute, it is a potential network Dos attack with "High" possibility
    2. source "195.129.24.210" made maximum "10" requests by "sshd login as root" and all failed in "Jul  1 10:56", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is just equal to the baseline of 10 requests per minute, it is a potential network Dos attack with "Medium" possibility
    3. source "zummit.com" made maximum "10" requests by "sshd login with empty logname" and all failed in "Jul  2 04:15", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is just equal to the baseline of 10 requests per minute, it is a potential network Dos attack with "Medium" possibility
    4. source "203.101.45.59 (dsl-Chn-static-059.45.101.203.touchtelindia.net)" made maximum "21" requests by "ftpd connection" in "Jul  3 10:05", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is obviously higher than the baseline of 10 requests per minute, it is a potential network Dos attack with "High" possibility
    5. source "62.99.164.82 (62.99.164.82.sh.interxion.inode.at)" made maximum "22" requests by "ftpd connection" in "Jul  3 23:16", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is obviously higher than the baseline of 10 requests per minute, it is a potential network Dos attack with "High" possibility
    The Json result:
    {
        "Dos events": [
            {
                "source": "202.82.200.188",
                "behaviour": "ftpd connection",
                "requests in one minute": 22,
                "time": "Jul  1 07:57",
                "out of memory": false,
                "possibility": "High"
            },
            {
                "source": "195.129.24.210",
                "behaviour": "sshd login as root",
                "requests in one minute": 10,
                "time": "Jul  1 10:56",
                "out of memory": false,
                "possibility": "Medium"
            },
            {
                "source": "zummit.com",
                "behaviour": "sshd login with empty logname",
                "requests in one minute": 10,
                "time": "Jul  2 04:15",
                "out of memory": false,
                "possibility": "Medium"
            },
            {
                "source": "203.101.45.59 (dsl-Chn-static-059.45.101.203.touchtelindia.net)",
                "behaviour": "ftpd connection",
                "requests in one minute": 21,
                "time": "Jul  3 10:05",
                "out of memory": false,
                "possibility": "High"
            },
            {
                "source": "62.99.164.82 (62.99.164.82.sh.interxion.inode.at)",
                "behaviour": "ftpd connection",
                "requests in one minute": 22,
                "time": "Jul  3 23:16",
                "out of memory": false,
                "possibility": "High"
            },
        ]
    }""",

    """1. source "220.117.241.3" made maximum "9" requests by "sshd login with empty logname" in "Nov 17 04:29", the frequency of requests in one minute is slightly lower than the baseline of 10 requests per minute, but it subsequently caused frequent "Out of Memory" events, it is a potential network Dos attack with "High" possibility
    2. source "211.98.81.12" made maximum "16" requests by "sshd login as root" and all failed in "Nov 17 14:27", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is higer than the baseline of 10 requests per minute, it is a potential network Dos attack with "High" possibility
    3. source "211.98.81.12" made maximum "24" requests by "sshd login as root" and all failed in "Nov 17 14:28", although there were no subsequent "Out of Memory" events happened, the frequency of requests in one minute is obviously higer than the baseline of 10 requests per minute, it is a potential network Dos attack with "High" possibility
    4. source "211.98.81.12" made maximum "12" requests by "sshd login as root" and all failed in "Nov 17 14:29", the frequency of requests in one minute is slighly higer than the baseline of 10 requests per minute and it subsequently caused frequent "Out of Memory" events, it is a potential network Dos attack with "High" possibility
    5. source "211.157.108.173" made maximum "10" requests by "sshd login with empty logname" in "Nov 18 00:12", the frequency of requests in one minute is equal to the baseline of 10 requests per minute, and it subsequently caused frequent "Out of Memory" events, it is a potential network Dos attack with "High" possibility
    6. source "66.15.25.56 (bdsl.66.15.25.56.gte.net)" made maximum "18" requests by "ftp connection" in "Nov 18 09:13", the frequency of requests in one minute is higher than the baseline of 10 requests per minute, and it subsequently caused frequent "Out of Memory" events, it is a potential network Dos attack with "High" possibility
    The Json result:
    {
        "Dos events": [
            {
                "source": "220.117.241.3",
                "behaviour": "sshd login with empty logname",
                "requests in one minute": 9,
                "time": "Nov 17 04:29",
                "out of memory": true,
                "possibility": "High"
            },
            {
                "source": "211.98.81.12",
                "behaviour": "sshd login as root",
                "requests in one minute": 16,
                "time": "Nov 17 14:27",
                "out of memory": false,
                "possibility": "High"
            },
            {
                "source": "211.98.81.12",
                "behaviour": "sshd login as root",
                "requests in one minute": 24,
                "time": "Nov 17 14:28",
                "out of memory": false,
                "possibility": "High"
            },
            {
                "source": "211.98.81.12",
                "behaviour": "sshd login as root",
                "requests in one minute": 24,
                "time": "Nov 17 14:29",
                "out of memory": true,
                "possibility": "High"
            },
            {
                "source": "211.157.108.173",
                "behaviour": "sshd login with empty logname",
                "requests in one minute": 10,
                "time": "Nov 18 00:12",
                "out of memory": true,
                "possibility": "High"
            },
            {
                "source": "66.15.25.56 (bdsl.66.15.25.56.gte.net)",
                "behaviour": "ftpd connection",
                "requests in one minute": 18,
                "time": "Nov 18 09:13",
                "out of memory": true,
                "possibility": "High"
            },
        ]
    }""",
]