package main

import (
	"net/url"
	"testing"
)

func Test_getHeadingFromHTML(t *testing.T) {
	tests := []struct {
		name string // description of this test case
		// Named input parameters for target function.
		html string
		want string
	}{
		{
			name: "extract heading",
			html: `<html><head><title>Test</title></head><body><h1>Heading 1</h1></body></html>`,
			want: "Heading 1",
		},
		{
			name: "no heading",
			html: `<html><head><title>Test</title></head><body><p>No heading here</p></body></html>`,
			want: "",
		},
		{
			name: "extract h2 heading",
			html: `<html><head><title>Test</title></head><body><h2>Heading 2</h2></body></html>`,
			want: "Heading 2",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := getHeadingFromHTML(tt.html)
			if got != tt.want {
				t.Errorf("getHeadingFromHTML() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_getFirstParagraphFromHTML(t *testing.T) {
	tests := []struct {
		name string // description of this test case
		// Named input parameters for target function.
		html string
		want string
	}{
		{
			name: "extract first paragraph",
			html: `<html><head><title>Test</title></head><body><p>First paragraph.</p><p>Second paragraph.</p></body></html>`,
			want: "First paragraph.",
		},
		{
			name: "no paragraphs",
			html: `<html><head><title>Test</title></head><body><h1>No paragraphs here</h1></body></html>`,
			want: "",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := getFirstParagraphFromHTML(tt.html)
			if got != tt.want {
				t.Errorf("getFirstParagraphFromHTML() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_getURLsFromHTML(t *testing.T) {
	tests := []struct {
		name string // description of this test case
		// Named input parameters for target function.
		htmlBody string
		baseURL  *url.URL
		want     []string
		wantErr  bool
	}{
		{
			name: "extract URLs",
			htmlBody: `<html><head><title>Test</title></head><body>
					<a href="https://www.example.com">Example</a>
					<a href="/relative/path">Relative Path</a>
				</body></html>`,
			baseURL: &url.URL{
				Scheme: "https",
				Host:   "www.test.com",
			},
			want: []string{
				"https://www.example.com",
				"https://www.test.com/relative/path",
			},
			wantErr: false,
		},
		{
			name:     "no links",
			htmlBody: `<html><head><title>Test</title></head><body><p>No links here</p></body></html>`,
			baseURL: &url.URL{
				Scheme: "https",
				Host:   "www.test.com",
			},
			want:    []string{},
			wantErr: false,
		},
		{
			name: "relative links with base URL",
			htmlBody: `<html><head><title>Test</title></head><body>
					<a href="/relative/path1">Relative Path 1</a>
					<a href="/relative/path2">Relative Path 2</a>
				</body></html>`,
			baseURL: &url.URL{
				Scheme: "https",
				Host:   "www.test.com",
			},
			want: []string{
				"https://www.test.com/relative/path1",
				"https://www.test.com/relative/path2",
			},
			wantErr: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, gotErr := getURLsFromHTML(tt.htmlBody, tt.baseURL)
			if gotErr != nil {
				if !tt.wantErr {
					t.Errorf("getURLsFromHTML() failed: %v", gotErr)
				}
				return
			}
			if tt.wantErr {
				t.Fatal("getURLsFromHTML() succeeded unexpectedly")
			}
			if len(got) != len(tt.want) {
				t.Errorf("getURLsFromHTML() returned %d URLs, want %d", len(got), len(tt.want))
				return
			}
			for i := range got {
				if got[i] != tt.want[i] {
					t.Errorf("getURLsFromHTML()[%d] = %v, want %v", i, got[i], tt.want[i])
				}
			}
		})
	}
}

func Test_getImagesFromHTML(t *testing.T) {
	tests := []struct {
		name string // description of this test case
		// Named input parameters for target function.
		htmlBody string
		baseURL  *url.URL
		want     []string
		wantErr  bool
	}{
		{
			name: "extract image URLs",
			htmlBody: `<html><head><title>Test</title></head><body>
					<img src="https://www.example.com/image1.jpg" />
					<img src="/relative/image2.jpg" />
				</body></html>`,
			baseURL: &url.URL{
				Scheme: "https",
				Host:   "www.test.com",
			},
			want: []string{
				"https://www.example.com/image1.jpg",
				"https://www.test.com/relative/image2.jpg",
			},
			wantErr: false,
		},
		{
			name:     "no images",
			htmlBody: `<html><head><title>Test</title></head><body><p>No images here</p></body></html>`,
			baseURL: &url.URL{
				Scheme: "https",
				Host:   "www.test.com",
			},
			want:    []string{},
			wantErr: false,
		},
		{
			name: "relative image URLs with base URL",
			htmlBody: `<html><head><title>Test</title></head><body>
					<img src="/relative/image1.jpg" />
					<img src="/relative/image2.jpg" />
				</body></html>`,
			baseURL: &url.URL{
				Scheme: "https",
				Host:   "www.test.com",
			},
			want: []string{
				"https://www.test.com/relative/image1.jpg",
				"https://www.test.com/relative/image2.jpg",
			},
			wantErr: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, gotErr := getImagesFromHTML(tt.htmlBody, tt.baseURL)
			if gotErr != nil {
				if !tt.wantErr {
					t.Errorf("getImagesFromHTML() failed: %v", gotErr)
				}
				return
			}
			if tt.wantErr {
				t.Fatal("getImagesFromHTML() succeeded unexpectedly")
			}
			if len(got) != len(tt.want) {
				t.Errorf("getImagesFromHTML() returned %d URLs, want %d", len(got), len(tt.want))
				return
			}
			for i := range got {
				if got[i] != tt.want[i] {
					t.Errorf("getImagesFromHTML()[%d] = %v, want %v", i, got[i], tt.want[i])
				}
			}
		})
	}
}

func Test_extractPageData(t *testing.T) {
	tests := []struct {
		name string // description of this test case
		// Named input parameters for target function.
		html    string
		pageURL string
		want    PageData
	}{
		{
			name: "extract page data",
			html: `<html><head><title>Test</title></head><body>
					<h1>Test Heading</h1>
					<p>First paragraph.</p>
					<a href="https://www.example.com">Example</a>
					<img src="https://www.example.com/image.jpg" />
				</body></html>`,
			pageURL: "https://www.test.com",
			want: PageData{
				URL:            "https://www.test.com",
				Heading:        "Test Heading",
				FirstParagraph: "First paragraph.",
				OutgoingLinks:  []string{"https://www.example.com"},
				ImageURLs:      []string{"https://www.example.com/image.jpg"},
			},
		},
		{
			name:    "empty page",
			html:    `<html><head><title>Test</title></head><body></body></html>`,
			pageURL: "https://www.test.com",
			want: PageData{
				URL:            "https://www.test.com",
				Heading:        "",
				FirstParagraph: "",
				OutgoingLinks:  []string{},
				ImageURLs:      []string{},
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := extractPageData(tt.html, tt.pageURL)
			if got.URL != tt.want.URL ||
				got.Heading != tt.want.Heading ||
				got.FirstParagraph != tt.want.FirstParagraph ||
				len(got.OutgoingLinks) != len(tt.want.OutgoingLinks) ||
				len(got.ImageURLs) != len(tt.want.ImageURLs) {
				t.Errorf("extractPageData() = %v, want %v", got, tt.want)
			}
		})
	}
}
