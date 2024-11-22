<?php
// 获取通过 POST 提交的数据
$fname = $_POST['fname'];
$age = $_POST['age'];

// 安全处理输入数据，避免跨站脚本攻击
$fname = htmlspecialchars($fname);
$age = htmlspecialchars($age);

echo "欢迎, " . $fname . "!<br>";
echo "你的年龄是 " . $age . " 岁。";
?>