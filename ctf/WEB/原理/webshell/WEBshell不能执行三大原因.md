[[rBASH]]

导致 webshell 不能执行命令的原因大概有三类：
1. 一是 php.ini 中用 disable_functions 指示器禁用了 system()、exec() 等等这类命令执行的相关函数；
2. 二是 web 进程运行在 rbash 这类受限 shell 环境中；
3. 三是 WAF 拦劫。
若是一则无法执行任何命令，若是二、三则可以执行少量命令