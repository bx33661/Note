## Begin of Upload

![image-20240821104047497](https://gitee.com/bx33661/image/raw/master/path/image-20240821104047497.png)

一道文件上传题，看看代码查看一下过滤情况

---

```javascript
        function validateForm() {
            var fileInput = document.getElementById("file");
            var file = fileInput.files[0];
            var allowedExtensions = ["jpg", "jpeg", "png", "gif"];
            var fileExtension = file.name.split('.').pop().toLowerCase();
            
            if (!file) {
                alert("Please select a file to upload.");
                return false;
            }
            
            if (!allowedExtensions.includes(fileExtension)) {
                alert("错误的拓展名，只允许上传: JPG, JPEG, PNG, GIF");
                return false;
            }
            
            return true;
        }
```

常规步骤，上传+抓包+修改后缀

![image-20240821104157153](https://gitee.com/bx33661/image/raw/master/path/image-20240821104157153.png)

利用中国蚁剑登录

![image-20240821104237203](https://gitee.com/bx33661/image/raw/master/path/image-20240821104237203.png)