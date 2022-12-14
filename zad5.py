# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# #- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Please, input number: '))

def fibonacci(num):
    fibo = []
    n1, n2 = 1, 1
    for i in range(num):
        fibo.append(n1)
        n1, n2 = n2, n1 + n2
    n1, n2 = 0, 1
    for i in range(num+1):
        fibo.insert(0, n1)
        n1, n2 = n2, n1 - n2
    return fibo

print(fibonacci(number))