def divide_func(num = int(input("Введите числитель >>> ")), den = int(input("Введите знаменатель >>> "))):
   try:
       result = num/den
   except ZeroDivisionError:
       result = 0
   return result

print(divide_func())
