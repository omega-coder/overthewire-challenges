# Level 6

URL : http://natas6.natas.labs.overthewire.org/

### Creds for level 6
**natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1**

## Solution

![natas6_homepage](https://res.cloudinary.com/https-omega-coder-github-io/image/upload/v1554241584/Screenshot_2019-04-02_23-43-15.png)


we obviously need to see the source code, we are only interested by this portion of the code.

```php
<?

include "includes/secret.inc";

if(array_key_exists("submit", $_POST)) {
    if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
}

?>

```

lets see what's inside of **includes/secret.inc**

`Ctrl+u`, and we can see the secret $secret=FOEIUWGHFEEUHOFUOIU.

let's submit the secret and get creds for level7







