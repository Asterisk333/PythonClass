def tenx(x):
    return x * 10


to_work = [1, 2, 3, 4, 5, 6, 7, 8, 9]

xTen = list(map(tenx, to_work))
x2_numbers = list(map(lambda x: x ** 2, to_work))

print(xTen)
print(x2_numbers)


