str_input = 1

with open("write_file.txt", "w") as write_f:
    while str_input !="":
        str_input = input("Введите данные. Чтобы выйти нажмите Enter >>> ")
        string = f"{str_input}\n"
        write_f.writelines(string)
