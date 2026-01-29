package main

func isValidPassword(password string) (isValid bool) {
	if len(password) < 5 || len(password) > 12 {
		return
	}

	hasUpper := false
	hasDigit := false

	for _, char := range password {
		if char >= 'A' && char <= 'Z' {
			hasUpper = true
		}

		if char >= '0' && char <= '9' {
			hasDigit = true
		}
	}

	if hasDigit && hasUpper {
		return true
	}

	return
}
