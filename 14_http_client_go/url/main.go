package main

import (
	"net/url"
)

func newParsedURL(urlString string) ParsedURL {
	parsedURL, err := url.Parse(urlString)
	if err != nil {
		return ParsedURL{}
	}

	password, _ := parsedURL.User.Password()

	return ParsedURL{
		protocol: parsedURL.Scheme,
		username: parsedURL.User.Username(),
		password: password,
		hostname: parsedURL.Hostname(),
		port:     parsedURL.Port(),
		pathname: parsedURL.Path,
		search:   parsedURL.RawQuery,
		hash:     parsedURL.Fragment,
	}
}
