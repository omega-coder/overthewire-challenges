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

We can see that both the username and password are injectable.  
Let's try to play a little with the query.  

let's enter test as the `username` and test as `password`, then the query will look like this : 

```sql
SELECT * from users where username="test" and password="test"
```

Now let's try :
- **username:"test**
- **password:"test**

Then our query would look like this:

```sql
SELECT * from users where username=""test" and password=""test"   
```

Now we can do this : username = **" or 1=1#**, this will be equivalent to

```sql
SELECT * FROM users where 1
```

`NOTE: # is used for commenting is SQL.`

We can use the payload `" or 1=1#` in both username or password, they are both injectable.

This challenge is a simple Authentification Bypass.


























