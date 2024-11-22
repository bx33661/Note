<?php

function validateAndProcess($data) {
    // 检查参数是否为数组
    if (!is_array($data)) {
        return false; // 参数不是数组
    }

    // 检查数组是否为空
    if (empty($data)) {
        return false; // 数组为空
    }

    // 检查数组中的每个元素是否为整数
    foreach ($data as $value) {
        if (!is_int($value)) {
            return false; // 数组包含非整数值
        }
    }

    // 处理逻辑：计算数组中所有整数的和
    $result = array_sum($data);
    return $result;
}

// 测试不同的数组输入
$testArray1 = [1, 2, 3, 4]; // 有效数组
$testArray2 = [1, 2, 'a', 4]; // 包含非整数
$testArray3 = []; // 空数组
$testArray4 = 'not an array'; // 非数组

// 测试并输出结果
var_dump(validateAndProcess($testArray1)); // 输出 int(10)
var_dump(validateAndProcess($testArray2)); // 输出 bool(false)
var_dump(validateAndProcess($testArray3)); // 输出 bool(false)
var_dump(validateAndProcess($testArray4)); // 输出 bool(false)

/*
int(10)
bool(false)
bool(false)
bool(false)
*/

?>
