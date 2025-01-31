# HTB-Crocodile

---

![image-20250125141558979](https://gitee.com/bx33661/image/raw/master/path/image-20250125141558979.png)

```bash
┌──(bx㉿kali)-[~/桌面]
└─$ nmap -sV -sC 10.129.196.17    
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-25 14:14 CST
Nmap scan report for 10.129.196.17
Host is up (0.27s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.119
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
|_-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Smash - Bootstrap Business Template
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 22.45 seconds

```

> `-sV`（版本检测）, 会尝试确定目标主机上运行的服务的具体版本信息。
>
> `-sC`（默认脚本扫描）,看到脚本执行的结果，可能包括额外的服务信息、漏洞提示、或其他有用的信息。

![image-20250125142200301](https://gitee.com/bx33661/image/raw/master/path/image-20250125142200301.png)

![image-20250125144243635](https://gitee.com/bx33661/image/raw/master/path/image-20250125144243635.png)

连接ftp

```bash
┌──(bx㉿kali)-[~/桌面]
└─$ ftp 10.129.196.17
Connected to 10.129.196.17.
220 (vsFTPd 3.0.3)
Name (10.129.196.17:bx): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||45295|)
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
226 Directory send OK.
ftp> get allowed.userlist
local: allowed.userlist remote: allowed.userlist
229 Entering Extended Passive Mode (|||47617|)
150 Opening BINARY mode data connection for allowed.userlist (33 bytes).
100% |***************************************************************************************************************|    33        1.01 MiB/s    00:00 ETA
226 Transfer complete.
33 bytes received in 00:00 (0.11 KiB/s)
ftp> 

```

**What Nmap scanning switch employs the use of default scripts during a scan?**

-sC

**What service version is found to be running on port 21?**

vsftpd 3.0.3

**What FTP code is returned to us for the "Anonymous FTP login allowed" message?**

230

**After connecting to the FTP server using the ftp client, what username do we provide when prompted to log in anonymously?**

get

**What is one of the higher-privilege sounding usernames in 'allowed.userlist' that we download from the FTP server?**

admin

**What version of Apache HTTP Server is running on the target host?**

Apache httpd 2.4.41

**What switch can we use with Gobuster to specify we are looking for specific filetypes?**

-x 

```bash
┌──(bx㉿kali)-[~/桌面]
└─$ gobuster --help                                            
Usage:
  gobuster [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  dir         Uses directory/file enumeration mode
  dns         Uses DNS subdomain enumeration mode
  fuzz        Uses fuzzing mode. Replaces the keyword FUZZ in the URL, Headers and the request body
  gcs         Uses gcs bucket enumeration mode
  help        Help about any command
  s3          Uses aws bucket enumeration mode
  tftp        Uses TFTP enumeration mode
  version     shows the current version
  vhost       Uses VHOST enumeration mode (you most probably want to use the IP address as the URL parameter)

Flags:
      --debug                 Enable debug output
      --delay duration        Time each thread waits between requests (e.g. 1500ms)
  -h, --help                  help for gobuster
      --no-color              Disable color output
      --no-error              Don't display errors
  -z, --no-progress           Don't display progress
  -o, --output string         Output file to write results to (defaults to stdout)
  -p, --pattern string        File containing replacement patterns
  -q, --quiet                 Don't print the banner and other noise
  -t, --threads int           Number of concurrent threads (default 10)
  -v, --verbose               Verbose output (errors)
  -w, --wordlist string       Path to the wordlist. Set to - to use STDIN.
      --wordlist-offset int   Resume from a given position in the wordlist (defaults to 0)

Use "gobuster [command] --help" for more information about a command.

```

**Which PHP file can we identify with directory brute force that will provide the opportunity to authenticate to the web service?**

```bash
┌──(bx㉿kali)-[~/桌面]
└─$ dirsearch -u http://10.129.196.17                                          
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3                                                                                                                            
 (_||| _) (/_(_|| (_| )                                                                                                                                     
                                                                                                                                                            
Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/bx/桌面/reports/http_10.129.196.17/_25-01-25_14-31-18.txt

Target: http://10.129.196.17/

[14:31:18] Starting:                                                                                                                                        
[14:31:23] 301 -  311B  - /js  ->  http://10.129.196.17/js/                 
[14:31:30] 403 -  278B  - /.ht_wsr.txt                                      
[14:31:30] 403 -  278B  - /.htaccess.orig                                   
[14:31:30] 403 -  278B  - /.htaccess.save                                   
[14:31:30] 403 -  278B  - /.htaccess_sc
[14:31:30] 403 -  278B  - /.htaccess_orig
[14:31:30] 403 -  278B  - /.htaccess.sample                                 
[14:31:30] 403 -  278B  - /.htaccess_extra
[14:31:30] 403 -  278B  - /.htaccess.bak1                                   
[14:31:30] 403 -  278B  - /.htaccessBAK
[14:31:30] 403 -  278B  - /.htaccessOLD2
[14:31:30] 403 -  278B  - /.htaccessOLD                                     
[14:31:30] 403 -  278B  - /.htm                                             
[14:31:30] 403 -  278B  - /.html
[14:31:30] 403 -  278B  - /.htpasswd_test                                   
[14:31:30] 403 -  278B  - /.htpasswds
[14:31:30] 403 -  278B  - /.httr-oauth                                      
[14:31:34] 403 -  278B  - /.php                                             
[14:32:09] 301 -  315B  - /assets  ->  http://10.129.196.17/assets/         
[14:32:09] 200 -  526B  - /assets/                                          
[14:32:19] 200 -    0B  - /config.php                                       
[14:32:22] 301 -  312B  - /css  ->  http://10.129.196.17/css/               
[14:32:23] 302 -    0B  - /dashboard/  ->  /login.php                       
[14:32:23] 301 -  318B  - /dashboard  ->  http://10.129.196.17/dashboard/   
[14:32:33] 301 -  314B  - /fonts  ->  http://10.129.196.17/fonts/           
[14:32:42] 200 -  479B  - /js/                                              
[14:32:46] 200 -  718B  - /login.php                                        
[14:32:47] 302 -    0B  - /logout.php  ->  login.php                        
[14:33:11] 403 -  278B  - /server-status                                    
[14:33:11] 403 -  278B  - /server-status/
```



**Submit root flag**

利用刚才ftp得到的密码和账号进行登录：
admin/rKXM59ESxesUFHAd

![image-20250125144433852](https://gitee.com/bx33661/image/raw/master/path/image-20250125144433852.png)