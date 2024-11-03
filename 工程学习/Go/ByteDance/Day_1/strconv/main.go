package main

import (
    "fmt"
    "strings"
)

func main() {
    // 示例输入字符串
    input := "  Hello, World!  \r\n"
	fmt.Println(input)

    // 去除字符串开头和结尾的空白字符和换行符
    trimmedInput := strings.Trim(input, " \r\n")

    fmt.Println("Original input:", input)
    fmt.Println("Trimmed input:", trimmedInput)
}
