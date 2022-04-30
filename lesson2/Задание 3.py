number = int(input("Введите номер месяца >>> "))
zima = [12, 1, 2]
vesna = [3, 4, 5]
leto = [6, 7, 8]
osen = [9, 10, 11]

seasons = {"весна":vesna, "зима":zima, "лето":leto, "осень":osen}
for key, value in seasons.items():
    if number in seasons[key]:
        print(f"Время года {key}!")
