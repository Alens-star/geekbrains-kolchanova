def fact(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number


n = int(input("Факториал какого числа посчитать? >>> \n"))
for num in fact(n):
    print(num)