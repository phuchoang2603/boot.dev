package main

import (
	"bytes"
	"log/slog"
	"net/http"
	"net/http/httptest"
	"testing"
	"time"
)

func Test_redactIP(t *testing.T) {
	tests := []struct {
		name string // description of this test case
		// Named input parameters for target function.
		hostport string
		want     string
	}{
		{
			name:     "IPv4 address with port",
			hostport: "192.168.1.1:8080",
			want:     "192.168.1.x",
		},
		{
			name:     "Local IPv6 address with port",
			hostport: "[::1]:8080",
			want:     "127.0.0.x",
		},
		{
			name:     "Invalid hostport format",
			hostport: "invalid_hostport",
			want:     "invalid_hostport",
		},
		{
			name:     "Non-IP host with port",
			hostport: "example.com:8080",
			want:     "example.com",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := redactIP(tt.hostport)
			if got != tt.want {
				t.Errorf("redactIP() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_requestLogger(t *testing.T) {
	logBuffer := &bytes.Buffer{}

	logger := slog.New(slog.NewTextHandler(logBuffer, &slog.HandlerOptions{
		ReplaceAttr: func(groups []string, a slog.Attr) slog.Attr {
			if a.Key == slog.TimeKey {
				return slog.Time(slog.TimeKey, time.Date(2023, 10, 1, 12, 34, 57, 0, time.UTC))
			}
			return a
		},
	}))

	requestLoggerMiddleware := requestLogger(logger)
	dummyHandler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {})
	loggedHandler := requestLoggerMiddleware(dummyHandler)

	req := httptest.NewRequest("GET", "http://lin.ko/api/stats", nil)
	rr := httptest.NewRecorder()
	loggedHandler.ServeHTTP(rr, req)

	const expectedLogString = `time=2023-10-01T12:34:57.000Z level=INFO msg="Served request" method=GET path=/api/stats client_ip=192.0.2.1:1234` + "\n"
	const expectedStatusCode = http.StatusOK

	if rr.Code != expectedStatusCode {
		t.Errorf("Expected status code %d, got %d", expectedStatusCode, rr.Code)
	}

	if logBuffer.String() != expectedLogString {
		t.Errorf("Expected log string:\n%s\nGot:\n%s", expectedLogString, logBuffer.String())
	}
}
