zp = ""
list_empl_20 = []
list_zp = []
x = 0
with open("zarplaty.txt", "r", encoding = "UTF-8") as my_f:
    for line in my_f:
        x += 1
        zp_list = line.split(" ")
        zp = float(zp_list[1].replace("\n", "").replace(",", "."))
        empl = zp_list[0]
        list_zp.append(zp)
        if zp < 20000:
            list_empl_20.append(empl)
print(f"Сотрудники c зарплатой меньше 20 тыс: {list_empl_20}.\nСредняя зарплата:{round(sum(list_zp)/x)}")