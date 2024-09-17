## Ubuntu软件安装

### php

在Ubuntu上安装PHP可以通过几个简单的步骤完成。以下是安装PHP的基本步骤：

1. **更新包列表**：
   首先，确保你的包列表是最新的。打开终端并运行以下命令：
   ```bash
   sudo apt update
   ```

2. **安装PHP**：
   默认情况下，Ubuntu的软件包库中包含PHP。使用以下命令安装PHP及其常用扩展：
   
   ```bash
   sudo apt install php libapache2-mod-php php-mysql
   ```
   这将安装PHP及其与Apache和MySQL的集成。
   
3. **验证安装**：
   安装完成后，你可以通过检查PHP版本来验证安装是否成功：
   ```bash
   php -v
   ```
   这将显示已安装的PHP版本信息。

4. **安装其他PHP扩展（可选）**：
   根据你的需求，你可能需要安装其他PHP扩展。例如：
   ```bash
   sudo apt install php-xml php-gd php-curl php-mbstring
   ```
   这些扩展用于处理XML、图像处理、HTTP请求和多字节字符串等功能。

5. **配置Apache以支持PHP**：
   如果你使用的是Apache服务器，通常安装过程会自动配置Apache以支持PHP。如果需要手动配置，可以编辑Apache的配置文件（例如`/etc/apache2/apache2.conf`）来确保PHP模块已启用。

6. **重启Apache服务器**：
   安装和配置完成后，重启Apache服务器以应用更改：
   
   ```bash
   sudo systemctl restart apache2
   ```

