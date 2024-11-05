from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

maximum = reduce(lambda x, y: x if x > y else y, numbers)

minimum = reduce(lambda a, b: a-b, numbers)

print(maximum)
print(minimum)
