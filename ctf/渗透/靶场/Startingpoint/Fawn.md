### Fawn

> 主要是FTP相关的

```bash
┌──(bx㉿kali)-[/home/bx]
└─PS> nmap -sC -sV -Pn 10.129.15.213
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-24 12:07 CST
Nmap scan report for 10.129.15.213
Host is up (0.39s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.54                                                                                     
|      Logged in as ftp                                                                                                    
|      TYPE: ASCII                                                                                                         
|      No session bandwidth limit                                                                                          
|      Session timeout in seconds is 300                                                                                   
|      Control connection is plain text                                                                                    
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.59 seconds

```



### Dancing

> SMB(Server Message Block)