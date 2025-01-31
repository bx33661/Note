# HTB-Apponintment

---

![image-20250124163540870](https://gitee.com/bx33661/image/raw/master/path/image-20250124163540870.png)

基本的端口扫描：
![image-20250124163626647](https://gitee.com/bx33661/image/raw/master/path/image-20250124163626647.png)

> 1. What does the acronym SQL stand for?
>
> Structured Query Language
>
> 2. What is one of the most common type of SQL vulnerabilities?
>
> SQL Injection
>
> 3. What is the 2021 OWASP Top 10 classification for this vulnerability?
>
> A03:2021-Injection  （这个得自己搜一下）
>
> 4. What does Nmap report as the service and version that are running on port 80 of the target?
>
> Apache httpd 2.4.38 ((Debian))
>
> *nmap可以查出来 -sV*
>
> 5. What is the standard port used for the HTTPS protocol?
>
> 443
>
> 6. What is a folder called in web-application terminology?
>
> directory
>
> 7. What is the HTTP response code is given for 'Not Found' errors?
>
> 404
>
> 8. Gobuster is one tool used to brute force directories on a webserver. What switch do we use with Gobuster to specify we're looking to discover directories, and not subdomains?
>
> dir
>
> 9. What single character can be used to comment out the rest of a line in MySQL?
>
> #





登录页面SQL界面查询源码如下：

```php
<?php
// 连接到 MySQL 数据库
mysql_connect("localhost", "db_username", "db_password");

// 选择数据库
mysql_select_db("users");

// 获取用户输入的用户名和密码
$username = $_POST['username'];
$password = $_POST['password'];

// 构建 SQL 查询语句
$sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";

// 执行查询并将结果存储在 $result 中
$result = mysql_query($sql);

// 获取结果集中的行数
$count = mysql_num_rows($result);

// 检查是否有匹配的用户
if ($count == 1) {
    // 创建会话并存储用户名和密码
    $_SESSION['username'] = $username;
    $_SESSION['password'] = $password;

    // 重定向到主页
    header("location:home.php");
} else {
    // 登录失败，重定向回登录页面
    header("location:login.php");
}
?>
```

我们输入`admin'#`时候后面语句就不会执行，满足登录

进入页面拿到flag

![image-20250124165224999](https://gitee.com/bx33661/image/raw/master/path/image-20250124165224999.png)