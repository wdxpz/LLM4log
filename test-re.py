import re

# text = '''这里是文本，其中包含URL和IP地址，例如：http://www.example.com和 86.193.48.194。
# Jul 18 03:26:49 combo ftpd[25648]: connection from 211.72.151.162 () at Mon Jul 18 03:26:49 2005
# ruser= rhost=mail.xmjl.com  user=root
# ruser= rhost=212-41-230-229.hebragasse.xdsl-line.inode.at
# ruser= rhost=pppzss.shenzhen.gd.cn
# ruser= rhost=wsip-24-120-168-221.lv.lv.cox.net
# '''

text = '''62.99.164.82.sh.interxion.inode.at'''

# 正则表达式用于匹配URL
url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
urls = re.findall(url_pattern, text)

rhost_pattern = r'([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
# rhost_pattern = r'([a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|[0-9-]+(?:\.[0-9]+){3})'
rhost = re.findall(rhost_pattern, text)

# 正则表达式用于匹配IPv4地址
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
ips = re.findall(ip_pattern, text)

print("URLs:", urls)
print("IPs:", ips)
print("RHOST:", rhost)



ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
for i in llm_url_list:
    if re.match(ip_pattern, i):
        ip_in_url.append(i)