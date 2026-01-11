def sum_nested_list(lst: list) -> int:
    total_size = 0
    for item in lst:
        if not isinstance(item, list):
            total_size += item
        else:
            total_size += sum_nested_list(item)
    return total_size
