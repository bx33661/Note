<?php

// 检查并输出 is_numeric 调用的结果
echo "is_numeric(' 36') = " . (is_numeric(' 36') ? 'true' : 'false') . PHP_EOL;
echo "is_numeric('36 ') = " . (is_numeric('36 ') ? 'true' : 'false') . PHP_EOL;
echo "is_numeric('3 6') = " . (is_numeric('3 6') ? 'true' : 'false') . PHP_EOL;

echo "is_numeric(\"\\n36\") = " . (is_numeric("\n36") ? 'true' : 'false') . PHP_EOL;
echo "is_numeric(\"\\t36\") = " . (is_numeric("\t36") ? 'true' : 'false') . PHP_EOL;

echo "is_numeric('36\\n') = " . (is_numeric("36\n") ? 'true' : 'false') . PHP_EOL;
echo "is_numeric('36\\t') = " . (is_numeric("36\t") ? 'true' : 'false') . PHP_EOL;

/*
is_numeric(' 36') = true
is_numeric('36 ') = false
is_numeric('3 6') = false
is_numeric("\n36") = true
is_numeric("\t36") = true
is_numeric('36\n') = false
is_numeric('36\t') = false
 */

?>
