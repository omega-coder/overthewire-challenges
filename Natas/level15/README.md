# Level 15

URL : http://natas15.natas.labs.overthewire.org/index.php

## solution

here is the source code for this level:

```php
<?

/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysql_connect('localhost', 'natas15', '<censored>');
    mysql_select_db('natas15', $link);
    
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysql_query($query, $link);
    if($res) {
    if(mysql_num_rows($res) > 0) {
        echo "This user exists.<br>";
    } else {
        echo "This user doesn't exist.<br>";
    }
    } else {
        echo "Error in query.<br>";
    }

    mysql_close($link);
} else {
?> 
```

In this level we will be dealing with a Blind-based SQL injection (`a Boolean based one`).  
After inspecting the source code, we can see that no real data from DB is sent to us after query execution, but we only see three (3) possible responses.  
1. This user exists.
2. This user doesn't exist.
3. Error in query.

----------------------
### Password retrieval method 

1. get password length first

According to previous challenges, length for all passwords is 32 chars.We can verify this by injecting in username field the following payload.
I have already explained injection method in the previous writeup.
```sql
natas16" and length(password) = 32#
```
if the output is "This user exists.", then password length is indeed 32, else it is not (I know it is 32 )

To retrieve the password, we can use `LIKE` or `strcmp()` function of MySql.

Let's try something.

username: **natas16" and strcmp(BINARY substr(password, 1, 1), "W") = 0#**

If after the previous injection we get the output saying `This user exists.`, then we know that the first character of the password is indeed `W`.

- substr(password, 1, 1) gets the first character of the password column.
- strcmp(str1, str2) compares the strings `str1` and `str2`, returns the distance between the two operands.
- **BINARY** is used for case-sensitivity.


### Exploitation











