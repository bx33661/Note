### Linux创建用户

---

#### 新手模式

```bash
sudo adduser username
```

![image-20240917131953786](https://gitee.com/bx33661/image/raw/master/path/image-20240917131953786.png)

#### 另一种方法

```
sudo useradd -m username
sudo passwd username
sudo usermod -aG sudo username
su - username
```



