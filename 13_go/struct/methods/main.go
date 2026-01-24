package main

import "fmt"

type authenticationInfo struct {
	username string
	password string
}

// create the method below
func (auth authenticationInfo) getBasicAuth() string {
	return fmt.Sprintf("Authorization: Basic %v:%v", auth.username, auth.password)
}
