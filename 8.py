name = input('Здравствуйте! Как Вас зовут? ')
print('Очень приятно, ', name, '!', ' Меня зовут Марк.', sep='')
age = int(input('Сколько Вам лет? '))
if 2024 - age > 1944:
    print('Да, ', name, ', я старше Вас на ', (2024 - age)-1944, ' лет.',
          sep='')
elif 2024 - age < 1944:
    print('Да, ', name, ', Вы старше меня на ', 1944-(2024 - age), ' лет.',
          sep='')
else:
    print('Да, ', name, ' мне тоже ', 2024 - 1944, sep='')
ans = input('Вам нравится программировать? ')
if ans == 'Да' or ans == 'да':
    print('Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.')
elif ans == 'Нет' or ans == 'нет':
    print('Жаль. Я думал, Вы сможете написать интересную программу для меня.')