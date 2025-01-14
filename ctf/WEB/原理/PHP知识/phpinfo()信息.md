# phpinfo()信息

---



### **2.系统的版本信息**

系统无非是两种 Linux 和 Windows ，这在我们后期命令执行的时候或者是 bypass disable_function 的时候有用

[![此处输入图片的描述](https://gitee.com/bx33661/image/raw/master/path/PHPINFO3.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO3.png)
[![此处输入图片的描述](https://gitee.com/bx33661/image/raw/master/path/PHPINFO4.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO4.png)

### **3.Configure Command(编译命令)**

这个其实就是编译 php 的时候的命令,这里面其实包含了几乎所有的， php 要加载的扩展和功能，但是看起来不是很方便(因为比较乱),但也是一目了然，当然这些功能在后面都有专门的栏目介绍。

[![此处输入图片的描述](https://gitee.com/bx33661/image/raw/master/path/PHPINFO5.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO5.png)

### **4.Loaded Configuration File(配置文件位置)**

这一栏表明了 php.ini 这个 php 配置文件的位置，在有文件读取的情况下可以进行读取，在渗透中还是很有帮助的。

[![此处输入图片的描述](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO6.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO6.png)

同时在windows中

![image-20250113183556769](https://gitee.com/bx33661/image/raw/master/path/image-20250113183556769.png)

### **5.Registered PHP Streams(支持的流)**

这个在文件包含、反序列化还有一些关键的 bypass 的时候非常有用

[![此处输入图片的描述](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO7.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO7.png)

### **6.Registered Stream Filters(支持的流过滤器)**

这个同样在文件包含、反序列化还有一些关键的 bypass 的时候非常有用

[![此处输入图片的描述](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO8.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO8.png)此处输入图片的描述

### **7.Core(核心)**

这个栏目里面有非常多重要的配置信息，我们可以简单的看一下：

#### **(1)allow_url_fopen&allow_url_include**

文件包含必看选项之一

[![此处输入图片的描述](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO9.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO9.png)

#### **(2)disable_functions**

命令执行、代码执行必看选项之一，具体可以看我的[这篇文章](https://www.k0rz3n.com/2019/02/12/PHP 中可以利用的危险的函数/)

[![此处输入图片的描述](https://gitee.com/bx33661/image/raw/master/path/PHPINFO10.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO10.png)

#### **(3)错误提示**

调试过程中经常使用的错误提示在没有关闭的情况下放入生产环境是不堪设想的

[![此处输入图片的描述](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO11.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO11.png)此处输入图片的描述

#### **(4)enable_dl**

该选项**默认为 on(在未来将被移除)** ，我们看一下 官方手册怎么说的

> 该指令仅对 Apache 模块版本的 PHP 有效。 你可以针对每个虚拟机或每个目录开启或关闭 dl() 动态加载 PHP 模块。
>
> 关闭动态加载的主要原因是为了安全。通过动态加载，有可能忽略所有 open_basedir 限制。 默认允许动态加载，除了使用 安全模式。在安全模式，总是无法使用 dl()。

[![此处输入图片的描述](https://gitee.com/bx33661/image/raw/master/path/PHPINFO14.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO14.png)

#### **(5)extension_dir**

和 dl() 配合使用效果更好，具体可以看[这篇文章](https://www.k0rz3n.com/2019/02/12/PHP 中可以利用的危险的函数/)

[![此处输入图片的描述](https://gitee.com/bx33661/image/raw/master/path/PHPINFO13.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO13.png)

#### **(6)include_path**

PHP 用include()函数包函文件时的默认路径

[![此处输入图片的描述](https://gitee.com/bx33661/image/raw/master/path/PHPINFO12.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO12.png)

#### **(7)open_basedir**

这个选项设置了文件读取的时候的目录限制

[![此处输入图片的描述](https://gitee.com/bx33661/image/raw/master/path/PHPINFO15.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO15.png)

#### **(8)short_open_tag**

判断服务器是不是支持短标签，这在写 shell 的时候很有帮助

[![此处输入图片的描述](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO19.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO19.png)

### **8.phar**

文件包含还有反序列化重点关注

[![此处输入图片的描述](https://gitee.com/bx33661/image/raw/master/path/PHPINFO16.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO16.png)此处输入图片的描述

### **9.SESSION**

session.save_path=”” –设置session的存储路径
session.save_handler=”” –设定用户自定义存储函数，如果想使用PHP内置会话存储机制之外的可以使用本函数(数据库等方式)
session.auto_start boolen –指定会话模块是否在请求开始时启动一个会话,默认为0不启动
session.serialize_handler string –定义用来序列化/反序列化的处理器名字。默认使用php

**例如：**

```
session.save_path="D:\xampp\tmp"表明所有的session文件都是存储在xampp/tmp下
session.save_handler=files    表明session是以文件的方式来进行存储的
session.auto_start=0表明默认不启动session
session.serialize_handler=php    表明session的默认序列话引擎使用的是php序列话引擎
```

这几个选项在文件包含的时候以及反序列化的时候非常的有用，具体可以参考一下 [LCTF2018 的一道题](https://www.k0rz3n.com/2018/11/21/LCTF 2018 部分 web 题 writeup/5.png) 以及我之前的[这篇文章](https://www.k0rz3n.com/2018/11/20/一篇文章带你理解漏洞之 PHP 文件包含漏洞/)

### **10.PHP Variables**

#### **(1)_SERVER[‘PATH’]**

这个是 windows 下特有的，能显示出系统的所有环境变量

#### **(2)_SERVER[“SCRIPT_FILENAME”]**

这个是最常用，也是最有效的一个办法，找到phpinfo()页面可以直接找到网站的绝对路径，对于写shell和信息搜集是必不可少的。

[![此处输入图片的描述](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO17.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO17.png)此处输入图片的描述
[![此处输入图片的描述](https://gitee.com/bx33661/image/raw/master/path/PHPINFO18.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/PHPINFO18.png)此处输入图片的描述

#### **(3)_SERVER[“SERVER_ADDR”]**

显示该网站的真实的 ip 地址，有时候通过phpinfo()泄漏的ip可以查查旁站、c段什么的，直接无视cdn。

#### **(4)_FILES[“filename”]**

在给PHP发送POST数据包时，如果数据包里包含文件区块，无论你访问的代码中有没有处理文件上传的逻辑，PHP都会将这个文件保存成一个临时文件（通常是/tmp/php[6个随机字符]），文件名可以在$_FILES变量中找到。这个临时文件，在请求结束后就会被删除。

这是常用的配合文件包含 get,shell 的方式，具体可见[这篇文章](https://www.k0rz3n.com/2018/11/20/一篇文章带你理解漏洞之 PHP 文件包含漏洞/)

### **11.gopher**

可以配合 SSRF 发起攻击

### **12.fastcgi**

查看是否开启fastcgi和fastcgi的版本，可能导致解析漏洞、远程命令执行、任意文件读取等问题

### **13.支持的程序**

可以通过phpinfo()查看一些特殊的程序服务，比如redis、memcache、mysql、SMTP、curl等等如果服务器装了redis或者memcache可以通过ssrf来getshell了，在discuz中都出现过此类问题。如果确定装了redis或memcache的话，在没有思路的情况下，可以着重找一下ssrf

## **0X02 PHPINFO 中要解释的信息**

### **1.Thread Safety**

这个信息有点意思，我们一般看到的都是 disable ，但是这不代表不安全，因此这个选项严格的讲并不叫“线程安全”,应该叫 “线程安全检查”。

> None Thread Safe就是非线程安全，在执行时不进行线程（thread）安全检查。
>
> Thread Safe就是线程安全，执行时会进行线程（thread）安全检查，以防止有新要求就启动新线程，耗尽系统资源。

再看看这两者的选择。

为了与外部交换数据，PHP提供了一种叫SAPI的接口。

SAPI是一个中间过程，提供了一个和外部通信的接口，有点类似于socket。

SAPI使得PHP可以和其他应用进行交互数据（如Apache、Nginx等）。

PHP默认提供了很多种SAPI，常见的提供给Apache、Nginx、IIS6/7的FastCGI，单独给IIS的ISAPI，以及Shell的CLI。

FastCGI执行方式是以单一线程来执行操作，所以不需要进行线程的安全检查，除去线程安全检查的防护反而可以提高执行效率。

而线程安全检查是为ISAPI方式的PHP准备的，也就是为IIS准备的，因为有许多php模块都不是线程安全的，所以需要使用Thread Safe的PHP。

所以，如果是以 FastCGI 执行 PHP ，都建议用Non Thread Safe的 PHP （zip安装包）。

### **2.expose_php**

这个选项开启将会在 http 包的头部显示 php 的版本等信息，是一种信息泄露，建议关闭