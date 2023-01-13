import random


def is_valid(number, left_valid, right_valid):
    flag = True
    if not number.isdigit():
        flag = False
    elif not left_valid <= int(number) <= right_valid:
        flag = False
    return flag


def is_print(number):
    n = number
    if n > 99:
        n %= 100
    if n in (1, 21, 31, 41, 51, 61, 71, 81, 91):
        return 'За ' + str(number) + ' попытку.'
    elif n in (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94):
        return 'За ' + str(number) + ' попытки.'
    else:
        return 'За ' + str(number) + ' попыток.'


def is_guess():
    print('Введите число обозночающее левую границу:')
    left = int(input())
    print('Введите число обозночающее правую границу:')
    right = int(input())
    num = random.randint(left, right)
    print(num)
    count = 1
    while True:
        print('Попытка', count)
        n = input()
        if is_valid(n, left, right):
            if int(n) > num:
                print('Ваше число больше загаданного. Попробуйте еще раз:')
            elif int(n) < num:
                print('Ваше число меньше загаданного. Попробуйте еще раз:')
            else:
                print('Вы угадали число.', is_print(count), 'Молодец!!!')
                break
        else:
            print('Вы ввели не правильное число или символ. Попробуйте еще раз:')
            count += 1
            continue
        count += 1


print('Добро пожаловать в игру "Угадайка"')
is_guess()
flag = True
while flag:
    print('Если хотите сыграть еще, нажмите 1')
    if int(input()) == 1:
        is_guess()
    else:
        print('Счастливого дня.')
        flag = False
