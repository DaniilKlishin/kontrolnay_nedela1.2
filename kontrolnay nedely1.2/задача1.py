import math

a= int(input('Введите a: '))
b= int(input('Введите b: '))
c= int(input('Введите c: '))
if a>b and a>c:
    print(f'{a}')
if b>a and b>c:
    print(f'{b}')
if c>a and c>b:
    print(f'{c}')