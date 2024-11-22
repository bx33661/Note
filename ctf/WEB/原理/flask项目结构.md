### flask项目结构

> 参加上次会议之后，觉得认识常见框架结构也是很重要的，整好加深一下对flask的理解

#### 简单项目

就是一个环境文件和单一应用文件

```
flask_app/
│
├── app.py
└── requirements.txt
```



#### 较大项目

这个主要是吧`app.py`文件进行细化，

- `__init__`初始化
- `routes.py` 路由定义的一些列函数
- `models.py`  数据模型

```
flask_app/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
│
├── config.py
├── requirements.txt
└── run.py
```

这个`config.py` 在我见到的案例中，主要是储存一些配置文件，配置api的键值对之类的东西，基本都是在根目录下



### 大项目（比较完整）

> 这个就比较完善了，添加了一些模板

```
my_flask_app/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── auth.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── templates/
│   │   ├── layout.html
│   │   └── home.html
│   └── static/
│       ├── css/
│       └── js/
│
├── config.py
├── requirements.txt
├── migrations/
│   └── ...
└── run.py
```

在网上找了张图借用一下

![img](https://gitee.com/bx33661/image/raw/master/path/548928cdca884e7341f047b3ecec83bf.png)

**`app/templates/`**：存放模板文件

**`app/static`** :就是存放前端的一些内容

其他的都是继续细分，形成完整结构



![image-20240929100511317](https://gitee.com/bx33661/image/raw/master/path/image-20240929100511317.png)

这个就算比较简单的结构，其实通过app.py的import结构也能窥探一些内容