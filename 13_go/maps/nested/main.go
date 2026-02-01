package main

func getNameCounts(names []string) map[rune]map[string]int {
	countedNames := make(map[rune]map[string]int)

	for _, name := range names {
		firstChar := []rune(name)[0]

		if _, exist := countedNames[firstChar]; !exist {
			countedNames[firstChar] = make(map[string]int)
		}

		countedNames[firstChar][name] += 1
	}

	return countedNames
}
