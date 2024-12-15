### 重写
```java
package org.example;  
  
public class Main {  
    public static void main(String[] args) {  
        Phone phone = new Huawei(); // Assuming Pet interacts with a phone  
        String message = callPhone(phone, "bx"); // Assuming Call method sends a command  
        System.out.println(message);  
    }  
  
    private static String callPhone(Phone phone, String command) {  
        // Implement logic to send command to the phone (e.g., network communication)  
        return phone.sayBand(command); // Assuming callPhone returns a response  
    }  
}  
  
class Phone {  
    public String name; // Assuming a generic phone class  
  
    public String sayBand(String command) {  
        return "Phone response: " + command;  
    }  
}  
  
class Huawei extends Phone {  
    public String name = "Huawei";  
  
    @Override  
    public String sayBand(String command) {  
        return super.sayBand(command) + " (from Huawei)";  
    }  
}
```


### 重载
class calc
```java
package org.example;  
  
 public class calc {  
    // Method overloading  
    public int sum(int a, int b) {  
        return a + b;  
    }  
    public int sum(int a, int b, int c) {  
        return a + b + c;  
    }  
    public int sum(int a, int b, int c, int d) {  
        return a + b + c + d;  
    }  
    public double sum(double a, double b) {  
        return a + b;  
    }  
}
```

Main.java
```java
package org.example;  
  
public class Main {  
    public static void main(String[] args) {  
        calc c = new calc();  
        System.out.println(c.sum(1, 2, 3, 4));  
        System.out.println(c.sum(1.2,3.4));  
        System.out.println(c.sum(1,2));  
    }  
}
```

> 输出结果如下：
> "C:\Program Files\Java\jdk-17\bin\java.exe" "-javaagent:E:\BaiduNetdiskDownload\IntelliJ IDEA 2024.2.4\lib\idea_rt.jar=47024:E:\BaiduNetdiskDownload\IntelliJ IDEA 2024.2.4\bin" -Dfile.encoding=UTF-8 -classpath E:\java\JavaStudy\target\classes org.example.Main
10
4.6
3