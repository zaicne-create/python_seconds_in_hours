#Задача 1. Вводим время в часах. А в минутах и секундах?
# 1 час = 60*60 минут = 3600 сек

import math
seconds_in_a_day = 24*60*60
print(f'Секунд в дне {seconds_in_a_day}')
seconds = int(input('Введите время в секундах, прошедшее с начала дня: '))
seconds_end_day = seconds_in_a_day - seconds
minutes_end_day = seconds_end_day/60
hours_end_day = minutes_end_day/60
print(f'До конца дня осталось {hours_end_day} часов\n'
      f'или {minutes_end_day} минут\nили {seconds_end_day} секунд')
seconds_in_a_day2  = 24*60*60
seconds2 = 20000 # это 1 час 2 минута 1 секунда, до конца дня 22 часа 59 минут 59 секунд
hours = (seconds_in_a_day2 - seconds2)//60//60
print(f'Часы {hours}')
minutes = math.ceil((((seconds_in_a_day2 - seconds2)/60/60) - hours))
# minutes = (seconds_in_a_day2 - seconds2)//60
# minutes = (seconds_in_a_day2 - seconds2) % 60
print(f'Минуты {minutes}')
seconds_left = minutes % 60
print(f'Секунды {seconds_left}')