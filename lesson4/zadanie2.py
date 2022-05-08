
list_dic = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list_dic[el+1] for el in range(0, len(list_dic)-1) if list_dic[el] < list_dic[el+1]]
print(new_list)