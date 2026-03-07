package main

import (
	"bytes"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

func TestHandlerChirpsValidate_ChirpTooLong(t *testing.T) {
	longBody := strings.Repeat("a", 141)
	reqBody := []byte(`{"body":"` + longBody + `"}`)
	req := httptest.NewRequest(http.MethodPost, "/api/validate_chirp", bytes.NewBuffer(reqBody))
	req.Header.Set("Content-Type", "application/json")
	res := httptest.NewRecorder()

	handlerChirpsValidate(res, req)

	if got, want := res.Result().StatusCode, http.StatusBadRequest; got != want {
		t.Fatalf("unexpected status %d, want %d", got, want)
	}

	var payload struct {
		Error string `json:"error"`
	}
	if err := json.NewDecoder(res.Body).Decode(&payload); err != nil {
		t.Fatalf("decode response: %v", err)
	}
	if payload.Error != "Chirp is too long" {
		t.Fatalf("unexpected error message %q", payload.Error)
	}
}

func TestReplaceBadWord(t *testing.T) {
	tests := []struct {
		name string
		body string
		want string
	}{
		{name: "non bad word", body: "hello", want: "hello"},
		{name: "single bad word", body: "kerfuffle", want: "****"},
		{name: "bad word case insens", body: "Sharbert", want: "****"},
		{name: "mixed words", body: "fornax hello", want: "**** hello"},
		{name: "non bad word with exclamation", body: "Fornax! hello", want: "Fornax! hello"},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := replaceBadWord(tt.body); got != tt.want {
				t.Fatalf("unexpected replacement %q, want %q", got, tt.want)
			}
		})
	}
}
