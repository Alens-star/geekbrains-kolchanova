from functools import reduce
sum = reduce(lambda a, x: a + x, [el for el in range(100, 1000) if el % 2 == 0])
print(sum)