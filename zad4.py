# '''4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.


number = int(input('Пожалуйста, введите целое число: '))

def binar_preob(num):
    res = ''
    while num > 0:
        res = str(num % 2) + res
        num = num // 2
    return res

print(f'Binary: {binar_preob(number)}')

print(bin(int(input('Пожалуйста, введите целое число: '))))
