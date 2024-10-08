# 认识js原型链

### 构造函数
> 构造函数是一种特殊的函数，用于创建和初始化对象。它通常与 `new` 关键字一起使用。
> 类似于面向对象中类的形式

```javascript
function BBB(){
    this.name = "bbb"
    this.age = 18
}
b = new BBB()
console.log(b)
```
![image.png](https://gitee.com/bx33661/image/raw/master/path/20241006171503.png)



### Object(对象)

> 一种基本的数据类型，用于存储键值对（也称为属性）
> 可以采用两种方法访问对象
> 
> - **点**：`object.property`
> - **方括号**：`object['property']`

```javascript
const Phone = {
    phonename:"Huawei_Mete70",
    price:7999,
    great:function(){
        console.log("Hello Huawei,Hello China!")
    }
}
Phone.great()
console.log(Phone['price'])

//Hello Huawei,Hello China!
//7999
```

> 在读文档的时候总看见例如`[[Prototype]]` 的定义：
>
> 在 JavaScript 中，`[[Prototype]]` 这个表示法中的双括号 `[[` 和 `]]` 是一种特殊的表示方式，用于表示对象的内部属性。这种表示法并不是 JavaScript 语言的一部分，而是 ECMAScript 规范中使用的术语，用于描述对象的内部属性和相关操作。下面是详细的解释：



### 原型和原型链

- **原型**： 每个对象都有一个原型（`prototype`），原型也是一个对象。对象可以通过原型链访问其原型上的属性和方法。

- **原型链**： 对象可以通过原型链访问其原型的原型，直到达到 `null` 为止。

看下面这个例子：三层

```js
var obj = {
    name:"田山",
    age:20
}
obj.__proto__ = {

}
obj.__proto__.__proto__ = {

}
obj.__proto__.__proto__.__proto__ = {
    id:"bx33661"
}

console.log(obj.id); 
```

1. **修改 `obj` 的原型**：

   ```javascript
   obj.__proto__ = {  
   }
   ```

   这行代码将 `obj` 的原型（即 `__proto__` 属性）设置为一个空对象。默认情况下，`obj` 的原型是 `Object.prototype`，但现在它被设置为一个新的空对象。

2. **修改 `obj` 的原型的原型**：

   ```javascript
   obj.__proto__.__proto__ = {  
   }
   ```

   这行代码将 `obj.__proto__` 的原型设置为另一个空对象。此时，`obj` 的原型链如下：

   ```js
   obj -> {} -> {}
   ```

3. **修改 `obj` 的原型的原型的原型**：

   ```javascript
   obj.__proto__.__proto__.__proto__ = {  
      id: "bx33661"  
   }
   ```

   这行代码将 `obj.__proto__.__proto__` 的原型设置为一个包含 `id` 属性的对象。此时，`obj` 的原型链如下：

   ```javascript
   obj -> {} -> {} -> { id: "bx33661" }
   ```
> 

我们在控制台观察

![image-20240925154600685](https://gitee.com/bx33661/image/raw/master/path/image-20240925154600685.png)

> `hasOwnProperty` 方法
>
> `hasOwnProperty` 是 JavaScript 中每个对象继承自 `Object.prototype` 的一个方法。它的主要用途是检查对象自身是否拥有指定的属性，而不考虑原型链上的属性。
>
> **语法**
>
> ```javascript
> obj.hasOwnProperty(prop)
> ```
>
> - **`obj`**：要检查的对象。
> - **`prop`**：要检查的属性名（字符串）。
>
> **返回值**
>
> - **`true`**：如果对象自身拥有指定的属性。
> - **`false`**：如果对象自身没有指定的属性，即使该属性存在于原型链上。



这这个例子中，`obj` 的原型链结构如下：

```js
obj -> {} -> {} -> { id: "bx33661" } -> null
```

原型链的尽头:

1. **`obj`**：这是你创建的对象，它有自己的属性 `name` 和 `age`。
2. **`obj.__proto__`**：这是 `obj` 的原型，一个空对象。
3. **`obj.__proto__.__proto__`**：这是 `obj.__proto__` 的原型，另一个空对象。
4. **`obj.__proto__.__proto__.__proto__`**：这是 `obj.__proto__.__proto__` 的原型，一个包含 `id` 属性的对象。
5. **`obj.__proto__.__proto__.__proto__.__proto__`**：这是 `obj.__proto__.__proto__.__proto__` 的原型，`null`。

> `null` 是原型链的尽头，因为它是JavaScript中表示“没有原型”的特殊值。当对象的原型为 `null` 时，表示这个对象没有原型，原型链到此为止。

