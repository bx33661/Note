Hello world

```python
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello, World!")
}

```



> 在Go语言中，声明的变量必须被使用，否则编译器会报错。这是Go语言的一项设计决策，旨在减少未使用代码和潜在的错误。

for循环使用

```go
package main

import "fmt"

func main() {
	bx := "bx33661"
	// This is a comment
	for i := 0; i < 5; i++ {
		fmt.Println(bx)
	}
}
```



数组

```go
package main

import "fmt"

func main() {
	s := make([]string, 3)
	s[0] = "a"
	s[1] = "t"
	s[2] = "k"
	//添加元素
	s = append(s, "l")
	//计算元素个数
	fmt.Print("个数： ", len(s))
	fmt.Println(s)
	//切片操作
	fmt.Println(s[1:3])
}

```



range用法
```go
package main

import "fmt"

func main() {
	//创建一个数组
	nums := []int{1, 2, 3, 4, 5}
	sum := 0
	//利用range遍历数组
	for i, v := range nums {
		sum += v
		fmt.Println("index: ", i, " value: ", v, "\n")
	}
	fmt.Println("sum: ", sum)
    //创建一个键值对
	m := map[string]string{"a": "apple", "b": "banana"}
	//利用range遍历map
	for k, v := range m {
		fmt.Println("key: ", k, " value: ", v)
	}
}
```



函数

```go
package main

import "fmt"

func add(a int, b int) int {
	return a + b
}

func main() {
	num1 := 3
	num2 := 5
	sum := add(num1, num2)
	fmt.Println("Sum of", num1, "and", num2, "is", sum)
}

```



指针

可以直接修改变量

```go
package main

import "fmt"

func add(n int) {
	n += 2
}

func add1(n *int) {
	*n += 2
}

func main() {
	n := 10
	add(n)
	fmt.Println(n)
	add1(&n)
	fmt.Println(n)
}

```



结构体

```go
package main

import "fmt"

type User struct{
	name string
	password string
}
func main(){
	dx := User{"dx33662","123456"}
	fmt.Println(dx.name,dx.password) 
}
```



错误
```go
package main

import (
	"errors"
	"fmt"
)

type user struct {
	name     string
	password string
}

func findUser(users []user, name string) (v *user, err error) {
	for _, u := range users {
		if u.name == name {
			return &u, nil
		}
	}
	return nil, errors.New("not found")
}

func main() {
	u, err := findUser([]user{{"wang", "1024"}}, "wang")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(u.name) // wang

	if u, err := findUser([]user{{"wang", "1024"}}, "li"); err != nil {
		fmt.Println(err) // not found
		return
	} else {
		fmt.Println(u.name)
	}
}
```

> 对于错误类型 `error`，`nil` 表示没有错误发生

我来解释几个点

```go
func findUser(users []user, name string) (v *user, err error)
```

定义了一个`findUser`函数，两个括号语法，第一个括号是接受参数，有两个参数

- users ---`[]user`类型
- name --- `string`类型

第二个是返回值，`v *user, err error`



格式化输出

> `%v` 是 [fmt](vscode-file://vscode-app/d:/BaiduNetdiskDownload/Microsoft VS Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 包中用于格式化输出的占位符之一。`%v` 可以用于打印任何类型的值，并且会根据值的类型选择合适的格式进行输出

- **`%+v`**：打印结构体时，会包括字段名。

  - **示例**：

    `fmt.Printf("p=%+v\n", p) // p={x:1 y:2}`

  - **输出**：

    `p={x:1 y:2}`

- **`%#v`**：打印值的 Go 语法表示，通常用于调试。

  - **示例**：

    `fmt.Printf("p=%#v\n", p) // p=main.point{x:1, y:2}`

  - **输出**：

    `p=main.point{x:1, y:2}`

- **`%T`**：打印值的类型。

  - **示例**：

    `fmt.Printf("p=%T\n", p) // p=main.point`

  - **输出**：

    `p=main.point`

- **`%%`**：打印百分号本身。

  - **示例**：

    `fmt.Printf("%%\n") // %`

  - **输出**：

    `%`

    



### 实战项目

#### 猜数游戏

```go
package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"strings"
)

func main() {
	maxNum := 100
	randomNum := rand.Intn(maxNum)
	fmt.Println("请输入一个数字")
	user_num := bufio.NewReader(os.Stdin)
	for {
		input, err := user_num.ReadString('\n')
		if err != nil {
			fmt.Println("输入过程出现错", err)
			continue
		}
		input = strings.Trim(input, "\r\n")
		guess, err := strconv.Atoi(input)
		if err != nil {
			fmt.Println("错误", err)
			return
		}
		fmt.Println("你输入的数为：", input)
		if guess == randomNum {
			fmt.Println("恭喜你，猜对了！！")
			break
		} else if guess > randomNum {
			fmt.Println("你输入的数大了，try again!!")
		} else {
			fmt.Println("你输入的数小了，try again!!")
		}
	}

}

```



#### 在线词典

