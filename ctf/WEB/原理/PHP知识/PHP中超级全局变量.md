# PHP中超级全局变量

---

在PHP中，超级全局变量是一些内置的变量，它们在所有的作用域中都是可用的，不需要特别声明，也不需要使用全局关键字来访问它们。以下是一些PHP中的超级全局变量：
1. **$GLOBALS**: 包含了所有全局变量的数组。变量的名字作为键名，变量的值作为键值。
2. **$_SERVER**: 包含了服务器和执行环境的信息，如头信息、路径、脚本位置等。
3. **$_GET**: 包含了通过GET方法传递的变量。
4. **$_POST**: 包含了通过POST方法传递的变量。
5. **$_FILES**: 包含了通过POST方法上传的文件信息。
6. **$_REQUEST**: 包含了通过GET、POST和COOKIE传递的变量。
7. **$_SESSION**: 包含了会话变量，用于存储关于用户会话的信息。
8. **$_COOKIE**: 包含了通过COOKIE传递的变量。
9. **$_ENV**: 包含了服务器端的环境变量。
以下是这些超级全局变量的简单说明：
- **$GLOBALS**: 
  ```php
  $var = "Hello world!";
  $GLOBALS['var'] = "Hello again!";
  echo $var; // 输出 "Hello again!"
  ```
- **$_SERVER**: 
  ```php
  echo $_SERVER['SERVER_NAME']; // 输出服务器名称
  ```
- **$_GET**: 
  ```php
  // 假设URL是 index.php?id=123
  echo $_GET['id']; // 输出 123
  ```
- **$_POST**: 
  ```php
  // 假设通过POST方法提交了表单
  echo $_POST['username']; // 输出提交的用户名
  ```
- **$_FILES**: 
  ```php
  echo $_FILES['file']['name']; // 输出上传文件的名字
  ```
- **$_REQUEST**: 
  ```php
  echo $_REQUEST['name']; // 可能是GET、POST或COOKIE中的'name'
  ```
- **$_SESSION**: 
  ```php
  session_start();
  $_SESSION['favcolor'] = 'blue'; // 设置会话变量
  echo $_SESSION['favcolor']; // 输出 'blue'
  ```
- **$_COOKIE**: 
  ```php
  echo $_COOKIE['user']; // 输出cookie中存储的'user'值
  ```
- **$_ENV**: 
  ```php
  echo $_ENV['USERNAME']; // 输出环境变量中的用户名
  ```
  使用这些超级全局变量时，要注意安全性，尤其是当涉及到用户输入时，以防止诸如SQL注入、XSS攻击等安全问题。
  
  ---
  
  ## 一道题目
  
  ```php
  <?php  
  error_reporting(0);
  include "flag1.php";
  highlight_file(__file__);
  if(isset($_GET['args'])){
      $args = $_GET['args'];
      if(!preg_match("/^\w+$/",$args)){
          die("args error!");
      }
      eval("var_dump($$args);");
  }
  ?>
  ```

![image-20240727175344775](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240727175344775.png)