# web靶场搭建

---

> 这次决定尝试自己搭建靶场，学习这个流程
>
> 这里使用的是阿里云2核云服务器

## 环境配置

### 安装docker

```bash
sudo apt update

apt-get install ca-certificates curl gnupg lsb-release

#安装证书
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -

#写入软件源
sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"

#安装docker
sudo apt install -y docker-ce

#验证安装
docker --version
```

### 安装`docker-compose`

```bash
#下载docker-compose 二进制文件
sudo curl -L "https://github.com/docker/compose/releases/download/v2.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

#添加权限
sudo chmod +x /usr/local/bin/docker-compose

#验证安装
docker-compose --version
```

![image-20240809142919544](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240809142919544.png)

## 搭建靶场

> 这里使用探姬-[PHPSerialize-labs](https://github.com/ProbiusOfficial/PHPSerialize-labs)：https://github.com/ProbiusOfficial/PHPSerialize-labs

### 使用docker-compose部署

```bash
git clone --depth 1 https://github.com/ProbiusOfficial/PHPSerialize-labs.git
cd PHPSerialize-labs
sudo docker-compose up -d   # 访问 http://localhost:8080/
```

![image-20240809143439082](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240809143439082.png)

这里用的是服务器所以我访问：http://myip:8080

需要注意的是如果你用的是服务器部署的话，需要开启8080端口的访问权限

![image-20240809150210676](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240809150210676.png)

![image-20240809150505722](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240809150505722.png)