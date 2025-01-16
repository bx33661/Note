## [ASIS 2019]Unicorn shop

> 主要是关于Unicode编码问题
>
> 查询网站：：：https://www.compart.com/en/unicode/

---

![image-20250116203521125](https://gitee.com/bx33661/image/raw/master/path/image-20250116203521125.png)

我们需要使用购买第四个才能成功，但是只能一个字符，所以利用unicode找到大于1337的字符

这里直接使用utf-8的话是不行的

将utf-8的值中的0x变为%

%E2%86%88

[“፼” U+137C Ethiopic Number Ten Thousand Unicode Character (compart.com)](https://www.compart.com/en/unicode/U+137C)

![image-20250116205519120](https://gitee.com/bx33661/image/raw/master/path/image-20250116205519120.png)