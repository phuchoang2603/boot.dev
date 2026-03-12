// Package auth provides authentication and authorization functionality for the HTTP server.
package auth

import (
	"crypto/rand"
	"encoding/hex"
	"net/http"
	"strings"
)

func GetBearerToken(headers http.Header) (string, error) {
	authHeader := headers.Get("Authorization")
	if !strings.HasPrefix(authHeader, "Bearer ") {
		return "", http.ErrNoCookie
	}
	return strings.TrimPrefix(authHeader, "Bearer "), nil
}

func GetAPIKey(headers http.Header) (string, error) {
	authHeader := headers.Get("Authorization")
	if !strings.HasPrefix(authHeader, "ApiKey ") {
		return "", http.ErrNoCookie
	}
	return strings.TrimPrefix(authHeader, "ApiKey "), nil
}

func MakeRefreshToken() string {
	b := make([]byte, 32)

	if _, err := rand.Read(b); err != nil {
		return ""
	}

	return hex.EncodeToString(b)
}
