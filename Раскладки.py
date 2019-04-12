import sys
a = input('Введите язык (Ru/Eng) -->')
a = a.rstrip()
if a != 'Ru' and a != 'Eng':
    print('Такого языка нет в программе!')
    sys.exit(-1)
Rd = dict()
Ed = dict()
R1 = 'абвгдеёжзийклмнопрстуфхцшщьъыэюяЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
E1 = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
R = r'''йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ бю1234567890!-+=*()%,.'''
E = r'''qwertyuiop[]asdfghjkl;'zxcvbnm,.`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>~ ,.1234567890!-+=*()%?/'''
for i in range(len(R)):
    Rd[R[i]] = E[i]
    Ed[E[i]] = R[i]
text2 = ''
text = input('Введите текст -->')
if a == 'Ru':
    for i in range(len(text)):
        if text[i] in E1:
                print('Введён неправильный язык!')
                sys.exit(-1)
if a == 'Eng':
    for i in range(len(text)):
        if text[i] in R1:
                print('Введён неправильный язык!')
                sys.exit(-1)
if a == 'Ru':
    for i in range(len(text)):
        text2 += Rd[text[i]]
elif a == 'Eng':
    for i in range(len(text)):
        text2 += Ed[text[i]]
print('Правильный текст -->' + text2)