<?php

// 开始会话
session_start();

// 检查用户是否通过表单提交用户名
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // 安全处理输入，防止XSS攻击
    $username = htmlspecialchars($_POST['username']);

    // 设置会话变量
    $_SESSION['username'] = $username;

    echo "欢迎, " . $_SESSION['username'] . "!<br>";
    echo "<a href='welcome.php'>转到欢迎页面</a>";
}

