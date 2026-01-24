package main

func bulkSend(numMessages int) float64 {
	totalCost := 0.0

	for i := 0; i < numMessages; i++ {
		totalCost += 1.0 + float64(i)/100.00
	}

	return totalCost
}
