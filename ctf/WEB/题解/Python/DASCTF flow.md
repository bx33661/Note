# DASCTF flow---/proc

----

![image-20250209210932446](https://gitee.com/bx33661/image/raw/master/path/image-20250209210932446.png)

当我们点击这个按钮会发现可以文件读取

![image-20250209211029345](https://gitee.com/bx33661/image/raw/master/path/image-20250209211029345.png)

但是尝试读取flag没有匹配文件

```(空)
/proc/self/environ
/proc/1/environ
```

![image-20250209211138239](https://gitee.com/bx33661/image/raw/master/path/image-20250209211138239.png)

![image-20250209211200930](https://gitee.com/bx33661/image/raw/master/path/image-20250209211200930.png)

**Kubernetes (k8s) 集群中的 Pod 运行环境**。

```bash
PATH=/usr/local/sbin:/usr/local/
bin:/usr/sbin:/usr/bin:/sbin:/
binHOSTNAME=
outFLAG=DASCTF{5ab6596a-f578-4474-ad99-6efc53569a0c}
KUBERNETES_PORT=tcp://10.240.0.1:443
KUBERNETES_PORT_443_TCP=tcp://10.240.0.1:443
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT_443_TCP_ADDR=10.240.0.1
KUBERNETES_SERVICE_HOST=10.240.0.1
KUBERNETES_SERVICE_PORT=443
KUBERNETES_SERVICE_PORT_HTTPS=443
DEBIAN_FRONTEND=HOME=/root
```



这一题我的理解是



![image-20250209211910193](https://gitee.com/bx33661/image/raw/master/path/image-20250209211910193.png)

./proc 文件系统基础

- **虚拟文件系统**：`/proc` 是内核提供的虚拟文件系统，用于暴露内核和进程的运行时信息
- **目录结构**：每个进程对应 `/proc/[PID]/` 目录