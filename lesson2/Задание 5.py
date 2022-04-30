my_list = [7, 5, 3, 3, 2]
k = 0
new_itm = input("Введите одно любое число >>> ")
try:
    new_itm = int(new_itm)
except ValueError:
    print("Вводить можно только числа. Попробуйте еще раз")
    exit()

for i in my_list:
    if new_itm >= i:
        while k != 1:
            my_list.insert(my_list.index(i) + my_list.count(i) - 1, new_itm)
            print(my_list.index(i), my_list.count(i), new_itm, k, my_list.index(i) + my_list.count(i) - 1)
            k += 1
    else:
        while k != 1:
            my_list.insert(len(my_list), new_itm)
            k += 1
print(my_list)
