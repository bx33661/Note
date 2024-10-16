<?php
$str = "Hello, World!";
$hash = sha1($str);
$hash1 = sha1("China");

// 正确的计算空数组的 SHA-1 哈希值
$nums = array();
$hash_array = sha1(implode('', $nums)); // 或者直接使用 sha1('')

echo "SHA-1 hash of '$str' is: $hash\n";
echo "SHA-1 hash of 'China' is: $hash1\n";
echo "SHA-1 hash of an empty array is: $hash_array\n";
?>

