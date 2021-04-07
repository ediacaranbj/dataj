#!/usr/bin/env python
# coding: utf-8

# ### Задание 1

# In[ ]:


word = input('Введите слово: ')
length = len(str(word))
middle = int(length // 2)
if length%2==0:
    print(str(word[middle-1])+str(word[middle]))
else:
    print(word[middle])


# ### Задание 2

# In[61]:


number = int(input('Введите число: '))
count = 0
while number != 0:
    count += number
    number = int(input('Введите число: '))
print(count)


# ### Задание 3

# In[119]:


boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys_sorted = sorted(boys)
girls_sorted = sorted(girls)
pairs = zip(boys_sorted, girls_sorted)
pairs_zip = list(pairs)
print(str(pairs_zip[0][0])+ ' и ' +str(pairs_zip[0][1]))
print(str(pairs_zip[1][0])+ ' и ' +str(pairs_zip[1][1]))
print(str(pairs_zip[2][0])+ ' и ' +str(pairs_zip[2][1]))
print(str(pairs_zip[3][0])+ ' и ' +str(pairs_zip[3][1]))
print(str(pairs_zip[4][0])+ ' и ' +str(pairs_zip[4][1]))


# ### Задание 4

# In[115]:


countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
thai_middle = (float(countries_temperature[0][1][0])+float(countries_temperature[0][1][1])+float(countries_temperature[0][1][2])+float(countries_temperature[0][1][3])+float(countries_temperature[0][1][4])+float(countries_temperature[0][1][5])+float(countries_temperature[0][1][6]))/7
de_middle = (float(countries_temperature[1][1][0])+float(countries_temperature[1][1][1])+float(countries_temperature[1][1][2])+float(countries_temperature[1][1][3])+float(countries_temperature[1][1][4]))/5
ru_middle = (float(countries_temperature[2][1][0])+float(countries_temperature[2][1][1])+float(countries_temperature[2][1][2])+float(countries_temperature[2][1][3])+float(countries_temperature[2][1][4])+float(countries_temperature[2][1][5])+float(countries_temperature[2][1][6]))/7
pl_middle = (float(countries_temperature[3][1][0])+float(countries_temperature[3][1][1])+float(countries_temperature[3][1][2])+float(countries_temperature[3][1][3])+float(countries_temperature[3][1][4])+float(countries_temperature[3][1][5]))/6
K_thai = 273.15 + ((thai_middle - 32.0) * (5.0/9.0))
K_de = 273.15 + ((de_middle - 32.0) * (5.0/9.0))
K_ru = 273.15 + ((ru_middle - 32.0) * (5.0/9.0))
K_pl = 273.15 + ((pl_middle - 32.0) * (5.0/9.0))
C_thai = round((K_thai - 273.15), 1)
C_de = round((K_de - 273.15), 1)
C_ru = round((K_ru - 273.15), 1)
C_pl = round((K_pl - 273.15), 1)
print('Средняя температура в странах: ')
print('Таиланд - ' + str(C_thai) + ' C')
print('Германия - '+ str(C_de) + ' C')
print('Россия - ' + str(C_ru) + ' C')
print('Польша - ' + str(C_pl) + ' C')

