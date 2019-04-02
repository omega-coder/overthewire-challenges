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
