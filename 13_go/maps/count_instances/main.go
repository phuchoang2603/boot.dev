package main

func updateCounts(messagedUsers []string, validUsers map[string]int) {
	for _, username := range messagedUsers {
		if _, ok := validUsers[username]; ok {
			validUsers[username] += 1
		}
	}
}
