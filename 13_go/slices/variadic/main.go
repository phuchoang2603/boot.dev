package main

func sum(nums ...int) (result int) {
	for i := range nums {
		result += nums[i]
	}
	return
}
