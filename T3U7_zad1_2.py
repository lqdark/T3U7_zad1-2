# -*- coding: cp1251 -*-
stroka=input('������1. ������� ������:')
if stroka == stroka[::-1]:
    print('yes')
else:
    print('no')
    


stroka='aasdasd   asdasdasdasd      asdasdasda                               sdasd'
print(f'������2. ���� ������ -- {stroka}')
print(' '.join(stroka.split()))