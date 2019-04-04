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

