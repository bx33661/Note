### wsl转移操作

1. 查看已安装版本 # wsl -l --all -v  NAME     STATE      VERSION * kali-linux  Running     2 

2.导出分发版为tar文件到E盘 # wsl --export kali-linux E:\kali-linux.tar 

3. 注销当前分发版 # wsl --unregister kali-linux 
4. 重新导入并安装WSL在D盘 # wsl --import kali-linux E:\kali-linux E:\kali-linux.tar --version 2 
5. 删除wsl-ubuntu20.04.tar # del E:\kali-linux.tar
6. 设置默认用户 # kali config --default-user 用户名