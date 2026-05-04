def quick_sort(nums, low, high):
    if low < high:
        middle = partition(nums, low, high)
        quick_sort(nums, low, middle - 1)
        quick_sort(nums, middle + 1, high)


def partition(nums, low, high):
    pivot = high
    i = low - 1

    for j in range(low, high):
        if nums[j] < nums[pivot]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[pivot] = nums[pivot], nums[i + 1]
    return i + 1
