<?php
//检测可用字符

//检测可用字符
function is_preged($a){
    if (!preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', $a)){
        return true;
    }
}

//输出可用字符
for($a = 0; $a < 256; $a++){
    if (!is_preged(chr($a))){
        echo chr($a)." ";
    }
}

