package main

func getMessageCosts(messages []string) (costs []float64) {
	costs = make([]float64, len(messages))

	for i := range messages {
		costs[i] = float64(len(messages[i])) * 0.01
	}

	return costs
}
