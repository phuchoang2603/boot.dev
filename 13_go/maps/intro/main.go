package main

import "errors"

func getUserMap(names []string, phoneNumbers []int) (map[string]user, error) {
	users := map[string]user{}

	if len(names) != len(phoneNumbers) {
		return users, errors.New("invalid sizes")
	}

	for i, name := range names {
		users[name] = user{
			name,
			phoneNumbers[i],
		}
	}

	return users, nil
}

type user struct {
	name        string
	phoneNumber int
}
