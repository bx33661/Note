<?php
show_source(__FILE__);
error_reporting(0);

$first = $_GET['one'];
$second = $_GET['two'];
if($first != $second){
    if(md5($first) === md5($second)){
        echo "!!!!success!!!";
    }else{
        echo '强比较MD5--error！！';
    }
}else{
    echo '两个量不能相等！！';
}
