def filter_numbers(numbers):
    no_negative = list(filter(lambda x: x >= 0, numbers))
    no_negative_greater_than_ten = list(filter(lambda x: x <= 10, no_negative))
    return no_negative_greater_than_ten


to_filter = 1, 2, 3545, -4, -35, 6, 27, 8, 90

print(filter_numbers(to_filter))
