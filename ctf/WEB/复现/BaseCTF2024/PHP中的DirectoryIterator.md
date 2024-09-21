### PHP中的DirectoryIterator

---

先来看一个例子：

```php
<?php
$dir = new DirectoryIterator('E:\untitled1');

foreach ($dir as $fileinfo) {
    if ($fileinfo->isDot()) {
        continue;
    }
    echo "Name: " . $fileinfo->getFilename() . "\n";
    echo "Type: " . ($fileinfo->isDir() ? 'Directory' : 'File') . "\n";
    echo "Size: " . $fileinfo->getSize() . " bytes\n";
    echo "Last Modified: " . date('Y-m-d H:i:s', $fileinfo->getMTime()) . "\n";
    echo "-------------------------\n";
}
?>
```

结果如下：

```php
Name: .idea
Type: Directory
Size: 4096 bytes
Last Modified: 2024-09-20 07:25:05
-------------------------
Name: demo.php
Type: File
Size: 37 bytes
Last Modified: 2024-09-10 15:51:59
-------------------------
Name: demo1.php
Type: File
Size: 652 bytes
Last Modified: 2024-09-10 10:04:30
-------------------------
Name: example.txt
Type: File
Size: 35 bytes
Last Modified: 2024-09-11 04:33:35
-------------------------
Name: file.php
Type: File
Size: 321 bytes
Last Modified: 2024-09-10 08:44:37
-------------------------
Name: pear.php
Type: File
Size: 34 bytes
Last Modified: 2024-09-10 14:48:39
-------------------------
Name: php进阶
Type: Directory
Size: 4096 bytes
Last Modified: 2024-09-13 07:18:15
-------------------------
```

