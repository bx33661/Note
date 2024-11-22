# 在wsl2下配置zsh + 美化Ubuntu终端

**在安装前确保你的wsl2已安装完成**

## 第一步：安装zsh

```bash
sudo apt install zsh
```

![image-20240515113701206](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240515113701206.png)

---

```bash
cat /etc/shells
```

*查看linux下安装了有多少shell*：

![image-20240515122259502](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240515122259502.png)

---

```sh
chsh -s /bin/zsh ## 设为默认终端
```

---

## 安装oh-my-zsh：

### 1.三种官方下载方法：

- curl:`sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
- wget:`sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
- fetch:`sh -c "$(fetch -o - https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`

> 安装成功可以继续执行下一步，如果出现 403无法连接到对应库的话执行以下操作

![image-20240515125244066](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240515125244066.png)

1. ```
   git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh
   ```

2. ```
   cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
   ```

### 2.

```
ls ~/.oh-my-zsh/themes
```

![image-20240515125656107](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240515125656107.png)

---

1. 下载四个字体：

![image-20240515130344409](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240515130344409.png)

![image-20240515130400262](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240515130400262.png)

双击两下，安装即可

2.

> github:

```sh
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
```

> gitee:

```sh
git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

3.

```sh
exec zsh
```

4.然后就进入提示配置环节，按照自己要求选就好。