## Docker搭建记录

<meta name="referrer" content="no-referrer">

---

> 主要记录一下如何配置和部署docker，并且打包发布到Docker-Hub

[bx33661/btools-web general | Docker Hub](https://hub.docker.com/repository/docker/bx33661/btools-web/general)

![image-20241205174825600](https://gitee.com/bx33661/image/raw/master/path/image-20241205174825600.png)

docker desktop截图

![image-20241205175332167](https://gitee.com/bx33661/image/raw/master/path/image-20241205175332167.png)

### Docker命令

**`docker-compose down`**：停止并删除容器、网络和卷等资源。

**`docker-compose build --no-cache`**：重新构建镜像，并且不使用缓存。

![image-20241205175416059](https://gitee.com/bx33661/image/raw/master/path/image-20241205175416059.png)

**`docker-compose up -d`**：启动所有服务容器，并让它们在后台运行。



### Docker文编写

`dockerfile`编写:

```dockerfile
# 使用Python官方镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 5000

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# 启动命令
CMD ["python", "app.py"]

```

`docker-compose`编写

```dockerfile
version: '3.8'

services:
  web:
    image: bx33661/btools-web:latest  
    container_name: btools-web
    ports:
      - "5000:5000"
    environment:
      - FLASK_APP=app.py
      - FLASK_ENV=production
    restart: unless-stopped
    networks:
      - btools-network

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