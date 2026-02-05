package pokeapi

import (
	"encoding/json"
	"io"
	"net/http"
)

type LocationInfo struct {
	EncounterMethodRates []struct {
		EncounterMethod struct {
			Name string `json:"name"`
			URL  string `json:"url"`
		} `json:"encounter_method"`
		VersionDetails []struct {
			Rate    int `json:"rate"`
			Version struct {
				Name string `json:"name"`
				URL  string `json:"url"`
			} `json:"version"`
		} `json:"version_details"`
	} `json:"encounter_method_rates"`
	GameIndex int `json:"game_index"`
	ID        int `json:"id"`
	Location  struct {
		Name string `json:"name"`
		URL  string `json:"url"`
	} `json:"location"`
	Name  string `json:"name"`
	Names []struct {
		Language struct {
			Name string `json:"name"`
			URL  string `json:"url"`
		} `json:"language"`
		Name string `json:"name"`
	} `json:"names"`
	PokemonEncounters []PokemonEncounter `json:"pokemon_encounters"`
}

type PokemonEncounter struct {
	Pokemon struct {
		Name string `json:"name"`
		URL  string `json:"url"`
	} `json:"pokemon"`
	VersionDetails []struct {
		EncounterDetails []struct {
			Chance          int   `json:"chance"`
			ConditionValues []any `json:"condition_values"`
			MaxLevel        int   `json:"max_level"`
			Method          struct {
				Name string `json:"name"`
				URL  string `json:"url"`
			} `json:"method"`
			MinLevel int `json:"min_level"`
		} `json:"encounter_details"`
		MaxChance int `json:"max_chance"`
		Version   struct {
			Name string `json:"name"`
			URL  string `json:"url"`
		} `json:"version"`
	} `json:"version_details"`
}

func (c *Client) GetLocationInfo(locationArea string) (locationResp LocationInfo, err error) {
	url := baseURL + "/location-area/" + locationArea

	data, found := c.cache.Get(url)

	if !found {
		req, err := http.NewRequest("GET", url, nil)
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
		c.cache.Add(url, data)
	}

	if err := json.Unmarshal(data, &locationResp); err != nil {
		return LocationInfo{}, err
	}

	return locationResp, nil
}
