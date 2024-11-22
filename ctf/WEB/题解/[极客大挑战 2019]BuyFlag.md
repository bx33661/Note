## [极客大挑战 2019]BuyFlag

---

![image-20240603174318768](https://gitee.com/bx33661/image/raw/master/path/image-20240603174318768.png)

F12审计代码发现：

```php
	~~~post money and password~~~
if (isset($_POST['password'])) {
	$password = $_POST['password'];
	if (is_numeric($password)) {
		echo "password can't be number</br>";
	}elseif ($password == 404) {
		echo "Password Right!</br>";
	}
}
```

需要传递两个参数money和password

> money = 100000000
>
> password = 404a

*构造payload：* password=404a&money=100000000

![image-20240603181531107](https://gitee.com/bx33661/image/raw/master/path/image-20240603181531107.png)

注意到这一点==you must be a student from CUIT!!!==

检查cookie：![image-20240603181708388](https://gitee.com/bx33661/image/raw/master/path/image-20240603181708388.png)

改为“1”：

![image-20240603181733079](https://gitee.com/bx33661/image/raw/master/path/image-20240603181733079.png)

成功得到flag
