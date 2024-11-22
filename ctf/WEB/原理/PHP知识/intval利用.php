<?php

// 输出 intval 调用的结果
echo "intval('1146.0') = " . intval('1146.0') . PHP_EOL;
echo "intval('1146.123') = " . intval('1146.123') . PHP_EOL;
echo "intval('1146aa') = " . intval('1146aa') . PHP_EOL;

echo "intval('1146e123') = " . intval('1146e123') . PHP_EOL;

echo "intval('0x117c', 0) = " . intval('0x117c', 0) . PHP_EOL;
echo "intval('010574', 0) = " . intval('010574', 0) . PHP_EOL;

echo "intval(' 1146') = " . intval(' 1146') . PHP_EOL;
?>
