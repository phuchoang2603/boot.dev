package main

func getMessageWithRetries(primary, secondary, tertiary string) ([3]string, [3]int) {
	messages := [3]string{primary, secondary, tertiary}

	totalCost := 0
	costs := [3]int{}
	for i := 0; i < 3; i++ {
		totalCost += len(messages[i])
		costs[i] = totalCost
	}

	return messages, costs
}
