package main

import (
	"fmt"
	"strings"
	"testing"
)

func Test(t *testing.T) {
	type testCase struct {
		address   string
		expectErr bool
	}

	runCases := []testCase{
		{"boot.dev", false},
		{"example.com", false},
		{"cloudflare.com", false},
	}

	submitCases := append(runCases, []testCase{
		{"iana.org", false},
	}...)

	testCases := runCases
	if withSubmit {
		testCases = submitCases
	}

	skipped := len(submitCases) - len(testCases)

	passCount := 0
	failCount := 0

	for _, test := range testCases {
		output, err := getIPAddress(test.address)
		splitIP := strings.Split(output, ".")
		if err != nil && !test.expectErr {
			failCount++
			t.Errorf(`---------------------------------
URL:			%v
ExpectedErr:	%v
GotErr:			%v
Fail
`, test.address, test.expectErr, err.Error())
		} else if len(splitIP) != 4 {
			failCount++
			t.Errorf(`---------------------------------
URL:			%v
Expected IP:	%v
Got:			%v
Fail
`, test.address, true, output)
		} else {
			passCount++
			fmt.Printf(`---------------------------------
URL:			%v
IP Address:		%v
Pass
`, test.address, output)
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
