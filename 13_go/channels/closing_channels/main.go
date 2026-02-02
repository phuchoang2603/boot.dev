package main

func countReports(numSentCh chan int) int {
	count := 0
	for num := range numSentCh {
		count += num
	}
	return count
}

func sendReports(numBatches int, ch chan int) {
	for i := range numBatches {
		numReports := i*23 + 32%17
		ch <- numReports
	}
	close(ch)
}
