package main

import (
	"fmt"
	"testing"
)

func Test(t *testing.T) {
	type testCase struct {
		address   string
		expectErr bool
		expected  string
	}

	runCases := []testCase{
		{"https://boot.dev/learn/learn-python", false, "boot.dev"},
		{"https://youtube.com", false, "youtube.com"},
	}

	submitCases := append(runCases, []testCase{
		{"://example.com", true, ""},
	}...)

	testCases := runCases
	if withSubmit {
		testCases = submitCases
	}

	skipped := len(submitCases) - len(testCases)

	passCount := 0
	failCount := 0

	for _, test := range testCases {
		output, err := getDomainNameFromURL(test.address)

		if test.expectErr && (err != nil) != test.expectErr {
			failCount++
			t.Errorf(`---------------------------------
URL:		%v
ExpectErr:	%v
GotErr:		%v
Fail
`, test.address, test.expectErr, err != nil)
		} else if output != test.expected {
			failCount++
			t.Errorf(`---------------------------------
URL:		%v
Expecting:	%v
Actual:		%v
Fail
`, test.address, test.expected, output)
		} else {
			passCount++
			fmt.Printf(`---------------------------------
URL:		%v
Expecting:  %v
Actual:     %v
Pass
`, test.address, test.expected, output)
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
