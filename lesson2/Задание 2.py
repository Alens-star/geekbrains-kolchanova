string = input("введите любое слово или набор символов >>> ")
list_symbols = list(string)
i = 0

if len(string) > 1 and len(string) % 2 == 0:
    while i != len(string):
        list_symbols[i+1], list_symbols[i] = list_symbols[i], list_symbols[i+1]
        i += 2
    result_string = ''.join(list_symbols)
elif len(string) > 1 and len(string) % 2 != 0:
    while i != len(string) - 1:
        list_symbols[i + 1], list_symbols[i] = list_symbols[i], list_symbols[i + 1]
        i += 2
    result_string = ''.join(list_symbols)
else:
    print("Необходимо ввести хотя бы 2 символа")
print(result_string)

