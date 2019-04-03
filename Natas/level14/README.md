# Level 14


URL : http://natas14.natas.labs.overthewire.org/

### Creds for level 14
natas14:Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1

## Introduction
We will be doing some `basic SQL injection` in this writeup. You may want to read on [SQL](https://en.wikipedia.org/wiki/SQL)

## Solution

we are given a simple form with two inputs **username** and **password**.

Let's review the source code and spot the vulnerability.

```php
<?
if(array_key_exists("username", $_REQUEST)) {
    $link = mysql_connect('localhost', 'natas14', '<censored>');
    mysql_select_db('natas14', $link);
    
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    if(mysql_num_rows(mysql_query($query, $link)) > 0) {
            echo "Successful login! The password for natas15 is <censored><br>";
    } else {
            echo "Access denied!<br>";
    }
    mysql_close($link);
} else {
?> 
```
















