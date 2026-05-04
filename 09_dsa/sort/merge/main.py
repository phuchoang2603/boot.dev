def merge_sort(nums):
    if len(nums) < 2:
        return nums

    middle = len(nums) // 2
    first_half = merge_sort(nums[:middle])
    second_half = merge_sort(nums[middle:])

    return merge(first_half, second_half)


def merge(first, second):
    i = 0
    j = 0
    sorted = []

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            sorted.append(first[i])
            i += 1
        else:
            sorted.append(second[j])
            j += 1

    sorted.extend(first[i:])
    sorted.extend(second[j:])

    return sorted
