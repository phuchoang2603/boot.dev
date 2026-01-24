package main

type cost struct {
	day   int
	value float64
}

func getDayCosts(costs []cost, day int) (costsGivenDay []float64) {
	for i := range costs {
		if costs[i].day == day {
			costsGivenDay = append(costsGivenDay, costs[i].value)
		}
	}
	return
}
