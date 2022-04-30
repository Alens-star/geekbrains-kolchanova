words = input("Введите несколько слов через пробел >>> ")
split_words = words.split(" ")
for i in split_words:
    if len(i) < 10:
        print("{} {}".format(split_words.index(i)+1, i))
    else:
        print("{} {}".format(split_words.index(i)+1, i[:10:]))
