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
