## OS库

> 内容格式由`Jupyter Notebook`导出
>
> 文档：https://docs.python.org/zh-cn/3/library/os.html

`os` 模块是 Python 标准库中的一个重要模块，提供了与操作系统交互的多种功能。它可以帮助你执行文件和目录操作、获取环境变量、执行系统命令等

采用`import` 语法引入 `os` 库

```python
import os
```

### 文件和目录操作

列出指定目录下的文件和子目录


```python
dirs = os.listdir(".")
print(dirs)
```

    ['.ipynb_checkpoints', 'enumerta()函数.md', 'learn.ipynb', 'macth-case语句.md', 'OOP', 'requirement.txt.md', 'sys和os库.md', 'zip语法.md', '基本类型', '迭代器', '高级操作']



```python
path = os.path.join('dir1', 'dir2', 'file.txt')
print(path)  # 输出: dir1/dir2/file.txt
```

    dir1\dir2\file.txt


遍历递归文件tree


```python

for root, dirs, files in os.walk('.'):
    print(f"Root: {root}")
    print(f"Dirs: {dirs}")
    print(f"Files: {files}")
```

    Root: .
    Dirs: ['.ipynb_checkpoints', 'OOP', '基本类型', '迭代器', '高级操作']
    Files: ['enumerta()函数.md', 'learn.ipynb', 'macth-case语句.md', 'requirement.txt.md', 'sys和os库.md', 'zip语法.md']
    Root: .\.ipynb_checkpoints
    Dirs: []
    Files: []
    Root: .\OOP
    Dirs: []
    Files: ['oop学习与分析.ipynb', 'OOP学习与分析2.ipynb']
    Root: .\基本类型
    Dirs: []
    Files: ['enumerate.ipynb', 'zip操作.ipynb', '元组tuple.ipynb', '多样条件判断.ipynb', '字典.ipynb', '断言语句.ipynb', '集合.ipynb']
    Root: .\迭代器
    Dirs: []
    Files: ['类迭代.py', '高级程序设计.ipynb']
    Root: .\高级操作
    Dirs: []
    Files: ['lambda.ipynb', '函数装饰器.ipynb']


### 环境变量

获取环境变量字典


```python
env = os.environ
for i in env:
    print(i)
```

    ALLUSERSPROFILE
    APPDATA
    APPLICATIONINSIGHTS_CONFIGURATION_CONTENT
    APPLICATION_INSIGHTS_NO_DIAGNOSTIC_CHANNEL
    CATALINA_HOME
    CHROME_CRASHPAD_PIPE_NAME
    CLION
    COMMONPROGRAMFILES
    COMMONPROGRAMFILES(X86)
    COMMONPROGRAMW6432
    COMPUTERNAME
    COMSPEC
    CUDA_PATH
    CUDA_PATH_V12_0
    CUDA_PATH_V12_5
    DEBUG
    DRIVERDATA
    ELECTRON_NO_ATTACH_CONSOLE
    ELECTRON_RUN_AS_NODE
    GOLAND
    GOPATH
    HOMEDRIVE
    HOMEPATH
    IGCCSVC_DB
    INTELLIJ IDEA
    JAVA_HOME
    JPY_INTERRUPT_EVENT
    LOCALAPPDATA
    LOGONSERVER
    MAVEN_HOME
    NUMBER_OF_PROCESSORS
    ONEDRIVE
    ONEDRIVECONSUMER
    OPENSSL_IA32CAP
    ORIGINAL_XDG_CURRENT_DESKTOP
    OS
    PATH
    PATHEXT
    PHP
    POSH_INSTALLER
    POSH_THEMES_PATH
    PROCESSOR_ARCHITECTURE
    PROCESSOR_IDENTIFIER
    PROCESSOR_LEVEL
    PROCESSOR_REVISION
    PROGRAMDATA
    PROGRAMFILES
    PROGRAMFILES(X86)
    PROGRAMW6432
    PROMPT
    PSMODULEPATH
    PUBLIC
    PYCHARM
    PYDEVD_IPYTHON_COMPATIBLE_DEBUGGING
    PYTHONIOENCODING
    PYTHONUNBUFFERED
    PYTHON_FROZEN_MODULES
    SESSIONNAME
    SYSTEMDRIVE
    SYSTEMROOT
    TEMP
    TMP
    USERDOMAIN
    USERDOMAIN_ROAMINGPROFILE
    USERNAME
    USERPROFILE
    VSCODE_AMD_ENTRYPOINT
    VSCODE_CLI
    VSCODE_CODE_CACHE_PATH
    VSCODE_CRASH_REPORTER_PROCESS_TYPE
    VSCODE_CWD
    VSCODE_DOTNET_INSTALL_TOOL_ORIGINAL_HOME
    VSCODE_HANDLES_UNCAUGHT_ERRORS
    VSCODE_IPC_HOOK
    VSCODE_L10N_BUNDLE_LOCATION
    VSCODE_NLS_CONFIG
    VSCODE_PID
    WINDIR
    WSLENV
    WT_PROFILE_ID
    WT_SESSION
    YAKIT_HOME
    ZES_ENABLE_SYSMAN
    PYDEVD_USE_FRAME_EVAL
    TERM
    CLICOLOR
    FORCE_COLOR
    CLICOLOR_FORCE
    PAGER
    GIT_PAGER
    MPLBACKEND


获取指定的环境变量


```python
go_path = os.getenv('GOPATH')
print(f"GOPATH_env = {go_path}")
```

    GOPATH_env = C:\Users\lenovo\go


### 系统命令和进程管理

os.system 的返回值
os.system 函数用于执行系统命令并返回该命令的退出码。例如：

```python
import os
```
执行一个命令
```python
return_code = os.system("ls")
```
打印返回值
```python
print(f"Return code: {return_code}")
```
返回值为 0：表示命令执行成功。
返回值非 0：表示命令执行失败，具体的非零值通常表示不同的错误类型。例如，1 可能表示一般错误，127 可能表示命令未找到。


```python
#调用起系统的计算器
os.system("C:\\windows\system32\calc.exe")
```


    0

![image-20241018162559519](https://gitee.com/bx33661/image/raw/master/path/image-20241018162559519.png)


```python
os.system("C:\\windows\system32\cmd.exe")
```


```python
os.system('ping www.bx33661.com')
```


    0

![image-20241018163107452](https://gitee.com/bx33661/image/raw/master/path/image-20241018163107452.png)

### 获取信息

获取用户名


```python
#获取用户名
os.getlogin()
```


    'lenovo'

获取当前路径


```python
os.getcwd()
#获取当前路径
```


    'e:\\gitproject\\Note\\工程学习\\Pyhton\\基本'

获取电脑cpu核心数


```python
os.cpu_count()
```


    32

获得n个字节长度的随机字符串


```python
#获得n个字节长度的随机字符串
os.urandom(8)
```


    b'\xf6Q\xee\t\xa8\xa3Mt'

获取进程PID


```python
#获取进程PID
pid = os.getpid()
print(f"当前进程的 PID: {pid}")
```

    当前进程的 PID: 26904

获取操作系统名称

```python
#获取操作系统名字
os_name = os.name
print(f"操作系统名字: {os_name}")
```

    操作系统名字: nt

> `os.name` 是一个字符串，表示当前操作系统的类型。它有以下几种可能的值：
>
> - **`'posix'`**: 表示类 Unix 操作系统，如 Linux、macOS 和其他 Unix 派生的系统。
> - **`'nt'`**: 表示 Windows 操作系统。
> - **`'java'`**: 表示 Jython，这是一种在 Java 平台上运行的 Python 实现。
>
> 为什么是 "nt"？
>
> - **nt** 是 "New Technology" 的缩写，这是 Microsoft 在 1993 年发布的 Windows NT 操作系统的简称。Windows NT 是 Windows 操作系统的高级版本，后来的 Windows 操作系统（如 Windows XP、Windows 7、Windows 10 等）都是基于 Windows NT 内核的。

```python
#更改当前工作路径
os.chdir('/path/to/directory')
```
