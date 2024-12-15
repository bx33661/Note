**使用 `{}` 的 MessageFormat 占位符:**

`java.text.MessageFormat` 类提供了使用花括号 `{}` 作为占位符的方式，这种方式更加灵活，尤其是在处理国际化和本地化时。

- **基本格式:** `String pattern = "String with {0} and {1} parameters";`
    
    - `{n}`: 表示参数列表中的第 n+1 个参数。
- **示例:**
    

```java
import java.text.MessageFormat;

public class MessageFormatExample {
    public static void main(String[] args) {
        String name = "Bob";
        int score = 95;

        String message = MessageFormat.format("Student {0} got a score of {1}.", name, score);
        System.out.println(message); // 输出: Student Bob got a score of 95.

                double price = 123.45;
        String formattedPrice = MessageFormat.format("Price: {0,number,currency}", price);
        System.out.println(formattedPrice); // 输出类似 Price: ￥123.45 (具体货币符号取决于本地设置)

        java.util.Date now = new java.util.Date();
        String formattedDate = MessageFormat.format("Today is {0,date,full}", now);
        System.out.println(formattedDate); // 输出类似 Today is 2024年1月2日 (具体日期格式取决于本地设置)

    }
}
```

**总结:**

- `%` 格式说明符主要用于简单的格式化输出，功能强大，控制灵活，但语法相对复杂。
- `{}` MessageFormat 占位符更适合于需要进行本地化和国际化的场景，可以格式化数字、日期等复杂类型，更易于阅读和维护。


```java
import java.text.MessageFormat;  
import java.util.Scanner;  
  
public class Main {  
    public static void main(String[] args) {  
        String name = "Bx33661";  
        int age = 20;  
        String message = MessageFormat.format("Name: {0}, age: {1}", name, age);  
        System.out.println(message);  
  
        String myPhone = "Huawei";  
        String message2 = MessageFormat.format("My phone band: {0}", myPhone);  
        System.out.println(message2);  
  
        String myPhone2 = "Xiaomi";  
        String message3 = MessageFormat.format("My phone band: {0}", myPhone2);  
        System.out.println(message3);  
  
        String myPhone3 = "Apple";  
        String message4 = MessageFormat.format("My phone band: {0}", myPhone3);  
        System.out.println(message4);  
  
        String myPhone4 = "Samsung";  
        String message5 = MessageFormat.format("My phone band: {0}", myPhone4);  
        System.out.println(message5);  
  
        String myPhone5 = "Oppo";  
        String message6 = MessageFormat.format("My phone band: {0}", myPhone5);  
        System.out.println(message6);  
  
        String myPhone6 = "Vivo";  
        String message7 = MessageFormat.format("My phone band: {0}", myPhone6);  
        System.out.println(message7);  
  
        String myPhone7 = "Nokia";  
        String message8 = MessageFormat.format("My phone band: {0}", myPhone7);  
        System.out.println(message8);  
  
        String myPhone8 = "Motorola";  
        String message9 = MessageFormat.format("My phone band: {0}", myPhone8);  
        System.out.println(message9);  
    }  
}
```