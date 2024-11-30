`systemctl` 是一个强大的命令行工具，用于管理和控制 systemd 初始化系统下的系统服务、目标（target）、挂载点（mount）、套接字（socket）等。它是 systemd 的核心命令行接口，提供了对系统资源的全面管理。

### systemd 简介
systemd 是一个系统和服务管理器，负责初始化系统、管理系统服务、监控系统资源等。它取代了传统的 SysV init 系统，成为现代 Linux 系统的标准初始化系统。

### systemctl 命令的基本用法
以下是 `systemctl` 命令的基本用法和常见子命令：

#### 1. **服务管理**
* **启动服务**：`systemctl start <服务名>`
* **停止服务**：`systemctl stop <服务名>`
* **重启服务**：`systemctl restart <服务名>`
* **检查服务状态**：`systemctl status <服务名>`

#### 2. **服务启用和禁用**
* **启用服务（开机自启动）**：`systemctl enable <服务名>`
* **禁用服务（取消开机自启动）**：`systemctl disable <服务名>`

#### 3. **目标（Target）管理**
* **列出所有目标**：`systemctl list-units --type=target`
* **切换到图形界面目标**：`systemctl isolate graphical.target`
* **切换到多用户命令行界面目标**：`systemctl isolate multi-user.target`

#### 4. **系统状态和日志**
* **显示系统状态**：`systemctl status`
* **显示所有日志**：`journalctl`
* **显示特定服务的日志**：`journalctl -u <服务名>`

#### 5. **其他操作**
* **重载 systemd 配置**：`systemctl daemon-reload`
* **检查服务是否配置为开机自启动**：`systemctl is-enabled <服务名>`

### 示例
* **启动 Docker 服务**：`systemctl start docker`
* **检查 Docker 服务状态**：`systemctl status docker`
* **启用 Docker 服务开机自启动**：`systemctl enable docker`

