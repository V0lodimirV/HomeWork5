def func1():
    print('***** функция 1 *****')
    my_string = (input(('введите предложение(функция1):\n'))).split(' ')
    my_string1 = '.'.join(my_string)
    print(my_string1)

def func2():
    print('***** функция 2 *****')
    my_string = input(str('Введите предложение(функция2):\n ')).replace(' ','')
    if my_string != my_string[::-1]:
        print('не является палиндромом')
    else:
        print('является палиндромом')


def func3():
    print('***** функция 3 *****')
    lst_1 = list(input('введите элементы:\n'))
    for i in lst_1:
        if lst_1.count(i) == 1:
            print(i, end=' ')


def func4():
    print('***** функция 4 *****')
    lst_1 = list(input('введите числа:\n').split())
    lst_2 = list(input('введите еще числа:\n').split())
    lst_3 = lst_1 + lst_2
    print('различных чисел:\n', len(set(lst_3)))


def runner(*function):
    if len(function) == 0:
        func1()
        func2()
        func3()
        func4()
    else:
        for i in function:
            globals()[i]()


