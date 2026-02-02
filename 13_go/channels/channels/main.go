package main

import (
	"fmt"
	"time"
)

type email struct {
	body string
	date time.Time
}

func checkEmailAge(emails [3]email) [3]bool {
	isOldChan := make(chan bool)

	go sendIsOld(isOldChan, emails)

	isOld := [3]bool{}
	fmt.Println("assign 1st")
	isOld[0] = <-isOldChan
	fmt.Println("assign 2nd")
	isOld[1] = <-isOldChan
	fmt.Println("assign 3rd")
	isOld[2] = <-isOldChan
	return isOld
}

func sendIsOld(isOldChan chan<- bool, emails [3]email) {
	for _, e := range emails {
		fmt.Println("execute sendIsOld")
		if e.date.Before(time.Date(2020, 0, 0, 0, 0, 0, 0, time.UTC)) {
			isOldChan <- true
			continue
		}
		isOldChan <- false
	}
}
