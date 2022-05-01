def my_func(x, y):
    if y < 0:
        for i in range(1, abs(y)):
            x = 1/x*1/x
        return x
    else:
        return "Знаменатель должен быть меньше 0"


print(my_func(2,-1))
