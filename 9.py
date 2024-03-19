length = input('Собака корoткошёрстной породы? ')
if length == 'Да' or length == 'да':
    height1 = input('Рост собаки менее 50 см? ')
    if height1 == 'Да' or height1 == 'да':
        tail = input('У собаки короткий хвост? ')
        if tail == 'Да' or tail == 'да':
            print('Английский бульдог')
        elif tail == 'Нет' or tail == 'нет':
            ears = input('У собаки длинные уши? ')
            if ears == 'Да' or ears == 'да':
                print('Гончая')
            elif ears == 'Нет' or ears == 'нет':
                body = input('У собаки короткое тело? ')
                if body == 'Да' or body == 'да':
                    print('Мопс')
                elif body == 'Нет' or body == 'нет':
                    print('Чихуахуа')
    elif height1 == 'Нет' or height1 == 'нет':
        weight = input('Собака весит более 50 кг? ')
        if weight == 'Да' or weight == 'да':
            print('Датский дог')
        elif weight == 'Нет' or weight == 'нет':
            print('Фоксхаунд')
elif length == 'Нет' or length == 'нет':
    height1 = input('Рост собаки менее 50 см? ')
    if height1 == 'Да' or height1 == 'да':
        nature = input('У собаки доброжелательный характер? ')
        if nature == 'Да' or nature == 'да':
            print('Кокер-спаниэль')
        elif nature == 'Нет' or nature == 'нет':
            print('Ирландский сеттер')
    elif height1 == 'Нет' or height1 == 'нет':
        height2 = input('У собаки рост менее 70 см? ')
        if height2 == 'Да' or height2 == 'да':
            ears = input('У собаки длинные уши? ')
            if ears == 'Да' or ears == 'да':
                print('Большой вандейский грифон')
            elif ears == 'Нет' or ears == 'нет':
                print('Колли')
        elif height2 == 'Нет' or height2 == 'нет':
            colour = input('Окрас рыжий с белыми отметинами? ')
            if colour == 'Да' or colour == 'да':
                print('Сенбернар')
            elif colour == 'Нет' or colour == 'нет':
                white = input('Белоснежный окрас? ')
                if white == 'Да' or white == 'да':
                    print('Ирландский волкодав')
                elif white == 'Нет' or white == 'нет':
                    print('Ньюфаундленд')

