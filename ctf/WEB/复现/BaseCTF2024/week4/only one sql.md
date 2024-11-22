### only one sql

---

> 时间注入

```php
<?php
highlight_file(__FILE__);
$sql = $_GET['sql'];
if (preg_match('/select|;|@|\n/i', $sql)) {
    die("你知道的，不可能有sql注入");
}
if (preg_match('/"|\$|`|\\\\/i', $sql)) {
    die("你知道的，不可能有RCE");
}
//flag in ctf.flag
$query = "mysql -u root -p123456 -e \"use ctf;select '没有select，让你执行一句又如何';" . $sql . "\"";
system($query); 
```

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYngifQ.1l0XFabWmjILdOSs72jx-bmYdRJRGXPnNs0H2Gu3qAQ