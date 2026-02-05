package pokeapi

import (
	"encoding/json"
	"fmt"
	"io"
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
		fullURL := baseURL + "/location-area/"
		url = &fullURL
	}

	data, found := c.cache.Get(*url)

	if !found {
		fmt.Println("Cache miss")
		req, err := http.NewRequest("GET", *url, nil)
		if err != nil {
			return locationResp, err
		}

		resp, err := c.httpClient.Do(req)
		if err != nil {
			return locationResp, err
		}
		defer resp.Body.Close()

		data, err = io.ReadAll(resp.Body)
		if err != nil {
			return locationResp, err
		}
		c.cache.Add(*url, data)
	}

	if err := json.Unmarshal(data, &locationResp); err != nil {
		return LocationAreaResp{}, err
	}

	return locationResp, nil
}
