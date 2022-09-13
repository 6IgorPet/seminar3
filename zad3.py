# 3.Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


my_list = [float(i) for i in input('Введите вещественные числа через пробел: ').split()]
print(my_list)
def min_max_fractional(lst):
    new_list = []
    for i in my_list:
        if i % 1 != 0:
            new_list.append(round(i % 1, 2))
    rez = max(new_list) - min(new_list)
    print(f'Разница между макс и мин значением дробной части элементов = {rez}')
    return

min_max_fractional(my_list)
 
new_list = [round(i % 1, 2) for i in my_list if i % 1 != 0]
print(f'Разница между макс и мин значением дробной части элементов = {max(new_list) - min(new_list)}')