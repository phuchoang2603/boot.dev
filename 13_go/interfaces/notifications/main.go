package main

type notification interface {
	importance() int
}

type directMessage struct {
	senderUsername string
	messageContent string
	priorityLevel  int
	isUrgent       bool
}

func (dM directMessage) importance() int {
	if dM.isUrgent {
		return 50
	} else {
		return dM.priorityLevel
	}
}

type groupMessage struct {
	groupName      string
	messageContent string
	priorityLevel  int
}

func (gM groupMessage) importance() int {
	return gM.priorityLevel
}

type systemAlert struct {
	alertCode      string
	messageContent string
}

func (sA systemAlert) importance() int {
	return 100
}

func processNotification(n notification) (string, int) {
	switch noti := n.(type) {
	case directMessage:
		return noti.senderUsername, noti.importance()
	case groupMessage:
		return noti.groupName, noti.importance()
	case systemAlert:
		return noti.alertCode, noti.importance()
	default:
		return "", 0
	}
}
