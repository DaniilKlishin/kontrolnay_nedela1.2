import math

a= float(input('Введите координату: '))
b= float(input('Введите радиус: '))
if a > b:
    print("Точка не пренадлижинт кругу")
if a < b:
    print("Координата пренадлижинт кругу")