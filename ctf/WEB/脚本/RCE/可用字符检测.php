<?php
//检测可用字符

//检测可用字符
function is_preged($a){
    if (preg_match('/\&|\/|\?|\*|\<|[\x{00}-\x{20}]|\>|\'|\"|\\|\(|\)|\[|\]|\{|\}/', $a)){
        return true;
    }
}

//输出可用字符
for($a = 0; $a < 256; $a++){
    if (!is_preged(chr($a))){
        echo chr($a)." ";
    }
}

