## Task one

[TOC]

![下载](C:/Users/lenovo/Desktop/%E4%B8%8B%E8%BD%BD.png)

> TypeScript 官网: https://www.typescriptlang.org/
>
> DataWhale课程地址：https://github.com/datawhalechina/wow-fullstack/tree/main/tutorial/TypeScript
>
> 根据datawhale课程学习~~~

### 配置环境

#### 线上运行学习

![](https://gitee.com/bx33661/image/raw/master/path/image-20240916124828432.png)

https://www.typescriptlang.org/zh/play/

#### 本地配置

1. 安装Node.js环境 ：https://nodejs.org/zh-cn

2. npm安装TypeScipt

```bash
npm install -g typescript
#会下载并安装 TypeScript 编译器（tsc）到你的系统中，使你可以在任何地方使用 tsc 命令。
```

3. 验证安装

```bash
tsc -v
```

![image-20240916130719767](https://gitee.com/bx33661/image/raw/master/path/image-20240916130719767.png)

4. 在vscode编写

安装TypeScript的插件

![image-20240916130939387](https://gitee.com/bx33661/image/raw/master/path/image-20240916130939387.png)

在终端中运行,初始化

```
npx tsc --init
```

创建一个`demo.ts`文件

> `TypeScript`文件最后都要编译成`JavaScript`文件

```typescript
//demo.ts
function say(world:string){
    console.log(world);
}
say('hello world!');
```

```bash
tsc demo1.ts
```

![image-20240916131153070](https://gitee.com/bx33661/image/raw/master/path/image-20240916131153070.png)

```javascript
//demo.js
function say(world) {
    console.log(world);
}
say('hello world!');
```



### TypeScript基本语法

#### 变量声明

```typescript
var [变量名] : [类型] = 值;
```

```typescript
//变量声明
//标准式
var bxname:string = "bx33661"

//没有初始值,这种声明指定了变量的类型，但没有赋初始值。在使用这个变量之前，你需要为其赋值，否则可能会导致未定义的行为。
var bx1:string

//没有设置变量类型
//TypeScript 会根据赋值自动推断类型
var bx2:string = "bx33661"
```

> 需要注意的是一旦变量被赋予一个值，TypeScript 就会推断其类型，之后就不能将其他类型的值赋给这个变量了。

*常量：*（使用`const`关键字）

```typescript
const bx3 = "hello";
```



#### 变量作用域

```typescript
var global_num = 12          // 全局变量
class Numbers { 
   num_val = 13;             // 实例变量
   static sval = 10;         // 静态变量
   
   storeNum():void { 
      var local_num = 14;    // 局部变量
   } 
} 
console.log("全局变量为: "+global_num)  
console.log(Numbers.sval)   // 静态变量
var obj = new Numbers(); 
console.log("实例变量: "+obj.num_val)
```



### 运算符

跟其他语言差不多，我就跟着例子过一遍

```typescript
var num1:number = 3
var num2:number = 7

console.log("加法:"+(num1+num2))
console.log("减法"+(num2-num1))
console.log("乘法"+(num1*num2))
console.log("除法"+(num2/num1))
console.log("取余"+(num2%num1))
//自增运算
console.log(num1)
num1++
console.log(num1)
//自减运算
console.log(num2)
num2--
console.log(num2)
//字符串
var str1:string = "hello"
var str2:string = "world"
console.log(str1+str2)
```

```
[LOG]: "加法:10" 
[LOG]: "减法4" 
[LOG]: "乘法21" 
[LOG]: "除法2.3333333333333335" 
[LOG]: "取余1" 
[LOG]: 3 
[LOG]: 4 
[LOG]: 7 
[LOG]: 6 
[LOG]: "helloworld" 
```

> 在处理字符串的时候，可以直接采用`+` ，将两个字符串拼接在一起

#### 关系运算符号

```typescript
//关系运算符号
var num1:number = 3
var num2:number = 7

//这里我们定义bi存储结果
var b1:boolean = num1>num2
console.log(b1)

var b2:boolean = num1<num2
console.log(b2)

var b3:boolean = num1>=num2
console.log(b3)

var b4:boolean = num1<=num2
console.log(b4)

var b5:boolean = num1==num2
console.log(b5)

var b6:boolean = num1!=num2
console.log(b6)
```

```
[LOG]: false 
[LOG]: true 
[LOG]: false 
[LOG]: true 
[LOG]: false 
[LOG]: true 
```



#### 逻辑运算

- `&&` 逻辑与
- `||` 逻辑或
- `!` 非



`typeof` 函数：

```typescript
var num1:number = 1
console.log(typeof(num1))

//"number"
```



### 其他

关于ts是否后面加`;`的问题，由于我没有参加过写项目的经验所以在网上找了一些文章

> 关于**ASI**:TypeScript, JavaScript 一样，有自动分号插入机制。这意味着在大多数情况下，即使你不写分号，TypeScript 也会在编译时自动插入它们。

看了一些人的分享，可能有时候不加分号会出现一些问题，但加不加`;`主要还是取决于团队开发风格