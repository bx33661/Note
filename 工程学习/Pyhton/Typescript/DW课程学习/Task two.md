## Task two

[TOC]

> DataWhale课程学习：https://github.com/datawhalechina/wow-fullstack/tree/main/tutorial/TypeScript
>
> 内容：Task2
>
> 学习者：BX33661

![Working With TypeScript: A Practical Guide for Developers](https://gitee.com/bx33661/image/raw/master/path/TS.png)

### Ts中注释

- `//`
- `/* */`
- `/** * */`文档注释

```typescript
//注释学习
/*
Let‘ go’
*/

/**
 * 计算两个数字的和
 * @param a 第一个数字
 * @param b 第二个数字
 * @returns 两个数字的和
 */
function add(a: number, b: number): number {
    return a + b;
}
```



### 条件语句

- `if`
- `if else`
- `if else if else`
- `switch case`

```typescript
let num1:number = 5

//if-else if-else语句
if(num1<10){
    console.log("small number")
}else if(num1>=10&&num1<=100){
    console.log("medium number")
}else {
    console.log("large number")
}

//switch-case 语句
switch (num1) {
    case 1:
        console.log("数字的值为1")
        break
    case 2:
        console.log("数字的值为2")
        break
    case 3:
        console.log("数字的值为3")
        break
    default:
        console.log("Not found")
        break
}
```



### 循环
#### for循环

```typescript
for ( init; condition; increment ){
    statement(s);
}
```

小例子，阶乘实现

```typescript
let num:number = 5
let result:number = 1
for(let i=1;i<=num;i++){
    result *=i
}
```



#### `for..in` 和`for..of`

- 遍历对象：
  - `for...in` 用于遍历对象的可枚举属性。
  - `for...of` 用于遍历可迭代对象的值。
- 返回值：
  - `for...in` 返回属性名（键）。
  - `for...of` 返回属性值。
- 适用范围：
  - `for...in` 可以遍历普通对象，也可以遍历数组。
  - `for...of` 只能遍历可迭代对象，不能直接遍历普通对象。

```typescript
let nums = [1,2,3,4,5]
for (let i in nums){
    console.log(i)
}
//0,1,2,3,4

let nums = [1,2,3,4,5]
for (let i of nums){
    console.log(i)
}
//1,2,3,4,5
```



#### `every` 和 `some`

`every` 方法用于测试数组中的**每一个元素**是否都通过了由提供的回调函数所实现的测试。如果数组中的所有元素都通过了测试，`every` 返回 `true`，否则返回 `false`。

`some` 方法用于测试数组中是否有**至少一个元素**通过了由提供的回调函数所实现的测试。如果至少有一个元素通过测试，`some` 返回 `true`，否则返回 `false`。

- `every`例子

```typescript
const numbers = [1, 2, 3, 4, 5];
const evennumbers = [2,6,8,10]
//判断数组中是不是所有都是偶数
const hasEven = numbers.every(num => num % 2 === 0);
console.log(hasEven);
// 输出: false
const hasEven2 = evennumbers.every(num => num % 2 === 0);
console.log(hasEven2);
//输出：True
```

- `some`例子

```typescript
const numbers = [1, 2, 3, 4, 5];
//判断是否存在偶数
const hasEven = numbers.some(num => num % 2 === 0);
console.log(hasEven); 
// 输出: true
```



#### `while`和`do..while`循环

while语法：

```typescript
while(condition)
{
   statement(s);
}
```

do..while语法

```typescript
do
{
   statement(s);
}while( condition );
```

斐波那契数列的实现：

```typescript
//while循环学习
//斐波那契数列
function fibonacci(n: number): number {
  let a:number = 1
  let b:number = 1
  while (n > 2) {
    let temp = a + b;
    a = b;
    b = temp;
    n--;
  }
  return b;
}
let result:number = fibonacci(5);
console.log(result)
```

> `break`的使用：
>
> - 出现在循环中，会立刻结束循环，继续流程的下一句
> - 出现在`switch`中，结束一个`case`

```typescript
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break; // 当 i 等于 5 时，退出循环
  }
  console.log(i); // 输出 0 到 4
}

```



> `continue` 的使用
>
> 它是跳出当前循环，进入下一次循环循环

```typescript
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    continue; // 当 i 等于 5 时，跳过本次循环，直接进入下一次循环
  }
  console.log(i); // 输出 0 到 9，除了 5
}

```



### 函数

语法格式

```typescript
function function_name(firstvalue: number, secondvalue?: number) {
    // 执行代码
    return value  //返回
}
```

>- `return`语句，返回值之后，函数就停止执行，基本与其他语言一样
>- 在 TypeScript 函数里，如果我们定义了参数，则我们必须传入这些参数，除非将这些参数设置为可选，可选参数使用问号标识 ,如参数二所示

一个小例子：

```typescript
function greet(person: string): string {
    return `Hello, ${person}!`;
}

let userName: string = "bx";
console.log(greet(userName));

//Hello,bx!
```



#### 反引号

上述例子中使用了 ``  ,用于创建**模板字符串**,感觉有点像python中的f{}

这里利用cluade帮我整理了一下用法：

**插值表达式**
模板字符串可以通过 `${}` 的形式来嵌入表达式或变量。这让我们可以轻松地将变量或表达式的值嵌入到字符串中。

```typescript
let name = "Alice";
let age = 25;
let greeting = `Hello, my name is ${name} and I am ${age} years old.`;
console.log(greeting);
// 输出: Hello, my name is Alice and I am 25 years old.
```

**多行字符串**
模板字符串可以直接跨多行书写，无需像传统字符串那样使用换行符 `\n`。

```typescript
let message = `This is a long message
that spans multiple lines
without using escape characters.`;
console.log(message);
```

**函数和表达式嵌入**
你还可以在 `${}` 中插入任意的 JavaScript 表达式，甚至是函数调用。

```typescript
function add(a: number, b: number): number {
  return a + b;
}

let result = `The sum of 5 and 3 is ${add(5, 3)}.`;
console.log(result);
// 输出: The sum of 5 and 3 is 8.
```

**嵌套模板字符串**
模板字符串可以包含其他模板字符串。

```typescript
let nested = `This is a nested template: ${`Hello, ${name}`}`;
console.log(nested);
```



#### 默认参数

我感觉有点类似于类中的构造函数，格式如下：

```typescript
function function_name(param1[:type],param2[:type] = default_value) { 
}
```

例子如下：（含有默认参数）

```typescript
function greet(person: string = "bbbx"): string {
    return `Hello, ${person}!`;
}
console.log(greet());
```



#### 构造函数

```typescript
var res = new Function ([arg1[, arg2[, ...argN]],] functionBody)
```

教程中的例子

```typescript
var myFunction = new Function("a", "b", "return a * b"); 
var x = myFunction(4, 3); 
console.log(x);

// 12
```

> 但是查了一些资料发现：这种构造函数
>
> **性能问题**：每次调用 `Function` 构造函数时，都会创建一个新的函数对象。这意味着每次调用都会进行函数定义和编译，这比直接调用预定义的函数要慢。
>
> 同时还存在一些**安全问题**



#### lambda 函数

之前在Python中学习过，

> 这样的定义的优点：
>
> 1. **更简洁的语法**：箭头函数允许你以更少的代码来编写函数。
> 2. **隐式返回**：如果函数体只包含一个表达式，则不需要 `return` 关键字，该表达式会自动返回

```typescript
let greet = (name: string) => `Hello, ${name}`;
console.log(greet("bx33661")); 

let add = (a: number, b: number) => a + b;
console.log(add(3, 9)); 

let sayHello = () => console.log("Hello, bx33661!");
sayHello(); 
```

几种写法，有参数和没有参数的，如果需要更复杂的话需要 { }

```typescript
let multiply = (a: number, b: number) => {
    let result = a * b;
    return result;
};
console.log(multiply(9, 3))
```

