# Task4

---

<img src="https://gitee.com/bx33661/image/raw/master/path/ts_logo.BstCNrTU_1Dbxpr.webp" alt="TypeScript" style="zoom: 50%;" />

> DataWhale：https://github.com/bx33661/TS-/blob/main/tutorial/TypeScript/%E7%AC%AC4%E7%AB%A0-ts%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1/Typescript%E6%95%99%E7%A8%8B4.4-%E6%B3%9B%E5%9E%8B.md
>
> Author：bx33661

[TOC]

## 接口

```typescript
//接口
//需要注意接口不能转换为 JavaScript。 它只是 TypeScript 的一部分。
//amanimal是一个接口，接口是一种规范的定义，定义了某一类对象应该有的属性和方法
interface Animal{
    name:string;
    age:number;
    gender:string;
    speak():void;
}

//定义一个对象时，可以指定它的类型为Animal，这样就限制了这个对象的属性和方法，必须符合Animal接口的定义
let dog:Animal = {
    name:'田山',
    age:3,
    gender:'公',
    speak:():string => {
        return '汪汪汪'
    }
}
console.log(dog.speak())
console.log(dog.name)
```

 

联合类型的应用：

```typescript
//联合类型应用
interface P {
    program:string
    command:string[]|string|(()=>string)
}
```

`commandline` 属性是一个联合类型，表示它可以是以下三种类型之一

- **`string[]`**: 一个字符串数组，表示命令行参数的列表。
- **`string`**: 一个字符串，表示整个命令行字符串。
- **`() => string`**: 一个返回字符串的函数，表示动态生成命令行字符串的函数。

意思就是表示它可以是 `string[]`、`string` 或 `() => string` 中的任意一种。



```typescript
interface namel{
    [index:number]:string
}

let list2:namel = ['Python','JavaScript','TypeScript']
console.log(list2[0])
```

这里主要分析一下这个接口语法

`[index: number]: string;` 是一种索引签名（Index Signature），用于定义对象的键值对类型。通俗来讲它规范这个键类型是number类型，值类型是string

那么我们接着一个测试

```typescript
interface  name2{
    [index:string]:string
}
let list3:name2 = {
    'name':'Python',
    'name2':'JavaScript',
    'name3':'TypeScript'
}
console.log(list3['name'])
```

这样一对比就可以清楚，这个键值类型就明白了

### 接口继承

一个例子：（单继承）

```typescript
interface Preson {
    name: string
    age: number
    gender: '男' | '女'
}

interface Student extends Preson {
    grade: number
}

let student: Student = {
    name: '田山',
    age: 18,
    gender: '男',
    grade: 1
}

console.log(student) // { name: '小明
```

> `gender: '男' | '女'` 这里做了一个语法限制，这个量是'男' 或 ‘女’

还可以多继承

```typescript
//多继承
interface Preson_name {
    name: string
}

interface Preson_age {
    age: number
}

interface Preason extends Preson_age,Preson_name{
    gender: '男' | '女'
}

let man: Preason = {
    name: '田山',
    age: 18,
    gender: '男'
}

console.log(man)
```



## 类

与其他语言一样

```typescript
class Python {
    //类的属性
    version: number;
    //构造函数
    constructor(version: number) {
        this.version = version;
    }

    getVersion() {
        console.log('Python' + this.version);
    }
}

let py = new Python(3.8);
py.getVersion(); 
```

在这个例子中，借助构造函数，我们可以为为我们实例

确定Python版本

### 类的继承

刚初步了解接口的继承，开始了解类的继承

```typescript
//类的继承
class language {
    name: string;
    constructor(name: string) {
        this.name = name;
    }
    getName(){
        return `This language is ${this.name}`;
    }
}

class python extends language {
    ver:number
    constructor(ver:number) {
        super('Python');
        this.ver = ver;
    }
    getName() {
        return `This is language is Python`;
    }
    getVersion(): string {
        return `This is Python ${this.ver}`;
    }
}

let myPython = new python(3.7);
console.log(myPython.getName());
console.log(myPython.getPython());
```

> 需要注意的是，在接口那部分我们可以继承多个接口，但是对于类而言，它只能继承一个父类
>
> “它只有一个爸爸”🙂

- 还是采用关键词`extends`去继承,上面这个例子可以很好说明

- 采用`new`语法创建一个实例

- 同时需要访问实例的属性或者方法需要使用 ` . ` 

谈到继承我们就要说关于方法的重写,对于上述例子，这个getName()方法就是被重写了

```typescript
   getName() {
        return `This is language is Python`;
    }
```

> 同时在子类中，你可以使用 `super` 关键字来调用父类中的方法。这在需要扩展父类方法的行为时非常有用

使用super之后，我们可以在父类基础之上去添加更多内容！



### 静态

使用关键词`static` 可以定义类中的静态属性和方法，这些静态属性和方法可以直接通过类型名称来直接调用

```typescript
class BYD{
    static carName = 'BYD';
    static getCarName():void{
        console.log("I love " + BYD.carName);
    }
}
BYD.getCarName(); // BYD
console.log(BYD.carName)
```

```
I love BYD
BYD
```



### 访问控制符

```typescript
class Phone {
    public region: string;
    private name: string;
    private price: number;
    constructor(name: string, price: number,region: string){
        this.region = region;
        this.name = name;
        this.price = price;
    }
    public getName(): string {
        return this.name;
    }
    public getPrice(): number {
        return this.price;
    }
}
let phone = new Phone('Huawei Meta 70',6999, 'China');
console.log(phone.getName());
console.log(phone.getPrice());

console.log(phone.region);

//下面这两个会报错！
console.log(phone.name);
console.log(phone.price);
```

> - public（默认） : 公有，可以在任何地方被访问。
> - protected : 受保护，可以被其自身以及其子类访问。
> - private : 私有，只能被其定义所在的类访问

这样访问修饰符号的出现可以保证变量数据安全



### instanceof 运算符

> `instanceof` 运算符是 TypeScript（和 JavaScript）中的一个关键字，用于检查一个对象是否是某个类的实例.
>
> 返回值是True or False

```typescript
class Animal {
    name: string;

    constructor(name: string) {
        this.name = name;
    }
}

class Dog extends Animal {
    breed: string;

    constructor(name: string, breed: string) {
        super(name);
        this.breed = breed;
    }
}

class Cat extends Animal {
    color: string;

    constructor(name: string, color: string) {
        super(name);
        this.color = color;
    }
}
let animal = new Animal('张三');
let dog = new Dog('李四', '拉布拉多');
let cat = new Cat('王五', 'White');

console.log(animal instanceof Animal); // 输出: true
console.log(dog instanceof Animal); // 输出: true
console.log(cat instanceof Animal); // 输出: true

console.log(animal instanceof Dog); // 输出: false
console.log(animal instanceof Cat); // 输出: false

console.log(dog instanceof Dog); // 输出: true
console.log(dog instanceof Cat); // 输出: false

console.log(cat instanceof Dog); // 输出: false
console.log(cat instanceof Cat); // 输出: true
```



### 类实现接口

这里我举一个例子，定义一个game，然后用Baskerball类去implements它

```typescript
//类实现接口
interface Game{
    name:string;
    player:string;
    play():void;
}

class Basketball implements Game{
    name = 'Basketball';
    player = '5';
    play(){
        console.log(`I love ${this.name}, ${this.player} players in a team.`);
    }
}

let basketball = new Basketball();
basketball.play(); // I love Basketball, 5 players in a team.
console.log(basketball.name); // Basketball
console.log(basketball.player); // 5
```

> deepseek告诉我为啥要这样实现
>
> - **实现接口** 意味着类必须提供接口中定义的所有属性和方法。
> - **语法**: 使用 `implements` 关键字，后跟接口名称。
> - **好处**: 提高类型安全、代码可读性和可扩展性。
> - **多个接口**: 一个类可以实现多个接口，通过逗号分隔接口名称。
>
> 通过实现接口，你可以确保类的结构和行为符合预期，从而提高代码的质量和可维护性



## 对象（Object）

```typescript
let langauge_program = {
    name1: "cpp", // 字符串类型
    name2: "java", // 字符串类型
    name3: "python", // 字符串类型
    name4: "javascript", // 字符串类型
    name5: "typescript", // 字符串类型
    version: 3.14, // 数字类型
    isPopular: true, // 布尔类型
    features: ["OOP", "Functional Programming", "Strong Typing"], // 数组类型
    dependencies: { // 对象类型
        library1: "React",
        library2: "Angular",
        library3: "Vue.js"
    }
};

//访问对象的值
console.log(langauge_program.name1);
console.log(langauge_program.name2);
console.log(langauge_program.name3);
```

我这这个例子中定义了一个`langauge_program`对象，其中有各种类型的属性

> - **对象** 可以包含不同类型的属性，包括字符串、数字、布尔值、数组、对象等。
> - 通过对象，你可以存储和访问不同类型的数据。

```typescript
function sayName(name: string) {
    return 'Hello, ' + name;
}
//将对象作为参数
console.log(sayName(langauge_program.name3)); 
```



### 添加新属性

```typescript
langauge_program.newProperty = "New Value";

// 输出: New Value
console.log(langauge_program.newProperty); 
```

> 使用扩展运算符（Spread Operator）
>
> 扩展运算符 `...` 可以将一个对象的属性展开到另一个对象中。
>
> ```typescript
> // 添加新属性
> langauge_program = {
>     ...langauge_program,
>     newProperty: "New Value"
> };
> ```
>
> 



## 泛型

> 这个东西还真不熟悉，感觉有点像cpp中的模板

> 泛型（Generics）是 TypeScript 中一个非常强大的特性，它允许你编写可以在多种类型上工作的代码，而不需要为每种类型编写单独的实现。泛型提供了一种方式来创建可重用的组件，这些组件可以处理多种类型的数据。

泛型的语法：

```
泛型的语法通常使用尖括号 <> 来定义类型参数。类型参数可以是任何有效的标识符，通常使用 T、U、V 等大写字母来表示
```

### 泛型函数

不管了，先写一个例子，根据结果来分析

```typescript
function identity<T>(arg:T):T {
    return arg;
}

let output = identity<string>('myString');
console.log(output); // myString
let output2 = identity<number>(100);
console.log(output2); // 100
```

```typescript
myString
100
```

**泛型函数 `identity`**:

- 使用类型参数 `T` 来表示参数和返回值的类型。
- 函数 `identity` 接受一个参数 `arg`，并返回该参数

例如第一个例子：当调用泛型函数的时候，`T` 此时为`string`，`arg` = `myString`



### 泛型类

```typescript
class GenericBox<T> {
    private _content: T;

    constructor(content: T) {
        this._content = content;
    }

    public getContent(): T {
        return this._content;
    }

    public setContent(content: T): void {
        this._content = content;
    }
}

// 使用泛型类
let stringBox = new GenericBox<string>('Hello, World!');
console.log(stringBox.getContent()); // Hello, World!

let numberBox = new GenericBox<number>(123);
console.log(numberBox.getContent()); // 123
```

一个泛型类的例子，

- 这个例子中定义了一个泛型类 `GenericBox<T>`
  - 使用类型参数 `T` 来表示类的属性和方法的类型。
  - `private _content: T;`：定义了一个私有属性 `_content`，类型为 `T`。
  - `constructor(content: T)`：构造函数接受一个参数 `content`，类型为 `T`，并将其赋值给 `_content` 属性。
  - `public getContent(): T`：定义了一个公共方法 `getContent`，返回 `_content` 属性的值。
  - `public setContent(content: T): void`：定义了一个公共方法 `setContent`，接受一个参数 `content`，类型为 `T`，并将其赋值给 `_content` 属性。