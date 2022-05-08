from functools import reduce
sum = reduce(lambda a, x: a + x, [el for el in range(99, 1001) if el % 2 == 0])
print(sum)
