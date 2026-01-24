package main

import (
	"fmt"
)

func (e email) cost() int {
	if !e.isSubscribed {
		return 5 * len(e.body)
	} else {
		return 2 * len(e.body)
	}
}

func (e email) format() string {
	emailStatus := "Subscribed"
	if !e.isSubscribed {
		emailStatus = "Not Subscribed"
	}
	return fmt.Sprintf("'%v' | %v", e.body, emailStatus)
}

type expense interface {
	cost() int
}

type formatter interface {
	format() string
}

type email struct {
	isSubscribed bool
	body         string
}
