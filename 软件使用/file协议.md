## file协议

---

**基本语法**

`file://` 协议的基本语法是：

```php
file://[主机名]/路径
```

- `file://`：协议标识符，表示使用 file 协议。
- `[主机名]`：可选部分。在本地文件系统中，通常省略或使用 `localhost`。
- `/路径`：文件的绝对或相对路径。

**示例**

- 访问绝对路径：`file:///var/www/html/index.php` (Linux/macOS) 或 `file:///C:/www/index.php` (Windows)
- 访问相对路径：`file://./my_file.txt` (当前目录下的 my_file.txt) 或 `file://path/to/my_file.txt` (相对于当前脚本的路径)

**重要说明**

1. **相对路径**：当使用相对路径（不以 `/`、`\` 或 Windows 盘符开头的路径）时，路径是相对于**当前工作目录**的。在很多情况下，这是脚本所在的目录，除非被修改了。使用 CLI (命令行界面) 时，目录默认是脚本被调用时所在的目录。

2. **安全性**：由于 `file://` 协议可以访问本地文件系统，因此在使用时需要注意安全性问题。**绝对不要**允许用户直接控制 `file://` 协议的路径，否则可能导致任意文件读取漏洞。例如，如果你的代码是这样：

   PHP

   ```
   <?php
   $filename = $_GET['filename'];
   include("file://" . $filename); // 非常危险！
   ?>
   ```

   攻击者可以通过构造 `filename` 参数来读取任何服务器上的文件，例如 `../../../../etc/passwd`。

3. **与 `include`/`require` 的关系**：`include`、`include_once`、`require` 和 `require_once` 等包含文件函数默认就使用 `file://` 协议来访问本地文件。因此，`include("my_file.php")` 等同于 `include("file://./my_file.php")`。

4. **`allow_url_fopen` 和 `allow_url_include` 配置**：

   - `allow_url_fopen`：控制是否允许使用 URL 封装协议（包括 `file://`）来访问文件。默认是 `On`，即允许。
   - `allow_url_include`：控制是否允许使用 URL 封装协议（包括 `file://`）来包含文件。默认是 `Off`，即不允许。**强烈建议保持 `allow_url_include` 为 `Off`，以提高安全性。**

   即使 `allow_url_include` 是 `Off`，`file://` 协议仍然可以用于 `file_get_contents()`、`fopen()` 等函数，只要 `allow_url_fopen` 是 `On`。

5. **Windows 路径**：在 Windows 系统中，可以使用 `C:\`、`D:\` 等盘符来表示绝对路径。例如：`file:///C:/www/index.php`。注意，需要使用三个斜杠 `///`。

**总结**

`file://` 协议是 PHP 中访问本地文件系统的基本方式。理解其工作原理和安全性注意事项非常重要。始终要谨慎处理用户输入，避免潜在的安全漏洞。

**补充说明**

虽然 `file://` 协议主要用于访问本地文件系统，但在某些特殊情况下，如果 `allow_url_fopen` 设置为 `On`，它也可能被用于访问网络共享文件（例如使用 SMB 协议挂载的网络驱动器），但这通常不推荐，因为它可能存在性能和安全问题。

希望以上总结能够帮助你更好地理解 `file://` 协议。