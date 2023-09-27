import math

a= int(input('Введите a: '))
b= int(input('Введите b: '))
c= int(input('Введите c: '))
if (a == b) or (a == c) or (b == c) or ((a == b) and (b == c)):
    print("Ошибка")
if ((a > b) and (a < c)) or ((a < b) and (a > c)):
    print(f'{a}')
if ((b > a) and (b < c)) or ((b < a) and (b > c)) :
    print(f'{b}')
if ((c > a) and (c < b)) or ((c < a) and (c > b)):
    print(f'{c}')