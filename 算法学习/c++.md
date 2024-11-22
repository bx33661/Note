# c++

[TOC]



学习c++的笔记，bx的笔记

## 面向对象编程

OOP（Object-Oriented Programming，面向对象编程）是一种编程范式，它基于以下主要概念：

1. **对象（Object）：** 对象是类的一个实例，具有状态（数据成员）和行为（成员函数）。每个对象都是独立的，可以通过操作对象的行为来修改其状态。
2. **类（Class）：** 类是对象的蓝图或模板，用于定义对象的结构和行为。类定义了对象可以包含的数据成员和成员函数。通过类，可以创建多个相似的对象。
3. **封装（Encapsulation）：** 封装是一种将数据和与数据相关的操作封装在一起的机制，以隐藏对象的内部实现细节。通过将数据成员声明为私有，可以限制对数据的直接访问，而通过公有成员函数提供对数据的控制访问。
4. **继承（Inheritance）：** 继承允许一个类（子类）从另一个类（父类）继承属性和行为。子类可以使用父类的成员，而且还可以添加自己的新成员或修改继承的成员。
5. **多态（Polymorphism）：** 多态性允许一个对象可以被视为多个不同类型的对象。多态性有两种类型：编译时多态（静态多态）和运行时多态（动态多态）。C++ 主要通过函数重载和虚函数来实现多态。

面向对象编程的优点包括：

- **可维护性：** 封装和继承使得代码更容易理解和维护。
- **重用性：** 可以通过继承和多态性实现代码的重用。
- **灵活性：** 对象可以动态地改变其状态和行为，从而实现更灵活的设计。



### 成员和用户：

1. **成员（Member）：** 成员是指属于类的变量和函数，包括数据成员（变量）和成员函数。成员可以是公有的（`public`）、私有的（`private`）或受保护的（`protected`）。

   ```cpp
   class MyClass {
   public:
       int publicMember;  // 公有数据成员
       void publicFunction() {
           // 公有成员函数
       }
   
   private:
       int privateMember;  // 私有数据成员
       void privateFunction() {
           // 私有成员函数
       }
   };
   ```

   在上面的例子中，`publicMember`、`publicFunction`、`privateMember` 和 `privateFunction` 都是成员。

2. **用户（User）：** 用户是指使用类的代码的部分，这可能是程序中的其他类、函数或任何其他能够创建和操作类的对象的部分。用户通过类的公有接口与类进行交互，而不需要知道其内部的实现细节。

   ```cpp
   int main() {
       MyClass myObject;
       myObject.publicFunction();  // 用户通过公有函数与类进行交互
       myObject.publicMember = 42; // 用户通过公有数据成员进行交互
       return 0;
   }
   ```

   在上面的例子中，`main` 函数是类 `MyClass` 的用户，因为它通过类的公有接口与类进行交互。

总体而言，类的成员是类的一部分，包括数据和函数，而用户是那些使用这个类的外部代码或其他类。成员和用户之间的关系是通过类的访问修饰符（`public`、`private`、`protected`）来管理的。

---



### 类（class）

类的成员

- **成员函数（Member Functions）：** 类中定义的函数，可以对类的成员进行操作。
- **成员变量（Member Variables）：** 类中定义的变量，用于存储对象的状态。
- **构造函数（Constructor）：** 特殊的成员函数，在对象创建时自动调用，用于初始化对象的成员。
- **析构函数（Destructor）：** 特殊的成员函数，在对象销毁时自动调用，用于清理资源。

```cpp
class BankAccount {
private://私有
    double balance;

public://公有
    void deposit(double amount) {
        balance += amount;
    }

    void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
        } else {
            cout << "Insufficient funds!" << endl;
        }
    }

    double getBalance() {
        return balance;
    }
};
```

在成员声明为`private`时，只能在类的内部被访问，类的用户无法直接修改和访问这些成员。

**私有成员**------用于“封装”，以保护数据的安全性和隐藏实现的细节。

***

### 构造函数

> 构造函数是一种特殊的成员函数，用于在对象创建时进行初始化。它的名称与类名相同，没有返回类型（包括 void），并且可以有参数。当对象被创建时，构造函数自动调用。构造函数的作用是确保对象被正确地初始化，以便在使用之前它的成员变量具有合适的值。

```cpp
class Point {
private:
    int x, y;

public:
    // 带参数的构造函数
    Point(int initX, int initY) : x(initX), y(initY) {
        // 其他初始化操作
    }
};
```

详情看--->成员初始化列表

***

## 析构函数（Destructor）

> 析构函数是类的另一个特殊成员函数，用于在对象生命周期结束时进行清理工作。析构函数的名称是在类名前面加上波浪号 `~`，它没有参数，也没有返回类型。当对象被销毁时（例如，它超出了作用域或者通过 `delete` 运算符被删除时），析构函数自动调用。









## 规范

**在函数命名时采用“驼峰命名”**



## 成员初始化列表

```cpp
class Point {
private:
    int x, y;

public:
    // 带参数的构造函数，使用成员初始化列表初始化 x 和 y
    Point(int initX, int initY) : x(initX), y(initY) {
        // 在构造函数的函数体中可以进行其他的初始化或操作
        // ...
    }
};
```

`Point(int initX,int initY) :x(initX),y(initY) `    使用`;`来初始化成员变量

