package main

type Message interface {
	Type() string
}

type TextMessage struct {
	Sender  string
	Content string
}

func (tm TextMessage) Type() string {
	return "text"
}

type MediaMessage struct {
	Sender    string
	MediaType string
	Content   string
}

func (mm MediaMessage) Type() string {
	return "media"
}

type LinkMessage struct {
	Sender  string
	URL     string
	Content string
}

func (lm LinkMessage) Type() string {
	return "link"
}

func filterMessages(messages []Message, filterType string) (filterMsg []Message) {
	for _, msg := range messages {
		if msg.Type() == filterType {
			filterMsg = append(filterMsg, msg)
		}
	}
	return
}
