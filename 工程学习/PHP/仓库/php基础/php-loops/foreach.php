<?php
$array = array("red","blue","yellow");
//循环遍历数组
foreach ($array as $i){
    echo $i."<br>";
}

// 涉及键值对
$members = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");

foreach ($members as $x => $y) {
    echo "$x : $y <br>";
}

//循环对象的属性
class Car {
    public $color;
    public $model;
    public function __construct($color, $model) {
        $this->color = $color;
        $this->model = $model;
    }
}

$myCar = new Car("red", "Volvo");

foreach ($myCar as $x => $y) {
    echo "$x: $y <br>";
}