package main

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strings"
)

func getHTML(rawURL string) (string, error) {
	req, err := http.NewRequest("GET", rawURL, nil)
	if err != nil {
		return "", err
	}

	req.Header.Set("User-Agent", "BootCrawler/1.0")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	if resp.StatusCode >= 400 {
		return "", fmt.Errorf("received HTTP status %d", resp.StatusCode)
	}

	if !strings.HasPrefix(resp.Header.Get("Content-Type"), "text/html") {
		return "", fmt.Errorf("received non-HTML content type: %s", resp.Header.Get("Content-Type"))
	}

	bodyBytes, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	return string(bodyBytes), nil
}

func (c *config) crawlPage(rawCurrentURL string) {
	c.concurrencyControl <- struct{}{}
	defer func() {
		<-c.concurrencyControl
		c.wg.Done()
	}()

	if c.isCrawlComplete() {
		return
	}

	normalizedURL, err := normalizeURL(rawCurrentURL)
	if err != nil {
		fmt.Printf("Error - crawlPage: couldn't normalize URL '%s': %v\n", rawCurrentURL, err)
		return
	}
	if isFirst := c.addPageVisit(normalizedURL); !isFirst {
		return
	}
	currentURL, err := url.Parse(rawCurrentURL)
	if err != nil || c.baseURL.Hostname() != currentURL.Hostname() {
		return
	}

	html, err := getHTML(rawCurrentURL)
	if err != nil {
		fmt.Printf("Error - crawlPage: couldn't get HTML for URL '%s': %v\n", rawCurrentURL, err)
		return
	}

	fmt.Printf("Crawled: %s\n", rawCurrentURL)

	pageData := extractPageData(html, rawCurrentURL)
	c.setPageData(normalizedURL, pageData)
	for _, nextURL := range pageData.OutgoingLinks {
		c.wg.Add(1)
		go c.crawlPage(nextURL)
	}
}

func (c *config) addPageVisit(normalizedURL string) (isFirst bool) {
	c.mu.Lock()
	defer c.mu.Unlock()

	if _, exists := c.pages[normalizedURL]; exists {
		return false
	}

	c.pages[normalizedURL] = PageData{}
	return true
}

func (c *config) setPageData(normalizedURL string, data PageData) {
	c.mu.Lock()
	defer c.mu.Unlock()

	c.pages[normalizedURL] = data
}

func (c *config) isCrawlComplete() bool {
	c.mu.Lock()
	defer c.mu.Unlock()

	return len(c.pages) >= c.maxPages
}
