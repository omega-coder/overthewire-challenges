# Level 8

URL : http://natas8.natas.labs.overthewire.org/


## Solution

let's see the source code first.

```php
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
        print "Access granted. The password for natas9 is <censored>";
    } else {
        print "Wrong secret";
    }
}

?>

```

so, basically, we need to satisfy this : encodeSecret(OUR_STRING) == encodedSecret;
since all functions used to encode are reversible, we only have to reapply them in reverse order thats all.

You can do it using a php interpreter **php -a**


```php
$encodedSecret = "3d3d516343746d4d6d6c315669563362";
$pass = base64_decode(strrev(hex2bin(encodedSecret))); 
echo $pass;
```

Now submit the password, and you will get the password for natas9



