def z1():
    x = int(input('Введите число: '))
    y = [3, 5, 17, 99, 67]
    if x in y:
        print("Вот загаданные числа: ", y, '\n', "Вот твое число: ", x, '\n', 'Молодец! Ты угадал число :)')
    else:
        print("Вот загаданные числа: ", y, '\n', "Вот твое число: ", x, '\n', 'Упс. Ты не угадал число :(')


def z2():
    slovo = ['котик', 'сирень', 'небо', 'котик']
    povtor = {str(x) for x in slovo if slovo.count(x) > 1}
    x = lambda: print('nothing')
    y = lambda: print(' '.join(povtor))
    x() if len(povtor) < 1 else y()


def z3():
    week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sun', 'Sut')
    weekends = int(input())
    print('Weekends:', week[:-weekends - 1:-1])
    print('Work days:', week[:-weekends])


def z4():
    import random
    a = ['Черепов', 'Булашева', 'Бахия', 'Шарипова', 'Налетова']
    b = ['Иванова', 'Исхаков', 'Павлова', 'Елизарова', 'Сергеев']
    v = a + b
    print("Все студенты: ", ', '.join(v), '\n')

    random.shuffle(a)
    while len(a) < 5:
        a.append(random.randint(0, 5))
    x = a[:3:]

    random.shuffle(b)
    while len(b) < 5:
        b.append(random.randint(0, 5))
    y = b[:3:]

    c = x + y
    c = sorted(c)
    print("Члены спортивной команды: ", ', '.join(c))
    print(len(c), '\n')

    if 'Иванова' in c:
        print("Студент Иванова входит в список членов спортивной команды.")
    else:
        print("Студент Иванова не входит в список членов спортивной команды.")
    print(c.count("Иванова"))

z4()