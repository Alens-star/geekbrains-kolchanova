
x = 0
list_str = []
with open("text_file.txt", "r", encoding = "UTF-8") as my_f:
    for line in my_f:
        list_str.append(len(line))
        x+=1
print(f"Количество строк:{x} и длина каждой строки:{list_str}")