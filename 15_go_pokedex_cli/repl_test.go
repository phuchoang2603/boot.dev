package main

import "testing"

func TestCleanInput(t *testing.T) {
	type testCase struct {
		input    string
		expected []string
	}

	testCases := []testCase{
		{
			input:    "  hello  world  ",
			expected: []string{"hello", "world"},
		},
		{
			input:    "catch pikachu",
			expected: []string{"catch", "pikachu"},
		},
		{
			input:    "EXPLORE",
			expected: []string{"explore"},
		},
		{
			input:    "",
			expected: []string{},
		},
		{
			input:    "   ",
			expected: []string{},
		},
	}

	for _, tc := range testCases {
		actual := cleanInput(tc.input)
		if len(actual) != len(tc.expected) {
			t.Errorf("Length mismatch: expected %d, got %d", len(tc.expected), len(actual))
			continue
		}
		for i := range actual {
			if actual[i] != tc.expected[i] {
				t.Errorf("Test case '%s': expected %v, got %v", tc.input, tc.expected, actual)
				break
			}
		}
	}
}
