from itertools import count
start_element = int(input("C какого значения генерировать числа? >>> "))
stop_element = 0

for el in count(start_element):
    if stop_element == 10:
        break
    else:
        print(el)
        stop_element+=1