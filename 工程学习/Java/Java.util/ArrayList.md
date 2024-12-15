`ArrayList` 是 Java 中的一种动态数组类，属于 `java.util` 包。与普通的数组不同，`ArrayList` 的大小是可变的，能够动态地增加或减少元素。它实现了 `List` 接口，支持所有的列表操作。

### **主要特性**

1. **动态大小**  
    `ArrayList` 会根据需要动态调整大小（自动扩容），无需手动管理数组长度。
    
2. **顺序存储**  
    底层使用数组实现，元素按插入顺序存储。
    
3. **随机访问**  
    由于是基于数组实现的，`ArrayList` 支持通过索引快速访问元素，访问时间复杂度为 O(1)O(1)。
    
4. **允许重复**  
    可以存储重复的元素。
    
5. **非线程安全**  
    `ArrayList` 不是线程安全的。如果在多线程环境中使用，需要手动同步。
    

---

### **基本操作**

1. **创建一个 ArrayList**
    
    ```java
    import java.util.ArrayList;
    
    public class Main {
        public static void main(String[] args) {
            ArrayList<String> list = new ArrayList<>(); // 创建一个 ArrayList
        }
    }
    ```
    
2. **添加元素**
    
    - 使用 `add()` 方法：
        
        ```java
        list.add("A");
        list.add("B");
        list.add(1, "C"); // 在索引 1 插入 "C"
        ```
        
3. **获取元素**
    
    - 使用 `get()` 方法：
        
        ```java
        String element = list.get(0); // 获取索引 0 的元素
        ```
        
4. **更新元素**
    
    - 使用 `set()` 方法：
        
        ```java
        list.set(1, "D"); // 更新索引 1 的元素为 "D"
        ```
        
5. **删除元素**
    
    - 使用 `remove()` 方法：
        
        ```java
        list.remove(1); // 删除索引 1 的元素
        list.remove("A"); // 删除值为 "A" 的元素
        ```
        
6. **遍历元素**
    
    - 使用 `for-each` 循环：
        
        ```java
        for (String item : list) {
            System.out.println(item);
        }
        ```
        
    - 使用迭代器：
        
        ```java
        Iterator<String> iterator = list.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
        ```
        
7. **获取大小**
    
    - 使用 `size()` 方法：
        
        ```java
        int size = list.size(); // 获取 ArrayList 的大小
        ```
        
8. **检查元素是否存在**
    
    - 使用 `contains()` 方法：
        
        ```java
        boolean exists = list.contains("A");
        ```
        

---

### **底层实现**

- `ArrayList` 底层是一个动态数组，默认初始容量为 10。
- 当容量不足时，`ArrayList` 会以 1.5×当前容量1.5 \times \text{当前容量} 的速率增长（创建一个更大的数组并将旧数据复制到新数组中）。

---

### **常用方法总结**

|方法|描述|
|---|---|
|`add(E e)`|添加元素到列表末尾|
|`add(int index, E e)`|在指定索引插入元素|
|`get(int index)`|获取指定索引的元素|
|`set(int index, E e)`|替换指定索引的元素|
|`remove(int index)`|删除指定索引的元素|
|`remove(Object o)`|删除第一次出现的指定元素|
|`size()`|返回元素数量|
|`isEmpty()`|检查列表是否为空|
|`contains(Object o)`|检查列表是否包含指定元素|
|`clear()`|清空所有元素|

---

### **注意事项**
1. **性能考虑**
    
    - 由于底层基于数组，插入、删除（非尾部操作）的时间复杂度为 O(n)，因为需要移动元素。
    - 如果经常需要在中间插入或删除元素，可以考虑使用 `LinkedList`。
2. **线程安全**
    - `ArrayList` 是非线程安全的。如果需要线程安全的操作，可以使用 `Collections.synchronizedList`：
        
        ```java
        List<String> syncList = Collections.synchronizedList(new ArrayList<>());
        ```
        
3. **自动装箱**
    
    - `ArrayList` 支持存储任何类型的对象，包括基本数据类型（通过自动装箱将其转换为对应的包装类）。

---

`ArrayList` 是 Java 中最常用的数据结构之一，适用于需要快速随机访问和动态调整大小的场景。




```java
package org.example;  
  
import java.util.ArrayList;  
import java.util.Iterator;  
  
  
public class Main {  
    public static void main(String[] args) {  
        ArrayList<Integer> list = new ArrayList<>();  
        list.add(1);  
        list.add(2);  
        list.add(3);  
        list.add(4);  
        //常规遍历
        for (int i = 0; i < list.size(); i++) {  
            System.out.println(list.get(i));  
        }  
        System.out.println("--------------------");  
        //高级遍历
        for (Integer i : list) {  
            System.out.println(i);  
        }  
        System.out.println("--------------------");  
        //迭代器
        Iterator<Integer> iterator = list.iterator();  
        while (iterator.hasNext()) {  
            System.out.println(iterator.next());  
        }  
    }  
}
```


