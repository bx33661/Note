## Task two

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

