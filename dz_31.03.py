#!/usr/bin/env python
# coding: utf-8

# In[2]:


phrase_1 = input('Введите первую фразу:')
phrase_2 = input('Введите вторую фразу:')
if len(phrase_1) > len(phrase_2): #считаем количество символов в строке и сравниваем
    print('Фраза 1 длиннее фразы 2')
elif len(phrase_1) < len(phrase_2):
    print('Фраза 2 длиннее фразы 1')
else:
    print('Фразы равной длины') #если длины строк не различаются, то выводим, что они равны


# In[14]:


year = input('Введите год: ')
if int(year)%400 == 0: #високосный год кратен 400
    print('Високосный год')
elif int(year)%100 == 0: #невисокосный год кратен 100
    print('Обычный год')
elif int(year)%4==0: #високосный год кратен 4
    print('Високосный год')
else:
    print('Обычный год')


# In[ ]:


day = int(input('Введите число: '))
month = input('Введите месяц: ')
if ((day >= 21 and day <= 31) and month == 'март') or ((day >= 1 and day <= 19) and month == 'апрель'): #устанавливаем диапазон дат и месяц
    print('Ваш знак зодиака: Овен')
elif ((day >= 21 and day <= 30) and month == 'апрель') or ((day >= 1 and day <= 20) and month == 'май'):
    print('Ваш знак зодиака: Телец')
elif ((day >= 21 and day <= 31) and month == 'май') or ((day >= 1 and day <= 20) and month == 'июнь'):
    print('Ваш знак зодиака: Близнецы')
elif ((day >= 21 and day <= 30) and month == 'июнь') or ((day >= 1 and day <= 22) and month == 'июль'):
    print('Ваш знак зодиака: Рак')
elif ((day >= 23 and day <= 31) and month == 'июль') or ((day >= 1 and day <= 22) and month == 'август'):
    print('Ваш знак зодиака: Лев')
elif ((day >= 23 and day <= 31) and month == 'август') or ((day >= 1 and day <= 22) and month == 'сентябрь'):
    print('Ваш знак зодиака: Дева')
elif ((day >= 23 and day <= 30) and month == 'сентябрь') or ((day >= 1 and day <= 22) and month == 'октябрь'):
    print('Ваш знак зодиака: Весы')
elif ((day >= 23 and day <= 31) and month == 'октябрь') or ((day >= 1 and day <= 21) and month == 'ноябрь'):
    print('Ваш знак зодиака: Скорпион')
elif ((day >= 22 and day <= 30) and month == 'ноябрь') or ((day >= 1 and day <= 21) and month == 'декабрь'):
    print('Ваш знак зодиака: Стрелец')
elif ((day >= 22 and day <= 31) and month == 'декабрь') or ((day >= 1 and day <= 19) and month == 'январь'):
    print('Ваш знак зодиака: Козерог')
elif ((day >= 20 and day <= 31) and month == 'январь') or ((day >= 1 and day <= 18) and month == 'февраль'):
    print('Ваш знак зодиака: Водолей')
elif ((day >= 19 and day <= 29) and month == 'февраль') or ((day >= 1 and day <= 20) and month == 'март'):
    print('Ваш знак зодиака: Рыбы')
else:
    print('Ошибка!')


# In[20]:


width = 10
length = 205
height = 5
if width < 15 and length < 15 and height < 15: #все стороны менее 15 см
    print('Коробка №1')
elif (width > 15 or width < 50) or (length > 15 or length < 50) or (height > 15 or height < 50): #хотя бы одна из сторон больше 15, но меньше 50 см
    print('Коробка №2')
elif length > 200: # длина больше 2 м
    print('Упаковка для лыж')
else: # остальные
    print('Стандартная коробка №3')


# In[18]:


number = list(input('Введите шестизначное число: ')) # преобразуем в список
if int(number[0])+int(number[1])+int(number[2]) == int(number[3])+int(number[4])+int(number[5]): # преобразуем каждый элемент списка в чтсла и сравниваем сумму первых трех и вторых трех
    print('Счастливый билет')
else:
    print('Несчастливый билет')


# In[33]:


figure = input('Введите тип фигуры: ')
if figure == 'круг':
    radius = input('Введите радиус круга: ')
    from math import pi
    sround = math.pi * (int(radius)**2)
    print('Результат: ')
    print('Площадь круга: ' + str(sround))
elif figure == 'треугольник':
    triangle_a = input('Введите длину стороны A: ')
    triangle_b = input('Введите длину стороны B: ')
    triangle_c = input('Введите длину стороны C: ')
    p = (int(triangle_a)+ int(triangle_b)+ int(triangle_c))/2
    from math import sqrt
    striangle = sqrt(p*(p-int(triangle_a))*(p-int(triangle_b))*(p-int(triangle_c)))
    print('Результат: ')
    print('Площадь круга: ' + str(striangle))
elif figure == 'прямоугольник':
    rectangle_a = input('Введите длину стороны A: ')
    rectangle_b = input('Введите длину стороны B: ')
    srectangle = int(rectangle_a)*int(rectangle_a)
    print('Результат: ')
    print('Площадь прямоугольниа: ' + str(srectangle))

