""" Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств. """

from random import randint

array_1 = []
array_2 = []

n = int(input('введите размер множества №1: '))
m = int(input('введите размер множества №2: '))

for i in range(n):
    array_1.append(randint (1,30))
print(array_1)

for i in range(m):
    array_2.append(randint (1,30))
print(array_2)

array_3 = []
for i in array_1:
    for j in array_2:
        if i==j:
            array_3.append(i)
            break
print(array_3)



