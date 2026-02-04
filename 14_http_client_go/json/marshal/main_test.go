package main

import (
	"fmt"
	"testing"
)

// Example structs for testing
type JelloUser struct {
	ID   string `json:"id"`
	Name string `json:"name"`
	Role string `json:"role"`
}

type JelloBoard struct {
	Name        string `json:"name"`
	Description string `json:"description"`
	TaskCount   int    `json:"taskCount"`
}

func TestMarshalAll(t *testing.T) {
	type testCase struct {
		inputs   []any
		expected [][]byte
	}

	runCases := []testCase{
		{
			inputs: []any{
				JelloUser{"001", "Sir Bedevere the Wise", "Scientist"},
				JelloUser{"002", "Sir Lancelot the Brave", "Knight"},
				JelloBoard{"Quest for the Holy Grail", "Tasks related to finding the Grail", 5},
			},
			expected: [][]byte{
				[]byte(`{"id":"001","name":"Sir Bedevere the Wise","role":"Scientist"}`),
				[]byte(`{"id":"002","name":"Sir Lancelot the Brave","role":"Knight"}`),
				[]byte(`{"name":"Quest for the Holy Grail","description":"Tasks related to finding the Grail","taskCount":5}`),
			},
		},
		{
			inputs: []any{
				JelloUser{"003", "Sir Galahad the Pure", "Knight"},
				JelloBoard{"Defeat the Killer Rabbit", "Prepare for battle with the Rabbit of Caerbannog", 7},
				JelloBoard{"Use the Holy Hand Grenade", "Instructions on deploying the Holy Hand Grenade of Antioch", 3},
			},
			expected: [][]byte{
				[]byte(`{"id":"003","name":"Sir Galahad the Pure","role":"Knight"}`),
				[]byte(`{"name":"Defeat the Killer Rabbit","description":"Prepare for battle with the Rabbit of Caerbannog","taskCount":7}`),
				[]byte(`{"name":"Use the Holy Hand Grenade","description":"Instructions on deploying the Holy Hand Grenade of Antioch","taskCount":3}`),
			},
		},
	}

	submitCases := append(runCases, []testCase{
		{
			inputs: []any{
				JelloUser{"004", "Sir Robin the Not-Quite-So-Brave-As-Sir-Lancelot", "Minstrel"},
				JelloBoard{"Avoid Dangerous Situations", "Strategies for running away bravely", 2},
			},
			expected: [][]byte{
				[]byte(`{"id":"004","name":"Sir Robin the Not-Quite-So-Brave-As-Sir-Lancelot","role":"Minstrel"}`),
				[]byte(`{"name":"Avoid Dangerous Situations","description":"Strategies for running away bravely","taskCount":2}`),
			},
		},
	}...)

	testCases := runCases
	if withSubmit {
		testCases = submitCases
	}

	skipped := len(submitCases) - len(testCases)

	passCount := 0
	failCount := 0

	for i, test := range testCases {
		output, err := marshalAll(test.inputs)
		if err != nil {
			failCount++
			t.Errorf(`---------------------------------
Test %d Failed: %v
  unexpected error: %v
`, i, test.inputs, err)
			continue
		}
		if len(output) != len(test.expected) {
			failCount++
			t.Errorf(`---------------------------------
Test %d Failed: %v
  expected length: %v
  actual length:   %v
`, i, test.inputs, len(test.expected), len(output))
			continue
		}
		for j, jsonOutput := range output {
			if string(jsonOutput) != string(test.expected[j]) {
				failCount++
				t.Errorf(`Test %d Failed at index %d:
  input:    %v
  expected: %s
  actual:   %s
`, i, j, test.inputs[j], test.expected[j], jsonOutput)
			} else {
				fmt.Printf(`---------------------------------
Test %d Passed at index %d:
  input:    %v
  expected: %s
  actual:   %s
`, i, j, test.inputs[j], test.expected[j], jsonOutput)
			}
		}
		passCount++
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
