package main

import (
	"net/url"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

type PageData struct {
	URL            string   `json:"url"`
	Heading        string   `json:"heading"`
	FirstParagraph string   `json:"first_paragraph"`
	OutgoingLinks  []string `json:"outgoing_links"`
	ImageURLs      []string `json:"image_urls"`
}

func extractPageData(html, pageURL string) PageData {
	baseURL, err := url.Parse(pageURL)
	if err != nil {
		return PageData{}
	}

	heading := getHeadingFromHTML(html)
	firstParagraph := getFirstParagraphFromHTML(html)
	outgoingLinks, _ := getURLsFromHTML(html, baseURL)
	imageURLs, _ := getImagesFromHTML(html, baseURL)

	return PageData{
		URL:            pageURL,
		Heading:        heading,
		FirstParagraph: firstParagraph,
		OutgoingLinks:  outgoingLinks,
		ImageURLs:      imageURLs,
	}
}

func getHeadingFromHTML(html string) string {
	doc, err := goquery.NewDocumentFromReader(strings.NewReader(html))
	if err != nil {
		return ""
	}

	heading := doc.Find("h1").First().Text()
	if heading == "" {
		heading = doc.Find("h2").First().Text()
	}

	return heading
}

func getFirstParagraphFromHTML(html string) string {
	doc, err := goquery.NewDocumentFromReader(strings.NewReader(html))
	if err != nil {
		return ""
	}

	return doc.Find("p").First().Text()
}

func getURLsFromHTML(htmlBody string, baseURL *url.URL) ([]string, error) {
	return getFromHTML(htmlBody, baseURL, "a", "href")
}

func getImagesFromHTML(htmlBody string, baseURL *url.URL) ([]string, error) {
	return getFromHTML(htmlBody, baseURL, "img", "src")
}
