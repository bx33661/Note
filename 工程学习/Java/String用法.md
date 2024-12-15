
**`String` 的基本概念**

在 Java 中，字符串不是基本数据类型（如 `int`、`char` 等），而是一个对象，属于 `java.lang` 包。这意味着字符串在 Java 中是作为类的实例来处理的。

**创建字符串**

创建字符串主要有两种方式：

1. **直接赋值（字面量方式）:**
    
    Java
    
    ```
    String str = "Hello";
    ```
    
    这是最简单也是最常用的方式。当使用这种方式创建字符串时，JVM 会首先在字符串常量池中查找是否已经存在相同的字符串。如果存在，则直接返回该字符串的引用；如果不存在，则在字符串常量池中创建一个新的字符串对象，并返回其引用。
    
2. **使用 `new` 关键字和构造方法:**
    
    Java
    
    ```
    String str = new String("Hello");
    ```
    
    使用这种方式创建字符串时，会在堆内存中创建一个新的 `String` 对象。即使字符串常量池中已经存在相同的字符串，也会在堆中创建一个新的对象。因此，这种方式会比直接赋值的方式占用更多的内存。
    

**字符串的特性**

- **不可变性（Immutable）:** `String` 对象一旦创建，其值就不能被修改。任何对字符串进行修改的操作，实际上都是创建了一个新的 `String` 对象。例如：
    
    Java
    
    ```
    String str = "Hello";
    str = str + " World"; // 实际上创建了一个新的字符串 "Hello World"
    ```
    
    这种不可变性带来了以下好处：
    
    - **线程安全：** 由于字符串是不可变的，因此在多线程环境下可以安全地共享字符串对象，无需进行额外的同步操作。
    - **提高性能：** 字符串常量池的存在使得相同的字符串可以被多个引用共享，从而减少了内存的占用。
    - **方便哈希计算：** 不可变的特性使得字符串的哈希值在创建后就不会发生改变，因此可以方便地用作哈希表的键。
- **字符串常量池:** JVM 为了提高性能和减少内存占用，维护了一个字符串常量池。使用字面量方式创建的字符串会被存储在这个常量池中。
    

**常用的 `String` 方法**

`String` 类提供了许多有用的方法，以下是一些常用的方法：

- `length()`：返回字符串的长度。
- `charAt(int index)`：返回指定索引处的字符。
- `concat(String str)`：将指定的字符串连接到该字符串的末尾（等价于 `+` 运算符）。
- `equals(Object obj)`：比较字符串与指定的对象是否相等（区分大小写）。
- `equalsIgnoreCase(String str)`：比较字符串与指定的字符串是否相等（不区分大小写）。
- `compareTo(String str)`：按字典顺序比较两个字符串。
- `substring(int beginIndex)`：返回从指定索引开始到字符串末尾的子字符串。
- `substring(int beginIndex, int endIndex)`：返回从指定索引开始到指定索引结束的子字符串（不包括结束索引处的字符）。
- `indexOf(String str)`：返回指定子字符串在该字符串中第一次出现的索引。
- `lastIndexOf(String str)`：返回指定子字符串在该字符串中最后一次出现的索引。
- `replace(char oldChar, char newChar)`：将字符串中所有出现的指定字符替换为新的字符。
- `split(String regex)`：根据给定的正则表达式拆分字符串。
- `trim()`：删除字符串开头和结尾的空白字符。
- `valueOf(Object obj)`：将其他类型的数据转换为字符串。

**`String`、`StringBuilder` 和 `StringBuffer` 的区别**

除了 `String` 类，Java 还提供了 `StringBuilder` 和 `StringBuffer` 类来处理字符串。它们之间的主要区别如下：

- **`String`：** 不可变字符串。适用于字符串操作较少的场景。
- **`StringBuilder`：** 可变字符串，非线程安全。适用于单线程环境下大量的字符串操作。性能比 `StringBuffer` 高。
- **`StringBuffer`：** 可变字符串，线程安全。适用于多线程环境下大量的字符串操作。

通常情况下，如果不需要考虑线程安全问题，建议使用 `StringBuilder` 以获得更好的性能。

**示例代码**

Java

```
public class StringExample {
    public static void main(String[] args) {
        String str1 = "Hello";
        String str2 = "Hello";
        String str3 = new String("Hello");

        System.out.println(str1 == str2); // true，因为 str1 和 str2 指向字符串常量池中的同一个对象
        System.out.println(str1 == str3); // false，因为 str3 在堆中创建了一个新的对象
        System.out.println(str1.equals(str3)); // true，因为 equals() 方法比较的是字符串的内容

        String str4 = "Hello World";
        System.out.println(str4.length()); // 11
        System.out.println(str4.substring(6)); // World

        StringBuilder sb = new StringBuilder("Hello");
        sb.append(" World");
        System.out.println(sb.toString()); // Hello World
    }
}
```

分割
```java
package org.example;  
  
import java.util.ArrayList;  
  
public class Main {  
    public static void main(String[] args) {  
        String demo = "11-22-33";  
        String[] split = demo.split("-");  
        for (String s: split) {  
            System.out.println(s);  
        }  
    }  
}
```