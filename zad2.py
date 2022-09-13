# 2.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


spsk = [7, 9, 77, 3, 10]

def pair_numb(lst):
    sqrt = []
    for i in range((len(lst) + 1) // 2):
        sqrt.append(lst[i] * lst[len(lst)-1-i])
    return sqrt

print(pair_numb(spsk))