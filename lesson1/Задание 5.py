'задание 5'

revenue = int(input("Введите выручку в рублях >>>> "))
costs = int(input("Введите затраты в рублях >>>> "))
if revenue < costs:
    print("Фирма получила убыток >>>> {} руб.".format(int(revenue-costs)))
else:
    profit = int(((revenue-costs)/revenue)*100)
    print("Фирма сработала в плюс. Рентабельность выручки {}%.".format(profit))
    num_of_empl = int(input("Введите количество сотрудников >>>> "))
    print("Средняя прибыль на сотрудника {} руб.!".format(int((revenue-costs)/num_of_empl)))
