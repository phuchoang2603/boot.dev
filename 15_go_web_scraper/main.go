package main

import (
	"fmt"
	"net/url"
	"os"
	"strconv"
	"sync"
)

type config struct {
	pages              map[string]PageData
	baseURL            *url.URL
	maxPages           int
	mu                 *sync.Mutex
	concurrencyControl chan struct{}
	wg                 *sync.WaitGroup
}

func main() {
	args := os.Args
	if len(args) != 4 {
		fmt.Println("Usage: go run main.go <base_url> <max_concurrency> <max_pages>")
		os.Exit(1)
	}

	baseURL, err := url.Parse(args[1])
	if err != nil {
		fmt.Printf("invalid URL provided: %s\n", args[1])
		os.Exit(1)
	}

	maxConcurrency, err := strconv.Atoi(args[2])
	if err != nil {
		fmt.Printf("invalid max concurrency provided: %s\n", args[2])
		os.Exit(1)
	}

	maxPages, err := strconv.Atoi(args[3])
	if err != nil {
		fmt.Printf("invalid max pages provided: %s\n", args[3])
		os.Exit(1)
	}

	cfg := config{
		pages:              make(map[string]PageData),
		baseURL:            baseURL,
		mu:                 &sync.Mutex{},
		concurrencyControl: make(chan struct{}, maxConcurrency), // limit concurrent requests
		wg:                 &sync.WaitGroup{},
		maxPages:           maxPages,
	}

	cfg.wg.Add(1)
	go cfg.crawlPage(baseURL.String())
	cfg.wg.Wait()

	if err := writeJSONReport(cfg.pages, "report.json"); err != nil {
		fmt.Printf("Error writing JSON report: %v\n", err)
		os.Exit(1)
	}
}
