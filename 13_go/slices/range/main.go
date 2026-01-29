package main

import "slices"

func indexOfFirstBadWord(msg []string, badWords []string) int {
	for m := range msg {
		if slices.Contains(badWords, msg[m]) {
			return m
		}
	}
	return -1
}
