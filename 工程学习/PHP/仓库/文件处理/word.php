<?php
$myfile = fopen("E:/untitled1/php进阶/文件处理/db.txt", "r") or die("Unable to open file!");
echo fread($myfile, filesize("E:/untitled1/php进阶/文件处理/db.txt"));
fclose($myfile);
