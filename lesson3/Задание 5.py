def sum_elements(list_numbers)
""" Суммирует введенные через пробел значения до тех пор, пока не будет введен знак вопроса."""
    global sum_result
    global fin_result
    new_list = []
    for index in range(len(list_numbers)):
        if list_numbers[index] != "?":
            new_list.append(int(list_numbers[index]))
        else:
            fin_result = True
            break
        sum_result += sum(new_list)
    return sum_result

fin_result = False
sum_result = 0
for_print_result = 0

while fin_result != True:
    numbers = input("Введите числа через пробел >>> ")
    list_numbers = numbers.split(" ")
    for_print_result = sum_elements(list_numbers)
    print(for_print_result)
