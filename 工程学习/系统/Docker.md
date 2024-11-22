# Docker

---

## 运行测试

### busybox

1. 拉取镜像

```bash
docker pull busybox:latest
```

2. 运行busybox

```bash
docker run -it busybox
```

- **`-i` (Interactive)**：表示运行容器时保持标准输入（stdin）打开，这样你可以与容器中的进程进行交互。

- **`-t` (TTY)**：为容器分配一个伪终端（pseudo-TTY），这使得你可以在终端中以交互式的方式运行命令。

