def my_func(arg1, arg2, arg3):
    list_func = [arg1, arg2, arg3]
    list_func.pop(list_func.index(min(list_func)))
    return sum(list_func)

print(my_func(1,3,6))
