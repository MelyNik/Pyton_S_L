# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве. 

number_x_A = float(input('Введите координату "х" точки "А": '))
number_y_A = float(input('Введите координату "y" точки "А": '))
number_x_B = float(input('Введите координату "x" точки "B": '))
number_y_B = float(input('Введите координату "y" точки "B": '))

print(round(((((number_x_A-number_x_B)**2)+((number_y_A-number_y_B))**2)**(0.5)),2))
