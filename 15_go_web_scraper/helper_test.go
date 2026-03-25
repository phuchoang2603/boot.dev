package main

import "testing"

func Test_normalizeURL(t *testing.T) {
	tests := []struct {
		name string // description of this test case
		// Named input parameters for target function.
		url  string
		want string
	}{
		{
			name: "remove scheme",
			url:  "https://www.boot.dev/blog/path",
			want: "www.boot.dev/blog/path",
		},
		{
			name: "remove slash",
			url:  "https://www.boot.dev/blog/path/",
			want: "www.boot.dev/blog/path",
		},
		{
			name: "remove scheme http",
			url:  "http://www.boot.dev/blog/path",
			want: "www.boot.dev/blog/path",
		},
		{
			name: "remove slash http",
			url:  "http://www.boot.dev/blog/path/",
			want: "www.boot.dev/blog/path",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := normalizeURL(tt.url)
			if err != nil {
				t.Errorf("normalizeURL() error = %v", err)
				return
			}
			if got != tt.want {
				t.Errorf("normalizeURL() = %v, want %v", got, tt.want)
			}
		})
	}
}
