import math

a= int(input('Введите a: '))
b= int(input('Введите b: '))
c= int(input('Введите c: '))
if a+b>c and b+c>a and a+c>b:
    print("Треугольник может существовать")
if a+b<c or b+c<a or a+c<b:    
    print('Треугольник не может существовать')