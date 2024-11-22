# Bash命令

[TOC]

---

### Base64

1. 编码字段

```bash
echo helloword |Base64
#aGVsbG93b3JsZAo=
```

2. 编码文件

```bash
base64 input.txt > output.txt
```

3. 解码字段

```bash
echo aGVsbG93b3JsZAo= |base64 -d
```

4. 解码文件

```bash
base64 -d output.txt > input.txt
```

> 注意的是
>
> - Base64 编码后数据量会增加，大约会比原始数据增加33%。
>
> 大概是base是3->4的过程
>
> - **换行符**：`base64` 编码结果默认每76个字符会插入一个换行符。如果你不希望有换行符，可以使用 `-w 0` 参数：
>
>   ```bash
>   echo -n "Hello, World!" | base64 -w 0
>   ```