## Easylogin

进入一个登录界面，查了一圈没有什么发现

爆破密码得到`000000`

![image-20240821181033614](https://gitee.com/bx33661/image/raw/master/path/image-20240821181033614.png)

利用这个密码登录admin账号

![image-20240821181526469](https://gitee.com/bx33661/image/raw/master/path/image-20240821181526469.png)

并没用什么有用的发现，查了一下别人的wp

才知道有**302**跳转

利用bp抓包发现flag

![image-20240821181454246](https://gitee.com/bx33661/image/raw/master/path/image-20240821181454246.png)