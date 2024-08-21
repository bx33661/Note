# Picgo打造个人图床

---

![image-20240529123910462](https://gitee.com/bx33661/image/raw/master/path/image-20240529123910462.png)

具体资源：

- [Picgo官方使用手册](https://picgo.github.io/PicGo-Doc/zh/guide/#picgo-is-here)

- [Picgo-gihtub](https://github.com/Molunerfinn/PicGo)
- 百度网盘下载：链接：https://pan.baidu.com/s/1SXusWry5hWRDJmyBK8T83Q?pwd=0wx3 提取码：0wx3 

1. 按要求安装完成安装

![769e16363bc8706de198bbef9e16089](https://gitee.com/bx33661/image/raw/master/path/769e16363bc8706de198bbef9e16089.png)

2. 配置仓库（这里使用gitee）

- 首先你得注册一个gitee的账号
- 创建一个仓库，具体配置如下

![image-20240529164310113](https://gitee.com/bx33661/image/raw/master/path/image-20240529164310113.png)

- 在设置中申请“私人令牌”：

![image-20240529164433129](https://gitee.com/bx33661/image/raw/master/path/image-20240529164433129.png)

**切记要保存好你的密钥**

3. 配置Picgo：

![image-20240529164609918](https://gitee.com/bx33661/image/raw/master/path/image-20240529164609918.png)

![image-20240529164729787](https://gitee.com/bx33661/image/raw/master/path/image-20240529164729787.png)

- repo:填上你的 名字/仓库名字（例如：bx33661/image）
- branch:master
- token:你的密钥
- path：path
- 其他不填就可以

4. 扩展：Typro配置：

设置->![image-20240529182232682](https://gitee.com/bx33661/image/raw/master/path/image-20240529182232682.png)



---

## 解决博客中图床无法显示的问题

在写东西的时候经常遇到这类问题，图床上图片无法正常显示

在blog头中添加：

```html
<meta name="referrer" content="no-referrer" />
```

![image-20240529125722271](https://gitee.com/bx33661/image/raw/master/path/image-20240529125722271.png)

> 这里查询了一下网络：
>
> 1. HTML的 标签提供了 HTML 文档的元数据。元数据不会显示在客户端，但是会被浏览器解析。这也是为什么加在mardown文章里不会看到这段代码的原因。
> 2. HTML 的 name 属性规定了元数据的名称，这里我们用到的是referer属性，这个属性的作用是让服务器判断来源页面，即用户是从哪来的，很多时候referer被当做防盗链来使用，服务器根据你的访问来源判断是否应该让你下载这个资源，如果你的来源不和规范，比如是个恶意爬虫，那么就会产生403错误。
> 3. 到这里，`content="no-referrer"`的意义就呼之欲出了，既然我们想拿到这个资源但被服务器认出来之后又被拒绝了，那么伪装一下，不告诉服务器不就行了？所以，这里content的no-referer就是表示不发送引用数据，隐藏自己的来源信息。这样，图片就能正常显示了。