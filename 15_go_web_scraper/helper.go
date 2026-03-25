package main

import (
	"net/url"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

func normalizeURL(inputURL string) (string, error) {
	urls, err := url.Parse(inputURL)
	if err != nil {
		return "", err
	}

	host := urls.Host
	path := urls.Path

	return host + strings.TrimSuffix(path, "/"), nil
}

func getFromHTML(htmlBody string, baseURL *url.URL, selector string, attr string) ([]string, error) {
	doc, err := goquery.NewDocumentFromReader(strings.NewReader(htmlBody))
	if err != nil {
		return nil, err
	}

	var results []string
	doc.Find(selector).Each(func(i int, s *goquery.Selection) {
		value, exists := s.Attr(attr)
		if exists {
			absoluteURL := toAbsoluteURL(value, baseURL)
			results = append(results, absoluteURL)
		}
	})

	return results, nil
}

func toAbsoluteURL(href string, baseURL *url.URL) string {
	parsedURL, err := url.Parse(href)
	if err != nil {
		return ""
	}

	if parsedURL.IsAbs() {
		return parsedURL.String()
	}

	return baseURL.ResolveReference(parsedURL).String()
}
