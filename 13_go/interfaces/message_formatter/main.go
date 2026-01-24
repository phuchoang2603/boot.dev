package main

type formatter interface {
	format() string
}

type plainText struct {
	message string
}

func (pt plainText) format() string {
	return pt.message
}

type bold struct {
	message string
}

func (b bold) format() string {
	return "**" + b.message + "**"
}

type code struct {
	message string
}

func (c code) format() string {
	return "`" + c.message + "`"
}

func sendMessage(format formatter) string {
	return format.format() // Adjusted to call Format without an argument
}
