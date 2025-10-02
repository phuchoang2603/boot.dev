def remove_nonints(nums):
    int_list = []
    for item in nums:
        if type(item) is int:
            int_list.append(item)
    return int_list
