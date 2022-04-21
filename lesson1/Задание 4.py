'задание 4'
number = int(input("Введите любое число "))
number_max = 0
while number != 0:
    number_start = number % 10
    number_mid = number // 10
    # print(number_mid)
    number_finish = number_mid % 10
    # print(number_finish)
    if number_start > number_finish and number_start > number_max:
        number_max = number_start
    else:
        number_max
    number //= 10
print(number_max)