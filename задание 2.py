'задание 2'
minutes_start = float(input("Введите количество минут"))
hours = int(minutes_start // 60)
minutes = int(minutes_start % hours)
seconds = int((minutes_start -hours*60-minutes)*60)
print("{}:{}:{}".format(hours, minutes, seconds))
