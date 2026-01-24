package main

func countConnections(groupSize int) (connections int) {
	for size := 2; size <= groupSize; size++ {
		connections += size - 1
	}
	return
}
