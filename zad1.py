# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.


spisok = [2, 3, 5, 9, 3]

def sum_ht(ls):
    sum = 0
    for k in range(len(spisok)):
        if k % 2 != 0 and k != 0:
            sum += spisok[k]
        else:
            k += 1
    return sum

print(sum_ht(spisok))
 
spis = [int(i) for i in input('Введите числа через пробел: ').split()]

def summ_ht(lst):
    lst = spis[1::2]
    print(lst)
    print(sum(lst))
    return

summ_ht(spis)