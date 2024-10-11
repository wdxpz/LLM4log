from typing import List

from pydantic import BaseModel


class Extract(BaseModel):
    IP: list[str]
    URL: list[str]
    memory: list[str]

l = Extract(IP=['192.168.1.1', '192.168.1.2'], URL=['http://www.example.com', 'http://www.example.org'], memory=['100', '200'])
print(l.IP)
