package main

func getLast[T any](s []T) T {
	if tLen := len(s); tLen == 0 {
		var zero T
		return zero
	} else {
		return s[tLen-1]
	}
}
