<?php
highlight_file(__FILE__); 
error_reporting(0); 
class demo{ 
    public $serial_number; 
    public function say_hello(){
        echo "hello!!";
    }
    public function __construct($num) {
        $this->serial_number = $num; 
        echo $this->serial_number."构造函数启用"."</br>"; 
    }
    public function __destruct(){
        echo $this->serial_number."析构函数启用"."</br>"; 
    }
    }
$a = new demo(1); 
$b = new demo(2); 
unset($b);
$c = new demo(3);
