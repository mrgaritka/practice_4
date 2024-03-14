import datetime as d

name = input('Здравствуйте! Как Вас зовут? ')
print('Очень приятно, ', name, '!', ' Меня зовут Марк.', sep='')
age = int(input('Сколько Вам лет? '))
if d.datetime.now().year - age > 1944:
    print('Да, ', name, ', я старше Вас на ', (d.datetime.now().year - age)-1944, ' лет.',
          sep='')
elif d.datetime.now().year - age < 1944:
    print('Да, ', name, ', Вы старше меня на ', 1944-(d.datetime.now().year - age), ' лет.',
          sep='')
else:
    print('Да, ', name, ' мне тоже ', d.datetime.now().year-1944, sep='')
ans = input('Вам нравится программировать? ')
if ans == 'Да' or ans == 'да':
    print('Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.')
elif ans == 'Нет' or ans == 'нет':
    print('Жаль. Я думал, Вы сможете написать интересную программу для меня.')