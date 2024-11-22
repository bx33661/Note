### Content-Type

> 起因最近做题的时候post传参数的时候，需要传一个json数据，但是无论如何都不对，最后检查发现是这个POST的`enctype`不对

- `application/x-www-form-urlencoded`

- `multipart/form-data`

- `text/plain`

- `application/json`

就是我们利用bp，hackbar也好，传post参数的时候都需要在HTTP头设置一个`Content-Type`



----

*就借助 deepseek总结一下*： 

#### `application/x-www-form-urlencoded`

这个是我们最常见的

> 这是默认的编码类型。在这种编码方式下，表单数据会被编码为键值对，键和值之间用 `=` 连接，不同的键值对之间用 `&` 连接。编码后的数据会被 URL 编码（即特殊字符会被转换为 `%HH` 格式，空格会被转换为 `+`）。

平时传参数基本全用的它，看介绍就是键值对的形式，被url编码，传递

```
a=hello&b=world
```

一个例子

前端html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
</head>
<body>
    <form method="post" action="submit.php" enctype="application/x-www-form-urlencoded">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>

```

后端php：

```php
<?php
// 检查是否有 POST 请求
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // 获取表单数据
    $username = $_POST['username'];
    $password = $_POST['password'];

    // 输出接收到的数据
    echo "Username: " . htmlspecialchars($username) . "<br>";
    echo "Password: " . htmlspecialchars($password) . "<br>";

    // 在这里可以添加更多的逻辑，例如验证用户名和密码、将数据存储到数据库等
} else {
    // 如果不是 POST 请求，显示错误信息
    echo "Invalid request method.";
}
?>
```

---



#### `multipart/form-data`

> 这种编码类型用于上传文件。在这种编码方式下，表单数据会被分割成多个部分，每个部分对应一个表单字段。每个部分都有自己的头信息，包括字段名、文件名（如果是文件）、内容类型等。

在做文件上传类型题的时候，我们抓包会发现这种形式的数据

前端html代码：

```html
<form method="post" action="upload.php" enctype="multipart/form-data">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="profile_picture">Profile Picture:</label>
        <input type="file" id="profile_picture" name="profile_picture" required>
        <br>
        <input type="submit" value="Submit">
    </form>
```

后端php：

```php
<?php
// 检查是否有 POST 请求
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // 获取表单数据
    $username = $_POST['username'];

    // 检查文件上传是否成功
    if (isset($_FILES['profile_picture']) && $_FILES['profile_picture']['error'] === UPLOAD_ERR_OK) {
        $fileTmpPath = $_FILES['profile_picture']['tmp_name'];
        $fileName = $_FILES['profile_picture']['name'];
        $fileSize = $_FILES['profile_picture']['size'];
        $fileType = $_FILES['profile_picture']['type'];

        // 设置上传目录
        $uploadDir = './uploads/';
        if (!is_dir($uploadDir)) {
            mkdir($uploadDir, 0777, true);
        }

        // 生成唯一的文件名
        $fileNameCmps = explode(".", $fileName);
        $fileExtension = strtolower(end($fileNameCmps));
        $newFileName = md5(time() . $fileName) . '.' . $fileExtension;

        // 移动文件到上传目录
        $destFilePath = $uploadDir . $newFileName;
        if (move_uploaded_file($fileTmpPath, $destFilePath)) {
            echo "Username: " . htmlspecialchars($username) . "<br>";
            echo "File uploaded successfully: " . htmlspecialchars($newFileName) . "<br>";
        } else {
            echo "File upload failed.";
        }
    } else {
        echo "File upload error.";
    }
} else {
    // 如果不是 POST 请求，显示错误信息
    echo "Invalid request method.";
}
?>
```

提交之后数据格式如下：

```html
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="username"

John Doe
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="profile_picture"; filename="profile.jpg"
Content-Type: image/jpeg

[binary data]
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```



---

#### `application/json`

> `application/json` 是一种用于表示 JSON 格式数据的 MIME 类型。JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，易于人阅读和编写，同时也易于机器解析和生成。

在原链题里面遇到过一次

- **`application/json`**：用于表示 JSON 格式的数据，适用于复杂的结构化数据传输。
- **使用场景**：API 请求、配置文件、日志记录等。
- **客户端处理**：使用 `fetch` 或 `XMLHttpRequest` 发送 JSON 数据，设置 `Content-Type` 为 `application/json`。
- **服务器端处理**：使用相应的中间件（如 Express 的 `express.json()`）解析 JSON 请求体。



就说传json格式的数据的时候使用这个

----

#### `text/plain`

> 这种编码类型会将表单数据以纯文本的形式发送，键和值之间用 `=` 连接，但不会对特殊字符进行 URL 编码。

就是第一个类型，不进行url编码，服务端不给你处理了