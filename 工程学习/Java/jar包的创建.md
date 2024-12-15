### jar包的创建

> 采用命令行不借助工具

`HelloWorld.java`

```java
package helloword;

/**
 * 第一个 Java 程序
 * 这是初学者基本都会写的一个程序
 * @author bx33661
 * @version 1.0
 */
public class HelloWorld {
    /**
     * 主函数：程序入口
     * @param args 主函数参数列表
     */
    public static void main(String[] args){
        System.out.println("Hello World!");
    }
}
```



```(空)
javac -encoding UTF-8 HelloWorld.java
```

![image-20241215112242074](https://gitee.com/bx33661/image/raw/master/path/image-20241215112242074.png)

```java
jar -cvf hello.jar HelloWorld.class
```

![image-20241215112334984](https://gitee.com/bx33661/image/raw/master/path/image-20241215112334984.png)