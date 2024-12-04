## Git一些操作

---

1. 查看分支

```bash
git branch
```

![image-20241204110601539](https://gitee.com/bx33661/image/raw/master/path/image-20241204110601539.png)

2. 新建分支

```bash
git branch dx33661
```

![image-20241204110718929](https://gitee.com/bx33661/image/raw/master/path/image-20241204110718929.png)

3. 切换分支

```bash
git checkout fetch
```

4. 合并分支：当前在master,将fetch合并过来

```bash
git merge fetch
```



### 解决冲突

一个简单的例子：

在master 分支

![image-20241204111339652](https://gitee.com/bx33661/image/raw/master/path/image-20241204111339652.png)

在fetch 分支

![image-20241204111426238](https://gitee.com/bx33661/image/raw/master/path/image-20241204111426238.png)

```bash
git merge fetch
```

![image-20241204111735241](https://gitee.com/bx33661/image/raw/master/path/image-20241204111735241.png)

![image-20241204111722611](https://gitee.com/bx33661/image/raw/master/path/image-20241204111722611.png)

```txt
<<<<<<< HEAD
这是 main 分支上的内容
=======
这是 fetch 分支上的内容
>>>>>>> new-feature

```



### Github上拉去请求

提交端：
![image-20241204114815966](https://gitee.com/bx33661/image/raw/master/path/image-20241204114815966.png)



作者端：审查和判断是否接受和merge

![image-20241204114620837](https://gitee.com/bx33661/image/raw/master/path/image-20241204114620837.png)