### Go循环for和make声明

---

`for`循环是唯一的循环结构，并且可以通过不同的用法实现多种循环形式

- 经典循环
- for...range...
- 类似while循环
- 无限循环

```go
package main

import "fmt"

const NAME = "bx33661"

func main() {
	fmt.Println(NAME)
	// 经典for循环
	for i := 0; i < 0; i++ {
		fmt.Println(i)
	}
	// 无限循环
	for {
		fmt.Println("无限循环")
		break
	}
	// for range方法
	s := []int{1, 2, 3}
	for i := range s {
		fmt.Println(i)
	}
	for index, i := range s {
		fmt.Println(index, i)
	}
	//类似while循环
	i := 0
	for i < 3 {
		fmt.Println(i)
		i++
	}
}
```

类似于while的写法：基本写法如下

```go
// Go 中的 while 循环相当于这样写
for condition {
    // 循环体
}
```



看到一个关于`for...range`比较好的例子

```go
// 遍历数组或切片
numbers := []int{1, 2, 3, 4, 5}
for index, value := range numbers {
    fmt.Println("Index:", index, "Value:", value)
}

// 遍历字符串
text := "Hello"
for index, char := range text {
    fmt.Println("Index:", index, "Character:", string(char))
}

// 遍历映射（map）
ages := map[string]int{"Alice": 25, "Bob": 30}
for key, value := range ages {
    fmt.Println("Key:", key, "Value:", value)
}
```



### make声明

----

> `make`是一个内建函数，用于创建和初始化**切片**（`slice`）、**映射**（`map`）和**通道**（`channel`）这三种引用类型

基本语法：

### `make`的基本语法

```go
make(type, size, capacity)
```

- **type**：要创建的类型，只能是`slice`、`map`或`channel`。
- **size**：指定切片或通道的大小。
- **capacity**：可选参数，仅适用于切片，指定切片的容量。



| 类型 | 必要参数         | 可选参数 | 示例                   |
| ---- | ---------------- | -------- | ---------------------- |
| 切片 | 长度             | 容量     | `make([]int, 5, 10)`   |
| 映射 | 无需指定初始大小 | 无       | `make(map[string]int)` |
| 通道 | 无缓冲或缓冲大小 | 无       | `make(chan int, 3)`    |