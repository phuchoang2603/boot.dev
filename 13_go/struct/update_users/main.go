package main

type User struct {
	Membership
	Name string
}

type Membership struct {
	Type             string
	MessageCharLimit int
}

func newUser(name string, membershipType string) User {
	messageCharLimit := 100
	if membershipType == "premium" {
		messageCharLimit = 1000
	}
	return User{
		Membership{
			Type:             membershipType,
			MessageCharLimit: messageCharLimit,
		},
		name,
	}
}
