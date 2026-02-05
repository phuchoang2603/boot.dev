package main

import (
	"fmt"
	"reflect"
	"testing"
)

func Test(t *testing.T) {
	type testCase struct {
		url      string
		expected []Issue
	}

	runCases := []testCase{
		{
			"https://api.boot.dev/v1/courses_rest_api/learn-http/issues?limit=1",
			[]Issue{{Title: "Fix that one bug nobody understands", Estimate: 19}},
		},
		{
			"https://api.boot.dev/v1/courses_rest_api/learn-http/issues?limit=2",
			[]Issue{
				{Title: "Fix that one bug nobody understands", Estimate: 19},
				{Title: "Implement user authentication flow", Estimate: 6},
			},
		},
	}

	submitCases := append(runCases, []testCase{
		{"", nil},
	}...)

	testCases := runCases
	if withSubmit {
		testCases = submitCases
	}

	skipped := len(submitCases) - len(testCases)

	passCount := 0
	failCount := 0

	for _, test := range testCases {
		items, _ := getIssues(test.url)

		if !reflect.DeepEqual(items, test.expected) {
			failCount++
			t.Errorf(`---------------------------------
URL:		%v
Expecting:  %+v
Actual:     %+v
Fail
`, test.url, test.expected, items)
		} else {
			passCount++
			fmt.Printf(`---------------------------------
URL:		%v
Expecting:  %+v
Actual:     %+v
Pass
`, test.url, test.expected, items)
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
