package main

import (
	"encoding/json"
	"os"
	"slices"
)

func writeJSONReport(pages map[string]PageData, filename string) error {
	keys := make([]string, 0, len(pages))
	for k := range pages {
		keys = append(keys, k)
	}
	slices.Sort(keys)

	orderedPages := make([]PageData, 0, len(pages))
	for _, k := range keys {
		orderedPages = append(orderedPages, pages[k])
	}

	data, err := json.MarshalIndent(orderedPages, "", "  ")
	if err != nil {
		return err
	}

	return os.WriteFile(filename, data, 0o644)
}
