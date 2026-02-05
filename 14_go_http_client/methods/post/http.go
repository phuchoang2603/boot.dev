package main

import (
	"bytes"
	"encoding/json"
	"net/http"
)

func createUser(url, apiKey string, data User) (User, error) {
	var user User

	jsonData, err := json.Marshal(data)
	if err != nil {
		return user, err
	}

	req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
	if err != nil {
		return user, err
	}

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("X-API-Key", apiKey)

	client := http.DefaultClient
	res, err := client.Do(req)
	if err != nil {
		return user, err
	}
	defer res.Body.Close()

	decoder := json.NewDecoder(res.Body)
	if err := decoder.Decode(&user); err != nil {
		return User{}, err
	}

	return user, nil
}
