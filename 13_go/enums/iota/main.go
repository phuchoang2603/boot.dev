package main

type emailStatus int

const (
	EmailBounced emailStatus = iota
	EmailInvalid
	EmailDelivered
	EmailOpened
)
