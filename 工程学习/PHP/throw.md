```php
<?php
function divide($num1, $num2) {
    if ($num2 == 0) {
        throw new Exception("不能除以0");
    }
    return $num1 / $num2;
}

try {
    echo divide(10, 0);
} catch (Exception $e) {
    echo '捕获异常 - ',  $e->getMessage(), "\n";
}
?>
```

### 自定义异常
可以通过继承 Exception 类来创建自定义异常类
```php
<?php
class DivisionByZeroException extends Exception {
    public function errorMessage() {
        // 自定义错误信息
        return "错误：除数不能为0。". $this->getMessage();
    }
}

function divide($num1, $num2) {
    if ($num2 == 0) {
        throw new DivisionByZeroException("尝试用0除以一个数。");
    }
    return $num1 / $num2;
}

try {
    echo divide(10, 0);
} catch (DivisionByZeroException $e) {
    echo $e->errorMessage();
}
?>
```