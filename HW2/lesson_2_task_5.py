def month_to_season(n):
    if n in [12, 1, 2]:
        result = 'Зима'
    elif n in [3, 4, 5]:
        result = 'Весна'
    elif n in [6, 7, 8]:
        result = 'Лето'
    elif n in [9, 10, 11]:
        result = 'Осень'
    else:
        result = 'Ошибка ввода' 
    print(result)
month_to_season(13)