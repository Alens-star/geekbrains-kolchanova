from itertools import cycle
start_list = ['А', 'Б', 'С', 9, 0, 1]
stop_element = 0
for el in cycle(start_list):
    if stop_element > 10:
        break
    print(el)
    stop_element += 1