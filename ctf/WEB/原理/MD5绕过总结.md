# MD5绕过总结

[TOC]

```toc
```
---

PHP中`md5函数`语法：

```php
md5(string,raw)
```

| 参数   | 描述                                                         |
| :----- | ------------------------------------------------------------ |
| string | 必需。要计算的字符串。                                       |
| raw    | 可选。默认不写为FALSE：32位16进制的字符串。TRUE：16位原始二进制格式的字符串 |



一个python的md5加密脚本：

```python
import hashlib
def md5_encode(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))
    md5_digest = md5_hash.hexdigest()
    return md5_digest

# md5(cookie_secret+md5(filename))
data = "8e0ec61c-e16c-4ed2-a4ca-f51cd96f3efe"
md5_encoded = md5_encode(data)

print(f"原始数据: {data}")
print(f"MD5 编码: {md5_encoded}")
```

## 基本方法

### `==`弱比较类型
**弱比较的概念：**
```php
var_dump("123a"==123);
var_dump("123a"=="123");
var_dump("a123"==0);
//bool(true)
//bool(false)
//bool(true)
```

#### 方法一 0e绕过
```php
<?php 
$v1 = $_GET['v1'];
$v2 = $_GET['v2'];

if (isset($v1) and isset($v2)) {
    if ($v1 != $v2 and md5($v1) == md5($v2)) {
        die("success!");
    }
}
show_source(__FILE__);
?>
```

审计过后得知，需要满足`v1`不等于`v2`，同时两个变量的md5值相同

由于这里使用的是 `==` 故而可能存在弱类型转换，假设 `$v1` 进行 md5 加密之后得到：`0e*************`，`$v2` 进行 md5 加密之后得到：`0e*************` 。

那么经过 `==` 比较，两者是相等的，因为 PHP 会将其看做是科学计数法。0 的任何次方都得 0，故而就是 `0` == `0`



列举一些例子：MD5 0e payload
```bash
$md5 						md5($md5)
s878926199a					0e545993274517709034328855841020
s155964671a					0e342768416822451524974117254469
s214587387a					0e848240448830537924465865611904
s214587387a					0e848240448830537924465865611904
s878926199a					0e545993274517709034328855841020
s1091221200a				0e940624217856561557816327384675
s1885207154a				0e509367213418206700842008763514
s1502113478a				0e861580163291561247404381396064
s1885207154a				0e509367213418206700842008763514
s1836677006a				0e481036490867661113260034900752
s155964671a					0e342768416822451524974117254469
s1184209335a				0e072485820392773389523109082030
s1665632922a				0e731198061491163073197128363787
s1502113478a				0e861580163291561247404381396064
s1836677006a				0e481036490867661113260034900752
s1091221200a				0e940624217856561557816327384675
s155964671a					0e342768416822451524974117254469
s1502113478a				0e861580163291561247404381396064
s155964671a					0e342768416822451524974117254469
s1665632922a				0e731198061491163073197128363787
s155964671a					0e342768416822451524974117254469
s1091221200a				0e940624217856561557816327384675
s1836677006a				0e481036490867661113260034900752
s1885207154a				0e509367213418206700842008763514
s532378020a					0e220463095855511507588041205815
s878926199a					0e545993274517709034328855841020
s1091221200a				0e940624217856561557816327384675
s214587387a					0e848240448830537924465865611904
s1502113478a				0e861580163291561247404381396064
s1091221200a				0e940624217856561557816327384675
s1665632922a				0e731198061491163073197128363787
s1885207154a				0e509367213418206700842008763514
s1836677006a				0e481036490867661113260034900752
s1665632922a				0e731198061491163073197128363787
s878926199a					0e545993274517709034328855841020
QNKCDZO						0e830400451993494058024219903391
```

SHA1 --0e--payload：
```txt
aaroZmOk
aaK1STfY
aaO8zKZF
aa3OFF9m
0e1290633704
10932435112
```

#### 方法二 ---数组绕过

```http
v1[]= 1&v2[]= 2
```

> md5()或者sha1()之类的函数计算的是一个字符串的哈希值，对于数组则返回false，如果`$str1`和`$str2`都是数组则双双返回FALSE, 两个FALSE相等得以绕过



#### 一些特例--md5碰撞

最典型的例子：强制类型转换

我们只能寻求两个内容不一样，但是md5值一样的文件

```php
<?php
if ((string)$_POST['param1'] !== (string)$_POST['param2'] && md5($_POST['param1']) === md5($_POST['param2'])) {
    die("success!");
}
?>

```

Payload：

```
first=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%00%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%55%5d%83%60%fb%5f%07%fe%a2
&second=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%02%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%d5%5d%83%60%fb%5f%07%fe%a2
```



ban了很多方法，那我们也可以使用md5碰撞的结果：

```php
<?php
show_source(__FILE__);
error_reporting(0);
$first = $_GET["first"];
$second = $_GET["second"];

if(is_array($first) || is_array($second)){
    die("No Array !!!");
}else if ($first !== $second && md5($first) === md5($second)){
    print("You are Right");
}else {
    die("ohhh no~");
}
```

Payload:

```
first=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%00%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%55%5d%83%60%fb%5f%07%fe%a2
&second=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%02%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%d5%5d%83%60%fb%5f%07%fe%a2
```

![image-20241016225215443](https://gitee.com/bx33661/image/raw/master/path/image-20241016225215443.png)





### `===`强比较类型

```php
<?php
var_dump("123a" === 123);  // bool(false)
var_dump("123a" === "123");  // bool(false)
var_dump("a123" === 0);  // bool(false)
```

弱比较（`==`）和强比较（`===`）的区别在于，弱比较会进行类型转换，而强比较不会。

>  `===` 强等于，先比较其数据类型再比较其值，不会进行类型转换。故而例题 - 1 的做法，在这里就不生效了。

```php
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

```

直接采用传入数组的方式，让两个量都等于`null`





### `$a` 等于 `md5($a)` 类型

md5值等于自身的形式，利用角度就是0e绕过，我们寻求一些特征如下的形式：

- 0e开头的
- md5后也是0e开头

满足上述内容的---Payload如下：

```php
<?php
$strings = [
    "0e215962017",
    "0e1284838308",
    "0e1137126905",
    "0e807097110",
    "0e730083352"
];

foreach ($strings as $string) {
    $md5_hash = md5($string);
    echo "MD5 hash of '$string' is: $md5_hash\n";
}
?>
```

输出结果

```php
MD5 hash of '0e215962017' is: 0e291242476940776845150308577824
MD5 hash of '0e1284838308' is: 0e708279691820928818722257405159
MD5 hash of '0e1137126905' is: 0e291659922323405260514745084877
MD5 hash of '0e807097110' is: 0e318093639164485566453180786895
MD5 hash of '0e730083352' is: 0e870635875304277170259950255928
----
0e215962017 0e291242476940776845150308577824
0e1284838308 0e708279691820928818722257405159
0e1137126905 0e291659922323405260514745084877
0e807097110 0e318093639164485566453180786895
0e730083352 0e870635875304277170259950255928
```



### MD5长度扩展攻击

---

> 使用工具：https://github.com/luoingly/attack-scripts/blob/main/logic/md5-extension-attack.py

一道最近做的题，

```php
// 你以为这就结束了
if (!isset($_SESSION['random'])) {
    $_SESSION['random'] = bin2hex(random_bytes(16)) . bin2hex(random_bytes(16)) . bin2hex(random_bytes(16));
}

// 你想看到 random 的值吗?
// 你不是很懂 MD5 吗? 那我就告诉你他的 MD5 吧
$random = $_SESSION['random'];
echo md5($random);
echo '<br />';

$name = $_POST['name'] ?? 'user';

// check if name ends with 'admin'
if (substr($name, -5) !== 'admin') {
    die('不是管理员也来凑热闹?');
}

$md5 = $_POST['md5'];
if (md5($random . $name) !== $md5) {
    die('伪造? NO NO NO!');
}
```



我们可以观察到：

`$name`可控

`md(random)` 值已经知道了

变量`$_SESSION['random']` 的长度我们知道

因为知道了第一个字符串`$_SESSION['random']`的长度，我们可以构造第二个字符串`$random . $name`的值，也就是说我们手动在第二个字符串`$random . $name`的前端添加一些特定数据，使得第一轮计算因为我们添加数据后符合一轮计算的原数据长度而只计算出第一个字符串的hash值。这样我们就可以利用这个结果作为我们二轮计算的幻数进行下面的计算，从而预测最终的md结果。


例如，我们得到的md值：2580094662738492023445e5fdb0e1ed，我们的目的是添加一系列数据（最后五个字符是admin），使得加上random之后的md5与第一次md5值一样

> 关于这个变量`$_SESSION['random']` 的长度的计算：
> 1byte = 8 个字节
> 16byte=128个字节
> 4个二进制数等于一个16进制数
> 128/4*3=96

```python
[>] Input known text length: 96
[>] Input known hash: 2580094662738492023445e5fdb0e1ed
[>] Input append text: admin
[*] Attacking...
[+] Extend text: b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00admin'
[+] Extend text (URL encoded): %80%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%03%00%00%00%00%00%00admin
[+] Extend text (Base64): gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAABhZG1pbg==
[+] Final hash: 735f29b2def96d4978625c18ddc4fcae
```

这样`md5($random . $name)`加密之后的值也就等于`735f29b2def96d4978625c18ddc4fcae`

> 这样就实现了可以添加我们想要的内容去上面然后，满足题目的md5检测



md5算法--填充消息步骤：

MD5算法的第一步是对输入消息进行填充，使其长度满足一定的条件。具体步骤如下：

- **填充比特**：首先，在消息的末尾添加一个“1”比特。然后，在“1”比特之后添加若干个“0”比特，直到消息的长度满足以下条件：填充后的消息长度模512等于448。
- **附加长度**：在填充后的消息末尾附加一个64位的二进制数，表示原始消息的长度（以比特为单位）。如果原始消息的长度超过64位所能表示的范围，则只取其低64位。

填充和附加长度后，消息的总长度将是512的倍数。



#### md5_extension_attack脚本

```Python
from struct import pack, unpack
from math import floor, sin

class MD5:

    def __init__(self):
        self.A, self.B, self.C, self.D = \
            (0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476)  # initial values
        self.r: list[int] = \
            [7, 12, 17, 22] * 4 + [5,  9, 14, 20] * 4 + \
            [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4  # shift values
        self.k: list[int] = \
            [floor(abs(sin(i + 1)) * pow(2, 32))
             for i in range(64)]  # constants

    def _lrot(self, x: int, n: int) -> int:
        # left rotate
        return (x << n) | (x >> 32 - n)

    def update(self, chunk: bytes) -> None:
        # update the hash for a chunk of data (64 bytes)
        w = list(unpack('<'+'I'*16, chunk))
        a, b, c, d = self.A, self.B, self.C, self.D

        for i in range(64):
            if i < 16:
                f = (b & c) | ((~b) & d)
                flag = i
            elif i < 32:
                f = (b & d) | (c & (~d))
                flag = (5 * i + 1) % 16
            elif i < 48:
                f = (b ^ c ^ d)
                flag = (3 * i + 5) % 16
            else:
                f = c ^ (b | (~d))
                flag = (7 * i) % 16

            tmp = b + \
                self._lrot((a + f + self.k[i] + w[flag])
                           & 0xffffffff, self.r[i])
            a, b, c, d = d, tmp & 0xffffffff, b, c

        self.A = (self.A + a) & 0xffffffff
        self.B = (self.B + b) & 0xffffffff
        self.C = (self.C + c) & 0xffffffff
        self.D = (self.D + d) & 0xffffffff

    def extend(self, msg: bytes) -> None:
        # extend the hash with a new message (padded)
        assert len(msg) % 64 == 0
        for i in range(0, len(msg), 64):
            self.update(msg[i:i + 64])

    def padding(self, msg: bytes) -> bytes:
        # pad the message
        length = pack('<Q', len(msg) * 8)

        msg += b'\x80'
        msg += b'\x00' * ((56 - len(msg)) % 64)
        msg += length

        return msg

    def digest(self) -> bytes:
        # return the hash
        return pack('<IIII', self.A, self.B, self.C, self.D)


def verify_md5(test_string: bytes) -> None:
    # (DEBUG function) verify the MD5 implementation
    from hashlib import md5 as md5_hashlib

    def md5_manual(msg: bytes) -> bytes:
        md5 = MD5()
        md5.extend(md5.padding(msg))
        return md5.digest()

    manual_result = md5_manual(test_string).hex()
    hashlib_result = md5_hashlib(test_string).hexdigest()

    assert manual_result == hashlib_result, "Test failed!"


def attack(message_len: int, known_hash: str,
           append_str: bytes) -> tuple:
    # MD5 extension attack
    md5 = MD5()

    previous_text = md5.padding(b"*" * message_len)
    current_text = previous_text + append_str

    md5.A, md5.B, md5.C, md5.D = unpack("<IIII", bytes.fromhex(known_hash))
    md5.extend(md5.padding(current_text)[len(previous_text):])

    return current_text[message_len:], md5.digest().hex()


if __name__ == '__main__':

    message_len = int(input("[>] Input known text length: "))
    known_hash = input("[>] Input known hash: ").strip()
    append_text = input("[>] Input append text: ").strip().encode()

    print("[*] Attacking...")

    extend_str, final_hash = attack(message_len, known_hash, append_text)

    from urllib.parse import quote
    from base64 import b64encode

    print("[+] Extend text:", extend_str)
    print("[+] Extend text (URL encoded):", quote(extend_str))
    print("[+] Extend text (Base64):", b64encode(extend_str).decode())
    print("[+] Final hash:", final_hash)
```



### 生成指定开头的md5值

直接贴脚本:

```python
import hashlib
import random

def encrypt_md5(chars):
    """生成MD5哈希值"""
    return hashlib.md5(chars.encode('utf-8')).hexdigest()

def generate_random_number(length=8):
    """生成一个指定长度的随机数字字符串"""
    return str(random.randint(10 ** (length - 1), 10 ** length - 1))

def main():
    start = "8031b"  # 指定的MD5值开头字符
    num_length = 12  # 可以指定长度
    while True:
        random_number = generate_random_number(num_length)
        print(f"Test {random_number}")
        md5_value = encrypt_md5(random_number)
        if md5_value.startswith(start):
            print("Yes!")
            print(f"[+] {random_number} {md5_value}")
            break
        else:
            print("No!")

if __name__ == '__main__':
    main()
    print('完成！')
```

可以调节这两个变量：
```python
    start = "8031b"  # 指定的MD5值开头字符
    num_length = 12  # 可以指定长度
```



### 万能密码

```python
#万能密码
ffifdyop
```

如果遇到sql语句如下：

```sql
select * from 'admin' where password=md5($pass,true)
```

> 学习到的原理：
>
> `ffifdyop`绕过，绕过原理是： 
>
> `ffifdyop` 被 `md5` 哈希了之后会变成 `276f722736c95d99e921722cf9ed621c`，
>
> 这个字符串前几位刚好是`'or'6` 
>
> 而 **Mysql** 刚好又会把 hex 转成 ascii 解释，因此拼接之后的形式是
>
> ```sql
> select * from ‘admin’ where password=’’ or ‘6xxxxx’
> ```
>
> 等价于 or 一个永真式，因此相当于万能密码，可以绕过md5()函数。 

总的来说，遇到这个**sql**语句就可以使用万能密码



#### 一个例题:[BJDCTF2020]Easy MD5

进入题目页面：发现只有一个输入框，根据提示我们输入万能密码

![image-20240603172648128](https://gitee.com/bx33661/image/raw/master/path/image-20240603172648128.png)

```php
ffifdyop
```



![image-20240603172851687](https://gitee.com/bx33661/image/raw/master/path/image-20240603172851687.png)

```html
<!--
$a = $GET['a'];
$b = $_GET['b'];

if($a != $b && md5($a) == md5($b)){
    // wow, glzjin wants a girl friend.
-->
```

我们利用数组绕过这个md5检测：

![image-20240603173158946](https://gitee.com/bx33661/image/raw/master/path/image-20240603173158946.png)

```php
<?php
error_reporting(0);
include "flag.php";

highlight_file(__FILE__);

if($_POST['param1']!==$_POST['param2']&&md5($_POST['param1'])===md5($_POST['param2'])){
    echo $flag;
}
```

![image-20240603173448331](https://gitee.com/bx33661/image/raw/master/path/image-20240603173448331.png)

利用post传参，得到flag

----

CTF中的弱比较和MD5绕过：https://www.qwesec.com/2024/02/ctfweb-md5.html





### 补充

```php
    <?php
        $flag="";
        $v1=$_GET['v1'];
        $v2=$_GET['v2'];
        if(isset($v1) && isset($v2)){
            if(!ctype_alpha($v1)){
                die("v1 error");
            }
            if(!is_numeric($v2)){
                die("v2 error");
            }
            if(md5($v1)==md5($v2)){
                echo $flag;
            }
        }else{
        
            echo "where is flag?";
        }
    ?>
```

- `v1 = "QNKCDZO"`，`md5("QNKCDZO") = "0e830400451993494058024219903391"`
- `v2 = "240610708"`，`md5("240610708") = "0e462097431906509019562988736854"`