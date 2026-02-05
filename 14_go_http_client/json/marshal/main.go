package main

import (
	"encoding/json"
	"fmt"
)

func marshalAll[T any](items []T) ([][]byte, error) {
	result := [][]byte{}

	for _, item := range items {
		data, err := json.Marshal(item)
		if err != nil {
			return nil, fmt.Errorf("error convert struct to slice of bytes: %w", err)
		}

		result = append(result, data)

	}

	return result, nil
}
