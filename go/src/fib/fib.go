package main

import (
	"strconv"
	"fmt"
	"os"
	"time"
	"math"
)

func fib(num int) int {
	if num == 0 || num == 1 {
		return 1
	} else {
		return fib(num - 1) + fib(num - 2)
	}
}

func main() {
	n, err := strconv.Atoi(os.Args[1])
	if err != nil {
		// handle error
		fmt.Println(err)
		os.Exit(2)
	}
	start := time.Now()
	fib(n)
	fmt.Println(float64(time.Since(start)) / math.Pow10(9))
}