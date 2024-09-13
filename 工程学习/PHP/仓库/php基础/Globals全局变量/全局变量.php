<?php
$x = 5201314;
function ex()
{
    echo $GLOBALS['x'];
}

function abc()
{
    $GLOBALS['bx'] = "bx333661";
}
//必须执行一下abc（）函数，否则无法输出$bx
abc();
echo $bx;
