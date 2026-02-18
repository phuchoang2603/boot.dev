package rss

import (
	"context"
	"encoding/xml"
	"io"
	"net/http"
)

func (c *Client) FetchFeed(ctx context.Context, feedURL string) (feed *RSSFeed, err error) {
	req, err := http.NewRequestWithContext(ctx, "GET", feedURL, nil)
	if err != nil {
		return &RSSFeed{}, err
	}
	req.Header.Set("User-Agent", UserAgent)

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return &RSSFeed{}, err
	}
	defer resp.Body.Close()

	data, err := io.ReadAll(resp.Body)
	if err != nil {
		return &RSSFeed{}, err
	}

	if err := xml.Unmarshal(data, &feed); err != nil {
		return &RSSFeed{}, err
	}

	feed.decodeFeed()

	return feed, err
}
