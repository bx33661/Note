package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	fmt.Println(os.Args)
	fmt.Println(os.Getenv("PATH"))

	buf, err := exec.Command("ping", "www.github.com").CombinedOutput()
	if err != nil {
		panic(err)
	}
	fmt.Println(string(buf))
}
