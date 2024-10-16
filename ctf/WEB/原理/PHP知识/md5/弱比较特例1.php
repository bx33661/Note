<?php
show_source(__FILE__);
error_reporting(0);
$first = $_GET["first"];
$second = $_GET["second"];

if(is_array($first) || is_array($second)){
    die("No Array !!!");
}else if ($first !== $second && md5($first) === md5($second)){
    print("You are Right");
}else {
    die("ohhh no~");
}