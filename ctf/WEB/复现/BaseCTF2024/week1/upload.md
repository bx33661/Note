### upload

----

```php
<?php
error_reporting(0);
if (isset($_FILES['file'])) {
    highlight_file(__FILE__);
    $file = $_FILES['file'];
    $filename = $file['name'];
    $filetype = $file['type'];
    $filesize = $file['size'];
    $filetmp = $file['tmp_name'];
    $fileerror = $file['error'];

    if ($fileerror === 0) {
        $destination = 'uploads/' . $filename;
        move_uploaded_file($filetmp, $destination);
        echo 'File uploaded successfully';
    } else {
        echo 'Error uploading file';
    }
}
?>
```

没有过滤，直接传入php文件一句话木马，

利用蚁剑即可，根目录下有flag

