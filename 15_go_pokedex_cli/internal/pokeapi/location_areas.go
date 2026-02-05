package pokeapi

import (
	"encoding/json"
	"net/http"
)

type LocationAreaResp struct {
	Count    int            `json:"count"`
	Next     *string        `json:"next"`
	Previous *string        `json:"previous"`
	Results  []LocationArea `json:"results"`
}

type LocationArea struct {
	Name string `json:"name"`
	URL  string `json:"url"`
}

func (c *Client) GetLocationAreaResp(url *string) (locationResp LocationAreaResp, err error) {
	if url == nil {
		url = &defaultURL
	}

	req, err := http.NewRequest("GET", *url, nil)
	if err != nil {
		return locationResp, err
	}

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return locationResp, err
	}
	defer resp.Body.Close()

	decoder := json.NewDecoder(resp.Body)
	if err := decoder.Decode(&locationResp); err != nil {
		return locationResp, err
	}

	return locationResp, nil
}
