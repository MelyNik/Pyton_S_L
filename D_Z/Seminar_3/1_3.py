# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011

def binary_conversion(number):
    if number == 1:
        return 1
    elif number == 0:
        return 0
    return number % 2 +10 * binary_conversion(number//2)


num = int(input('Введите число: '))

number = binary_conversion(num)
print(number)

# Или

def Filling_in_the_list(number):
    array = []
    a = num_1
    while a != 0:
        array.append(a - ((a//2) * 2))
        a = a // 2
    return array

def Flipping(array):
    k = len(array)
    my_list = []
    for i in range(len(array)):
        my_list.append(array[k-1])
        k-=1
        print(int(my_list[i]), end="")

num_1 = int(input('Введите число: '))

array = Filling_in_the_list(num_1)

Flipping(array)
