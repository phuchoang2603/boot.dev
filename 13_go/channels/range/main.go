package main

func concurrentFib(n int) []int {
	ch := make(chan int)
	result := make([]int, 0)

	go fibonacci(n, ch)

	for num := range ch {
		result = append(result, num)
	}

	return result
}

func fibonacci(n int, ch chan int) {
	x, y := 0, 1
	for range n {
		ch <- x
		x, y = y, x+y
	}
	close(ch)
}
