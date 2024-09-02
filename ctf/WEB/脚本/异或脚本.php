<?php
$myfile = fopen("text.txt", "w");  //新创建一个文件，也就是rce_or.txt，给他写的权限
$contents="";
for ($i=0; $i < 256; $i++) { 
	for ($j=0; $j <256 ; $j++) { 

		if($i<16){
			$hex_i='0'.dechex($i); //ascii的前16个字符的十六进制应该是01，02，所以在前缀加‘0’
		}
		else{
			$hex_i=dechex($i);  //前16个后面的就不用加0了
		}
		if($j<16){
			$hex_j='0'.dechex($j);   //同理上方
		}
		else{
			$hex_j=dechex($j);      //同理上方
		}
		$preg ='/[a-z]|[0-9]|\+|\-|\.|\_|\||\$|\{|\}|\~|\%|\&|\;/i';
		if(preg_match($preg , hex2bin($hex_i))||preg_match($preg , hex2bin($hex_j))){
					echo "";     //如果有符合条件的就筛掉，输出空格
    }
  
		else{             //可以使用的字符如下
		$a='%'.$hex_i;    //十六进制前加百分号就变成了URL编码格式
		$b='%'.$hex_j;
		$c=(urldecode($a)^urldecode($b));  //urldecode函数是解URL编码，把他们变成字符串，这里是字符串进行按位或运算，按位或运算后，可以得到新的字符，如%21和%00进行按位或就变成了!,这样我们就可以使用感叹号,就类似于合成新的字符
		if (ord($c)>=32&ord($c)<=126) {          //ord函数是将字符变成ASCII码
			$contents=$contents.$c." ".$a." ".$b."\n";     //每次到这里都写入刚刚建立的文本内
		}
	}

}
}
fwrite($myfile,$contents);
fclose($myfile);
?>