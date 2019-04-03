# Level 11

URL : http://natas11.natas.labs.overthewire.org

## Solution

This is more like  a crypto challenge:

#### Let's examine the source code

```php
<?
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}

saveData($data);

?>

#### Source Code #2

```php

<?
if($data["showpassword"] == "yes") {
        print "The password for natas12 is <censored><br>";
    }
?>
```

- **we dont know the xor key**
- ** we need to change setpassword to yes**


---------------------
We will first recover the xor key. We have the base64 encoded cipher and we also have what was originally XORed with the key to get the cipher.

We can recover the key first.

```python
from base64 import b64decode, b64encode
b64_encoded = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV56QUcIaAw="
original = '{"showpassword":"no","bgcolor":"#ffffff"}' # this is the result on using php's json_encode(array) on the original array in source code 

key_ = ""

for i, j in zip(original.encode(), b64decode(b64_encoded)):
    key_ += chr(i ^ j)

print(key_)
# key_ = qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8..
# which means key = qw8J
```


#### Let's get the password!

we will xor_encrypt() our own cookie to get the password

we need to encrypt this : **{"showpassword":"yes","bgcolor":"#ffffff"}**, since we need showpassword to be equal to yes!

```python
from base64 import b64encode
c = '{"showpassword":"yes","bgcolor":"#ffffff"}'
key = "qw8J"

res = ""
for i in range(len(c)):
    res += chr(ord(c[i]) ^ ord(key[i % 4])) # 4 = len(key)

print(b64encode(key.encode()))

```



