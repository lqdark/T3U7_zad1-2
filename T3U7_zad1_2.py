# -*- coding: cp1251 -*-
stroka=input('Задача1. Введите строку:')
if stroka == stroka[::-1]:
    print('yes')
else:
    print('no')
    


stroka='aasdasd   asdasdasdasd      asdasdasda                               sdasd'
print(f'Задача2. Дана строка -- {stroka}')
print(' '.join(stroka.split()))