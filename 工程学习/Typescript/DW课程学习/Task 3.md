# Task 3

[TOC]

---

> DataWhale教程：https://github.com/bx33661/TS-/blob/main/tutorial/TypeScript/%E7%AC%AC3%E7%AB%A0-ts%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B/TypeScript%E6%95%99%E7%A8%8B3-%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B.md
>
> author：bx33661

在 TypeScript（简称 TS）中，数据类型用于定义变量、函数参数、返回值等的类型。TypeScript 是 JavaScript 的超集，因此它继承了 JavaScript 的所有数据类型，并增加了一些额外的类型来增强类型检查和代码的可维护性。以下是 TypeScript 中常见的数据类型：

## 基本数据类型（Primitive Types）

- **`number`**: 表示数字，包括整数和浮点数。
  
  ```typescript
  let age: number = 25;
  ```
  
- **`string`**: 表示字符串，可以使用单引号、双引号或反引号（模板字符串）。
  
  ```typescript
  let name: string = "Alice";
  ```
  
- **`boolean`**: 表示布尔值，只有两个值：`true` 和 `false`。
  ```typescript
  let isStudent: boolean = true;
  ```

- **`null`**: 表示空值或不存在的值。
  ```typescript
  let empty: null = null;
  ```

- **`undefined`**: 表示未定义的值。
  ```typescript
  let notDefined: undefined = undefined;
  ```

- **`symbol`**: 表示唯一的、不可变的值，通常用作对象属性的键。
  
  ```typescript
  let sym: symbol = Symbol("key");
  ```

### 2. 特殊类型
- **`any`**: 表示任意类型，可以赋值为任何类型的值。使用 `any` 会关闭类型检查，应谨慎使用。
  ```typescript
  let dynamicValue: any = 42;
  dynamicValue = "Hello";
  ```

- **`unknown`**: 类似于 `any`，但更安全。在使用 `unknown` 类型的值之前，必须进行类型检查或类型断言。
  ```typescript
  let unknownValue: unknown = 42;
  if (typeof unknownValue === "number") {
    let num: number = unknownValue;
  }
  ```

- **`void`**: 表示没有返回值的函数的返回类型。通常用于函数没有返回值的情况。
  ```typescript
  function logMessage(message: string): void {
    console.log(message);
  }
  ```

- **`never`**: 表示永远不会发生的值的类型。通常用于永远不会返回的函数（如抛出异常的函数）。
  ```typescript
  function throwError(message: string): never {
    throw new Error(message);
  }
  ```



## Number类型

这个类型基本都是常规的进制，运算等操作，但是ts中含有许多的内置的方法，下面是跟着教程操作的例子：

```typescript
let num: number = 42.123456;

// toFixed 方法：将数字转换为指定小数位数的字符串
let fixedNum = num.toFixed(2);
console.log(`toFixed: ${fixedNum}`); // 输出: toFixed: 42.12

// toPrecision 方法：将数字转换为指定有效数字位数的字符串
let precisionNum = num.toPrecision(4);
console.log(`toPrecision: ${precisionNum}`); // 输出: toPrecision: 42.12

// toExponential 方法：将数字转换为指数表示法的字符串
let exponentialNum = num.toExponential(2);
console.log(`toExponential: ${exponentialNum}`); // 输出: toExponential: 4.21e+1

// toString 方法：将数字转换为字符串
let strNum = num.toString();
console.log(`toString: ${strNum}`); // 输出: toString: 42.123456

// valueOf 方法：返回数字的原始值
let valueOfNum = num.valueOf();
console.log(`valueOf: ${valueOfNum}`); // 输出: valueOf: 42.123456

// isFinite 方法：判断数字是否为有限数
let isFiniteNum = Number.isFinite(num);
console.log(`isFinite: ${isFiniteNum}`); // 输出: isFinite: true

// isNaN 方法：判断数字是否为 NaN
let isNaNNum = Number.isNaN(num);
console.log(`isNaN: ${isNaNNum}`); // 输出: isNaN: false

// isInteger 方法：判断数字是否为整数
let isIntegerNum = Number.isInteger(num);
console.log(`isInteger: ${isIntegerNum}`); // 输出: isInteger: false

// parseFloat 方法：将字符串转换为浮点数
let strFloat = "42.123456";
let parsedFloat = Number.parseFloat(strFloat);
console.log(`parseFloat: ${parsedFloat}`); 
// 输出: parseFloat: 42.123456

// parseInt 方法：将字符串转换为整数
let strInt = "42";
let parsedInt = Number.parseInt(strInt, 10);
console.log(`parseInt: ${parsedInt}`); // 输出: parseInt: 42

// MAX_VALUE 和 MIN_VALUE 属性：表示 Number 类型的最大值和最小值
console.log(`MAX_VALUE: ${Number.MAX_VALUE}`); // 输出: MAX_VALUE: 1.7976931348623157e+308
console.log(`MIN_VALUE: ${Number.MIN_VALUE}`); // 输出: MIN_VALUE: 5e-324

// POSITIVE_INFINITY 和 NEGATIVE_INFINITY 属性：表示正无穷和负无穷
console.log(`POSITIVE_INFINITY: ${Number.POSITIVE_INFINITY}`); // 输出: POSITIVE_INFINITY: Infinity
console.log(`NEGATIVE_INFINITY: ${Number.NEGATIVE_INFINITY}`); // 输出: NEGATIVE_INFINITY: -Infinity

// NaN 属性：表示非数字值
console.log(`NaN: ${Number.NaN}`); // 输出: NaN: NaN
```





## 数组

> 在 TypeScript 中，数组是一种常见的数据结构，用于存储多个相同类型的元素

操作十分多，这里通过一个例子走一遍,输出结果都在注释中

```typescript
// 定义一个数组
let numbers: number[] = [1, 2, 3, 4, 5];

// 访问数组元素
console.log(numbers[0]); // 输出: 1
console.log(numbers[2]); // 输出: 3

// 修改数组元素
numbers[1] = 10;
console.log(numbers); // 输出: [1, 10, 3, 4, 5]

// 添加元素
numbers.push(6); // 在末尾添加元素
numbers.unshift(0); // 在开头添加元素
console.log(numbers); // 输出: [0, 1, 10, 3, 4, 5, 6]

// 删除元素
let lastNumber = numbers.pop(); // 删除并返回最后一个元素
let firstNumber = numbers.shift(); // 删除并返回第一个元素
console.log(numbers); // 输出: [1, 10, 3, 4, 5]
console.log(lastNumber); // 输出: 6
console.log(firstNumber); // 输出: 0

// 数组的长度
console.log(numbers.length); // 输出: 5

// 遍历数组
// 使用 for 循环
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}

// 使用 forEach 方法
numbers.forEach(num => {
  console.log(num);
});

// 使用 for...of 循环
for (let num of numbers) {
  console.log(num);
}

// 多维数组
let matrix: number[][] = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];
console.log(matrix[0][1]); // 输出: 2

//切片操作
let arr: number[] = [1, 2, 3, 4, 5];
let slicedArr = arr.slice(1, 4);
console.log(slicedArr); // 输出 [2, 3, 4]
```

还有经过了解，还有一些特殊的数组

```typescript
// 数组的联合类型
let mixedArray: (number | string)[] = [1, "Alice", 2, "Bob"];
console.log(mixedArray); // 输出: [1, "Alice", 2, "Bob"]

// 只读数组
let readonlyNumbers: ReadonlyArray<number> = [1, 2, 3];
// readonlyNumbers.push(4); // 错误: 只读数组不能修改

// 数组的解构赋值
let [first, second, third] = numbers;
console.log(first); // 输出: 1
console.log(second); // 输出: 10
console.log(third); // 输出: 3
```



## Map对象

> `Map` 是一种用于存储键值对的数据结构,之前学习算法见过这种数据类型

创建方式

```typescript
// 方法一
let myMap = new Map<string, number>();
// 方法二
let anotherMap = new Map<string, number>([
  ["four", 4],
  ["five", 5],
  ["six", 6]
]);
```

用一个例子过一遍常规操作

```typescript
// 创建一个 Map 对象
let myMap = new Map<string, number>();

// 添加键值对
myMap.set("one", 1);
myMap.set("two", 2);
myMap.set("three", 3);

// 获取值
console.log(myMap.get("one")); // 输出: 1
console.log(myMap.get("two")); // 输出: 2

// 检查键是否存在
console.log(myMap.has("one")); // 输出: true
console.log(myMap.has("four")); // 输出: false

// 删除键值对
myMap.delete("two");
console.log(myMap.has("two")); // 输出: false

// 获取 Map 的大小
console.log(myMap.size); // 输出: 2

// 清空 Map
myMap.clear();
console.log(myMap.size); // 输出: 0

// 合并两个 Map
let mergedMap = new Map([...myMap, ...anotherMap]);
```

进行遍历操作，有点想Python对字典的操作

```typescript
// 创建一个键值对
let myMap = new Map<string, number>();
myMap.set("one", 1);
myMap.set("two", 2);
myMap.set("three", 3);

// 遍历 Map
// 使用 for...of 循环
for (let [key, value] of myMap) {
  console.log(`Key: ${key}, Value: ${value}`);
}

// 使用 forEach 方法
myMap.forEach((value, key) => {
  console.log(`Key: ${key}, Value: ${value}`);
});
```

Ts中map对象的特性

> Map的键可以是任何类型的值（包括函数、对象或任何原始值），而普通的JavaScript对象（包括TypeScript中的对象）的键只能是字符串或Symbol。

```
// 使用不同类型的键
let objKey = { key: "objKey" };
let arrKey = [1, 2, 3];

let mixedMap = new Map<any, string>();
mixedMap.set(objKey, "Object Key");
mixedMap.set(arrKey, "Array Key");

console.log(mixedMap.get(objKey)); // 输出: Object Key
console.log(mixedMap.get(arrKey)); // 输出: Array Key
```

