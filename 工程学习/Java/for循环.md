for循环
```java
for(初始条件;终止条件;更新语句){
    循环语句;
}
```



Java5之后引入增强for
```java
public class Main {  
    public static void main(String[] args) {  
        int[] nums = {1, 2, 3, 4, 5};  
        for (int i : nums){  
            System.out.println(i);  
        }  
    }  
}
```