<meta name="referrer" content="no-referrer">

## 框架前端样式

[[TOC]]

----

### 样式预览：

- 主页

![B-panda](https://gitee.com/bx33661/image/raw/master/path/B-panda.png)

![bbb](https://gitee.com/bx33661/image/raw/master/path/bbb.png)

- 工具页

![image-20241203211524999](https://gitee.com/bx33661/image/raw/master/path/image-20241203211524999.png)

![image-20241203211546785](https://gitee.com/bx33661/image/raw/master/path/image-20241203211546785.png)

![image-20241207115641019](https://gitee.com/bx33661/image/raw/master/path/image-20241207115641019.png)

![系统资源监控页面](https://gitee.com/bx33661/image/raw/master/path/%E7%B3%BB%E7%BB%9F%E8%B5%84%E6%BA%90%E7%9B%91%E6%8E%A7%E9%A1%B5%E9%9D%A2.png)

### 具体细节配置

引入https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js

#### 卡面：

主要是采用Bootstrap风格，和栏设计

> Bootstrap的网格系统基于12列布局，每个 `col-` 类表示一个列的宽度，数值（如6）表示该列占据12列总宽度的比例。

##### 工具栏风格

```html
            <div class="col-md-4 col-12">
                <div class="card shadow-sm d-flex flex-column" style="min-height: 250px;">
                    <div class="card-body text-center flex-grow-1">
                        <h5 class="card-title"><i class="fas fa-file-pdf text-danger"></i>PDF操作</h5>
                        <p class="card-text">快速处理您的PDF文件，例如合并、拆分或压缩。</p>
                        <a href="{{ url_for('pdf_routes.pdf_index') }}" class="btn btn-primary">前往操作</a>
                    </div>
                </div>
            </div>
```

--->

只需要配置`url_for`和`fas`图标

> `url_for` 是 Flask 框架中的一个函数，用于生成 URL。它通过端点名称（endpoint）和可选的参数来构建 URL

```html
<a href="{{ url_for('pdf_routes.pdf_index') }}" class="btn btn-primary">前往操作</a>
```



##### 重要卡面设计风格：

这个主要采用定向外链，添加时只需要配置`fas`图标

```html
        <div class="col-md-6">
            <div class="card shadow-sm special-card" style="min-width: 200px;">
                <div class="card-body text-center">
                    <h5 class="card-title"><i class="fas fa-book text-info"></i>文档说明</h5>
                    <p class="card-text">了解B-Panda的使用文档和常见问题解答。</p>
                    <a href="http://doc.bx33661.com/" class="btn btn-primary">查看文档</a>
                </div>
            </div>
        </div>
```

#### 工具页面

*主要背景采用渐变式样式*

可以按需求修改背景渐变：
```css
background: linear-gradient(45deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
```

linear-gradient 函数用于创建一个线性渐变背景。
45deg 表示渐变的角度，45 度是从左上角到右下角的渐变。
#ff9a9e, #fad0c4, #fbc2eb, #a18cd1 是渐变的颜色，从一个颜色渐变到另一个颜色，然后再渐变到下一个颜色，以此类推。

### 最新解决方案

> **模板继承**（Template Inheritance）或**模板扩展**（Template Extension）
>
> 在 Flask 中，它通过 Jinja2 模板引擎实现这种继承机制。这种模式的特点是：
>
> 1. **父模板**（如 `base.html`）：
>    - 定义基础的页面结构
>    - 使用 `{% block %}` 标记可以被子模板覆盖的区域
>    - 通常包含共用的元素（导航栏、页脚等）
> 2. **子模板**（如 `network.html`）：
>    - 使用 `{% extends %}` 声明继承自哪个父模板
>    - 只需要定义自己特有的内容
>    - 通过 `{% block %}` 填充父模板中预留的区域

我已经定义了基本模板`base.html`的样式，后续工具采用集成的方式就可以

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}B-Panda|自动化工具箱{% endblock %}</title>
    <!-- 引入 Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- 引入 Font Awesome -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <!-- 引入 Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    {% block styles %}{% endblock %}
</head>
<body>
    <!-- 导航栏 -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm sticky-top">
        <div class="container">
            <a class="navbar-brand text-primary fs-4 fw-bold" href="/">B-Panda</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link px-3 py-2" href="/" style="transition: color 0.3s ease-in-out;" onmouseover="this.style.color='#0d6efd'" onmouseout="this.style.color='#6c757d'">首页</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link px-3 py-2" href="/#about" style="transition: color 0.3s ease-in-out;" onmouseover="this.style.color='#0d6efd'" onmouseout="this.style.color='#6c757d'">关于作者</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link px-3 py-2" href="/#projects" style="transition: color 0.3s ease-in-out;" onmouseover="this.style.color='#0d6efd'" onmouseout="this.style.color='#6c757d'">项目介绍</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- 主要内容区域 -->
    <main>
        {% block content %}{% endblock %}
    </main>

    <!-- 引入 Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html> 
```

例如：

```(空)
{% extends "base.html" %}

{% block content %}
....内容
{% endblock %} 
```



### 完整代码

index.html:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>B-Panda|自动化工具箱</title>
    <!-- 引入 Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- 引入 Font Awesome -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <!-- 引入 Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #4a90e2;
            --secondary-color: #5c6ac4;
            --accent-color: #00c9a7;
            --text-color: #2d3748;
            --light-bg: #f8fafc;
        }

        body {
            font-family: 'Poppins', sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background: linear-gradient(135deg, #f6f9fc 0%, #f1f4f8 100%);
            animation: fadeIn 0.8s ease-in-out;
        }

        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        .navbar {
            background: rgba(255, 255, 255, 0.95) !important;
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(74, 144, 226, 0.1);
        }

        .navbar-brand {
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            transition: transform 0.3s ease;
        }

        .navbar-brand:hover {
            transform: scale(1.05);
        }

        .hero-section {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            border-radius: 20px;
            padding: 4rem;
            margin-top: 2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
            position: relative;
            overflow: hidden;
        }

        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 300px;
            height: 300px;
            background: linear-gradient(135deg, rgba(74, 144, 226, 0.1), rgba(92, 106, 196, 0.1));
            border-radius: 50%;
            transform: translate(50%, -50%);
            z-index: 0;
        }

        .hero-title {
            font-size: 3.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1.5rem;
        }

        .card {
            border: none;
            border-radius: 15px;
            transition: all 0.3s ease;
            background: white;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            overflow: hidden;
        }

        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        }

        .card-body {
            padding: 2rem;
        }

        .card-title {
            font-weight: 600;
            margin-bottom: 1.5rem;
            color: var(--primary-color);
        }

        .card-text {
            color: #64748b;
            font-size: 0.95rem;
            line-height: 1.7;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            border: none;
            padding: 0.8rem 2rem;
            border-radius: 10px;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(74, 144, 226, 0.3);
        }

        .special-card {
            background: linear-gradient(135deg, #ffffff, #f8fafc);
            border: 2px solid rgba(74, 144, 226, 0.1);
        }

        .about-section, .projects-section {
            background: white;
            border-radius: 20px;
            padding: 4rem;
            margin-top: 4rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        }

        /* 添加动画类 */
        .animate-on-scroll {
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.6s ease-out;
        }

        .animate-on-scroll.visible {
            opacity: 1;
            transform: translateY(0);
        }

        @media (max-width: 768px) {
            .hero-section {
                padding: 2rem;
                text-align: center;
            }

            .hero-title {
                font-size: 2.5rem;
            }

            .card {
                margin-bottom: 1.5rem;
            }
        }

        .hero-image img {
            filter: drop-shadow(0 10px 20px rgba(0,0,0,0.1));
        }
        
        @keyframes float {
            0% {
                transform: translateY(0px);
            }
            50% {
                transform: translateY(-20px);
            }
            100% {
                transform: translateY(0px);
            }
        }
        
        .special-card {
            transition: all 0.3s ease;
            border: none;
            background: linear-gradient(145deg, #ffffff, #f8fafc);
            box-shadow: 0 8px 20px rgba(74, 144, 226, 0.1);
        }
        
        .special-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 25px rgba(74, 144, 226, 0.2);
        }
        
        @media (max-width: 768px) {
            .hero-section {
                flex-direction: column;
                text-align: center;
                padding: 2rem;
            }
            
            .hero-image {
                margin-top: 2rem;
            }
            
            .hero-image img {
                max-width: 200px;
            }
        }
    </style>
</head>
<body>
    <!-- 导航栏 -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm sticky-top">
        <div class="container">
            <a class="navbar-brand text-primary fs-4 fw-bold" href="#">B-Panda</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link px-3 py-2" href="#" style="transition: color 0.3s ease-in-out;" onmouseover="this.style.color='#0d6efd'" onmouseout="this.style.color='#6c757d'">首页</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link px-3 py-2" href="#about" style="transition: color 0.3s ease-in-out;" onmouseover="this.style.color='#0d6efd'" onmouseout="this.style.color='#6c757d'">关于作者</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link px-3 py-2" href="#projects" style="transition: color 0.3s ease-in-out;" onmouseover="this.style.color='#0d6efd'" onmouseout="this.style.color='#6c757d'">项目介绍</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- 展示区 -->
    <div class="container mt-5 animate-on-scroll">
        <div class="hero-section d-flex align-items-center justify-content-between">
            <div class="hero-text">
                <h1 class="hero-title">B-Panda</h1>
                <p class="hero-subtitle fs-4 text-muted">一个基于Python开发的自动化工具集。<br>让工作更简单，效率更高。</p>
                <a href="#features" class="btn btn-primary mt-4">开始使用 <i class="fas fa-arrow-right ms-2"></i></a>
            </div>
            <div class="hero-image">
                <img src="https://www.bx33661.com/upload/thumbnails/2024/w1600/logo-removebg-preview.png" 
                     alt="B-Panda Logo" 
                     class="img-fluid" 
                     style="max-width: 300px; animation: float 3s ease-in-out infinite;">
            </div>
        </div>
    </div>

    <!-- 功能卡片区域 -->
    <div id="features" class="container mt-5">
        <h2 class="text-center mb-5 animate-on-scroll">核心功能</h2>
        <div class="row g-4">
            <!-- PDF操作卡片 -->
            <div class="col-md-4 col-12">
                <div class="card shadow-sm d-flex flex-column" style="min-height: 250px;">
                    <div class="card-body text-center flex-grow-1">
                        <h5 class="card-title"><i class="fas fa-file-pdf text-danger"></i>PDF操作</h5>
                        <p class="card-text">快速处理您的PDF文件，例如合并、拆分或压缩。</p>
                        <a href="{{ url_for('pdf_routes.pdf_index') }}" class="btn btn-primary">前往操作</a>
                    </div>
                </div>
            </div>
        
            <!-- 邮件操作卡片 -->
            <div class="col-md-4 col-12">
                <div class="card shadow-sm d-flex flex-column" style="min-height: 250px;">
                    <div class="card-body text-center flex-grow-1">
                        <h5 class="card-title"><i class="fas fa-envelope text-warning"></i>邮件操作</h5>
                        <p class="card-text">管理和自动化您的邮件，例如批量发送或格式化。</p>
                        <a href="{{ url_for('email_routes.email_index') }}" class="btn btn-primary">开始管理</a>
                    </div>
                </div>
            </div>
        
            <!-- 文件查找卡片 -->
            <div class="col-md-4 col-12">
                <div class="card shadow-sm d-flex flex-column" style="min-height: 250px;">
                    <div class="card-body text-center flex-grow-1">
                        <h5 class="card-title"><i class="fas fa-search text-success"></i>文件查找</h5>
                        <p class="card-text">通过关键字快速查找您的重要文件。</p>
                        <a href="{{ url_for('find_routes.find_index') }}" class="btn btn-primary">查找文件</a>
                    </div>
                </div>
            </div>
        
            <!-- Base64编解码 -->
            <div class="col-md-4 col-12">
                <div class="card shadow-sm d-flex flex-column" style="min-height: 250px;">
                    <div class="card-body text-center flex-grow-1">
                        <h5 class="card-title"><i class="fa-solid fa-keyboard"></i>Base64编解码</h5>
                        <p class="card-text">进行快速的Base64编解码，帮助我们快人一倍。</p>
                        <a href="{{ url_for('bs_routes.bs_index') }}"  class="btn btn-primary">Base64</a>
                    </div>
                </div>
            </div>
        
            <!-- 系统监控 -->
            <div class="col-md-4 col-12">
                <div class="card shadow-sm d-flex flex-column" style="min-height: 250px;">
                    <div class="card-body text-center flex-grow-1">
                        <h5 class="card-title"><i class="fas fa-desktop text-primary"></i>系统监控</h5>
                        <p class="card-text">实时看系统状态，了解性能和健康状况。</p>
                        <a href="{{ url_for('system_monitor.index') }}" class="btn btn-primary">开始监控</a>
                    </div>
                </div>
            </div>
    
            <!-- 网络工具 -->
            <div class="col-md-4 col-12">
                <div class="card shadow-sm d-flex flex-column" style="min-height: 250px;">
                    <div class="card-body text-center flex-grow-1">
                        <h5 class="card-title"><i class="fas fa-network-wired text-purple"></i>网络工具</h5>
                        <p class="card-text">IP查询、端口扫描、Ping测试等功能。</p>
                        <a href="{{ url_for('network_routes.network_index') }}" class="btn btn-primary">开始诊断</a>
                    </div>
                </div>
            </div>
        
        </div>  
    </div>


        <!-- 重要卡片布局 -->
        <div class="container mt-5">
            <div class="row justify-content-center g-4">
                <!-- 文档说明卡片 -->
                <div class="col-md-5">
                    <div class="card shadow-sm special-card h-100">
                        <div class="card-body text-center d-flex flex-column">
                            <h5 class="card-title">
                                <i class="fas fa-book text-info me-2"></i>文档说明
                            </h5>
                            <p class="card-text flex-grow-1">了解B-Panda的使用文档和常见问题解。</p>
                            <a href="http://doc.bx33661.com/" class="btn btn-primary mt-auto">查看文档</a>
                        </div>
                    </div>
                </div>
                
                <!-- B-Panda|网站监控卡片 -->
                <div class="col-md-5">
                    <div class="card shadow-sm special-card h-100">
                        <div class="card-body text-center d-flex flex-column">
                            <h5 class="card-title">
                                <i class="fas fa-desktop text-primary me-2"></i>B-Panda|网站监控
                            </h5>
                            <p class="card-text flex-grow-1">监控网站状态，了解性能和健康状况。</p>
                            <a href="https://www.github.com/BX33661/B-Panda" class="btn btn-primary mt-auto">开始监控</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 关于作者 -->
        <div id="about" class="container mt-5 about-section">
            <h2 class="text-center">关于作者</h2>
            <p class="text-center mt-3">大家好，我是BX33661，我们一起见证星辰大海。</p>
            <p class="text-center mt-3">个人博客：<a href="http://www.bx33661.com" target="_blank">www.bx33661.com</a></p>
        </div>

        <!-- 项目介绍 -->
        <div id="projects" class="container mt-5 projects-section">
            <h2 class="text-center">项目介绍</h2>
            <p class="text-center mt-3">这个项目是高级程序设计课程结课作业，由BX33661独立完成。</p>
            <p class="text-center mt-3">这是一个基于Flask框架搭建的Python自动化项目，旨在简化日常任务自动化处理。项目通过Flask作为后端，结合Python的各种自动化库，实现了任务调度、据处理与告生成等功能。技术栈括Flask、Python等，具有良好的扩展性和易于维护的架构。未来版本将进一步优化用户界面并增加更多自动化功能。</p>
        </div>
    </div>

    <!-- 引入 Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <!-- 添加新的脚本 -->
    <script>
        // 滚动动画
        function checkScroll() {
            const elements = document.querySelectorAll('.animate-on-scroll');
            elements.forEach(element => {
                const elementTop = element.getBoundingClientRect().top;
                const elementVisible = 150;
                
                if (elementTop < window.innerHeight - elementVisible) {
                    element.classList.add('visible');
                }
            });
        }

        window.addEventListener('scroll', checkScroll);
        checkScroll(); // 初始检查

        // 导航栏滚动效果
        window.addEventListener('scroll', function() {
            const navbar = document.querySelector('.navbar');
            if (window.scrollY > 50) {
                navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
            } else {
                navbar.style.boxShadow = 'none';
            }
        });
    </script>
</body>
</html>
```



bs.html:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Base64 编码解码</title>
    <!-- 引入 Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- 引入 Font Awesome -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(45deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
            background-size: 300% 300%;
            animation: gradientAnimation 10s ease infinite;
            color: #fff;
            font-family: 'Arial', sans-serif;
        }
        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .container {
            max-width: 800px;
            margin: 3rem auto;
            background: rgba(255, 255, 255, 0.9);
            color: #333;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }
        .form-label {
            font-weight: bold;
        }
        .form-select, .form-control {
            border-radius: 0.5rem;
        }
        .btn-primary {
            width: 100%;
            padding: 0.8rem;
            font-size: 1rem;
            border-radius: 0.5rem;
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            border: none;
        }
        .btn-primary:hover {
            background: linear-gradient(135deg, #2575fc, #6a11cb);
        }
        .btn-secondary {
            width: 100%;
            padding: 0.8rem;
            font-size: 1rem;
            border-radius: 0.5rem;
            background-color: #f1f1f1;
            border: none;
        }
        .btn-secondary:hover {
            background-color: #e0e0e0;
        }
    </style>
</head>
<body>

    <!-- 主容器 -->
    <div class="container">
        <h1 class="text-center text-primary mb-4">Base64 编码解码</h1>

        <!-- 编码部分 -->
        <div class="mb-5">
            <h3>编码</h3>
            <label for="encode_input" class="form-label">输入文本：</label>
            <textarea id="encode_input" class="form-control" rows="4" placeholder="请输入要编码的文本"></textarea>
            <button id="encode_btn" class="btn btn-primary mt-3">开始编码</button>
            <div class="mt-3">
                <label for="encoded_output" class="form-label">编码结果：</label>
                <textarea id="encoded_output" class="form-control" rows="4" readonly placeholder="编码结果会显示在这里"></textarea>
            </div>
        </div>

        <!-- 解码部分 -->
        <div>
            <h3>解码</h3>
            <label for="decode_input" class="form-label">输入Base64字符串：</label>
            <textarea id="decode_input" class="form-control" rows="4" placeholder="请输入Base64字符串"></textarea>
            <button id="decode_btn" class="btn btn-secondary mt-3">开始解码</button>
            <div class="mt-3">
                <label for="decoded_output" class="form-label">解码结果：</label>
                <textarea id="decoded_output" class="form-control" rows="4" readonly placeholder="解码结果会显示在这里"></textarea>
            </div>
        </div>

        <div class="text-center mt-4">
            <a href="{{ url_for('index') }}">返回首页</a>
        </div>
    </div>

    <!-- 引入 Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    
    <script>
        document.getElementById('encode_btn').addEventListener('click', function () {
            var inputString = document.getElementById('encode_input').value;
            fetch('/base/encode', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ input_string: inputString })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('encoded_output').value = data.encoded_string;
            })
            .catch(error => alert('编码失败: ' + error));
        });

        document.getElementById('decode_btn').addEventListener('click', function () {
            var base64String = document.getElementById('decode_input').value;
            fetch('/base/decode', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ base64_string: base64String })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('decoded_output').value = data.decoded_string;
            })
            .catch(error => alert('解码失败: ' + error));
        });
    </script>

</body>
</html>

```

