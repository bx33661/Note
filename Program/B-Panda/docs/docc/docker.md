<meta name="referrer" content="no-referrer">

## Docker搭建记录

---

> 主要记录一下如何配置和部署docker，并且打包发布到Docker-Hub

[bx33661/btools-web general | Docker Hub](https://hub.docker.com/repository/docker/bx33661/btools-web/general)

![dockerhub](https://gitee.com/bx33661/image/raw/master/path/dockerhub.png)

docker desktop截图

![dockerdestop](https://gitee.com/bx33661/image/raw/master/path/dockerdestop.png)

### Docker命令

**`docker-compose down`**：停止并删除容器、网络和卷等资源。

**`docker-compose build --no-cache`**：重新构建镜像，并且不使用缓存。

![image-20241205175416059](https://gitee.com/bx33661/image/raw/master/path/image-20241205175416059.png)

**`docker-compose up -d`**：启动所有服务容器，并让它们在后台运行。



### Docker文编写

`dockerfile`编写:

```dockerfile
# 使用Python官方镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=Asia/Shanghai

# 安装系统依赖
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
        libpq-dev \
        build-essential \
        libfreetype6-dev \
        libffi-dev \
        libjpeg-dev \
        zlib1g-dev \
        liblcms2-dev \
        libwebp-dev \
        libopenjp2-7-dev \
        tcl8.6-dev \
        tk8.6-dev \
        python3-tk \
        libharfbuzz-dev \
        libfribidi-dev \
        libxcb1-dev \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 暴露端口
EXPOSE 5000

# 启动命令
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

```

`docker-compose`编写

```dockerfile
version: '3.8'

services:
  web:
    build: .
    image: bx33661/btools:latest
    container_name: btools-web
    restart: always
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
    volumes:
      - ./logs:/app/logs

networks:
  btools-network:
    driver: bridge

```



### Docker打包发布

在本地测试完成之后，可以打包发布到DockerHub等平台

这里以dockerhub为例子

![image-20241205175449937](https://gitee.com/bx33661/image/raw/master/path/image-20241205175449937.png)

```bash
docker build -t btools-web:latest .
docker login
docker tag btools-web:latest your-username/btools-web:latest
docker push your-username/btools-web:latest
```

**`docker tag <local_image_id> dockerhub_username/repository_name:tag`**