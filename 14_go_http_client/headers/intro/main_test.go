package main

import (
	"fmt"
	"net/http"
	"testing"
)

func Test(t *testing.T) {
	type testCase struct {
		headers  map[string]string
		expected string
	}

	runCases := []testCase{
		{map[string]string{"Content-Type": "application/json", "Authorization": "Bearer token123"}, "application/json"},
		{map[string]string{"Content-Type": "text/html", "Accept-Language": "en-US"}, "text/html"},
	}

	submitCases := append(runCases, []testCase{
		{map[string]string{"Authorization": "Bearer token123"}, ""},
		{map[string]string{"Content-Type": "application/xml", "Cache-Control": "no-cache"}, "application/xml"},
	}...)

	testCases := runCases
	if withSubmit {
		testCases = submitCases
	}

	skipped := len(submitCases) - len(testCases)

	passCount := 0
	failCount := 0

	for _, test := range testCases {
		res := &http.Response{
			Header: http.Header{},
		}
		for key, value := range test.headers {
			res.Header.Set(key, value)
		}

		output := getContentType(res)

		if output != test.expected {
			failCount++
			t.Errorf(`---------------------------------
Headers:    %v
Expecting:  %v
Actual:     %v
Fail
`, test.headers, test.expected, output)
		} else {
			passCount++
			fmt.Printf(`---------------------------------
Headers:    %v
Expecting:  %v
Actual:     %v
Pass
`, test.headers, test.expected, output)
		}
	}

	fmt.Println("---------------------------------")
	if skipped > 0 {
		fmt.Printf("%d passed, %d failed, %d skipped\n", passCount, failCount, skipped)
	} else {
		fmt.Printf("%d passed, %d failed\n", passCount, failCount)
	}
}

// withSubmit is set at compile time depending
// on which button is used to run the tests
var withSubmit = true
