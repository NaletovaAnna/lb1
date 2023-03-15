def z1():
    try:
        x = int(input('Введите число:'))
        y = x % 3
    except ValueError:
        print('Это не число :(')
    else:
        if y == 0 and x != 0:
            print('Да!', x, 'делится на 3 :)')
        elif x == 0:
            print('Оу, это ноль (-_-)')
        else:
            print('Оу,', x, 'не делится на 3 :(')
z1()

def z2():
    try:
        x = int(input('Введи число'))
        y =  100 / x
    except ValueError:
        print('Оу, ты ввел не число :(')
    except ZeroDivisionError:
        print('Оу, на ноль делить нельзя :(')
    else:
        print(y)
z2()

def z3():
    x = input('Введи любую дату в формате дд.мм.гггг:')
    x = x.split('.')
    if int(x[0]) * int(x[1]) == int(x[2][2:4]):
        print('Ооо, это магическая дата вунш пунш&$#%&*RTCVBH$%TG')
    else:
        print('Вы не попадете в Хогвартс')
z3()

def z4():
    x = input('Введи номер билета:')
    y = 0
    z = 0
    if len(x) % 2 == 0:
        for i in x[0:int(len(x) / 2)]:
            y = y + int(i)
        for i in x[int(len(x) / 2):int(len(x))+1]:
            z = z + int(i)
        if y == z:
            print('Ооо, да ты везуник :)')
        else:
            print('Несчастливый билет :(')
    else:
        print('НЕЧЕТНОЕ КОЛИЧЕСТВО ЧИСЕЛ')
z4()