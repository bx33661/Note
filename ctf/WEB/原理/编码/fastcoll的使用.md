## fastcoll的使用

---

### 生成两md5相同的图片

```bash
PS E:\Tools\CTF\WEB\fastcoll_v1.0.0.5.exe> ./fastcoll_v1.0.0.5.exe -p 1.jpg -o 11.jpg 12.jpg
MD5 collision generator v1.5
by Marc Stevens (http://www.win.tue.nl/hashclash/)

Using output filenames: '11.jpg' and '12.jpg'
Using prefixfile: '1.jpg'
Using initial value: 5bced2a67e9c03658bc9699a1344ddde

Generating first block: ..
Generating second block: S10.......................
Running time: 0.773 s
```



#### XYCTF一道题

> md5碰撞

![image-20250117120534988](https://gitee.com/bx33661/image/raw/master/path/image-20250117120534988.png)

我们直接上传我们生成的两张图片

```bash
{"areEqual":true,"md5Equal":true,"md5_1":"e9942a0951dffce07bc7d06e10151775","md5_2":"e9942a0951dffce07bc7d06e10151775"}XYCTF{83b8beab-05bf-4e57-bf28-0bbb861a209e}
```

