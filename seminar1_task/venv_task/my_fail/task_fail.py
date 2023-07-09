from my_fail import print_fail as pf

def function_menu():
    numberTask = int(input('Введите номер задачи: '))
    if 0 <= numberTask < 7:
        if numberTask == 0:
            print(pf.list_of_tasks())
            function_menu()
        elif numberTask == 1:
            print(pf.triangle_text())
            triangle()
        elif numberTask == 2:
            print(pf.simple_or_complex_text())
            simple_or_complex()
        elif numberTask == 3:
            print(pf.leap_year_text())
            leap_year()
        elif numberTask == 4:
            print(pf.what_is_the_number_entered_text())
            what_is_the_number_entered()
        elif numberTask == 5:
            print(pf.tree_star_text1())
            tree_star()
        elif numberTask == 6:
            print(pf.multiplication_table_text())
            multiplication_table()
            function_menu()
    else:
        print(pf.error_text())
        function_menu()



# Задача из дз про треугольник!
# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
def triangle():
    a = int(input('Введите первую сторону треугольника: '))
    b = int(input('Введите вторую сторону треугольника: '))
    c = int(input('Введите третью сторону треугольника: '))

    sumAB = a + b
    sumAC = a + c
    sumBC = b + c

    if a <= sumBC and b <= sumAC and c <= sumAB:
        print('Треугольник существует!')
        if a == b == c == a:
            print('Треугольник равносторонний!')
            function_menu()
        elif a != b != c != a:
            print('Треугольник разносторонний!')
            function_menu()
        elif a == b != c or b == c != a or a == c != b:
            print('Треугольник равнобедренный!')
            function_menu()
    else:
        print('Треугольник не существует!')
        function_menu()


# Задача из дз про простые или сложные числа!
# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: 
# “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def simple_or_complex():
    i = 2
    counter = 0
    NOT_SIMPLE = 1
    MIN = 0
    MAX = 100000
    number = int(input('Введите число в диапазоне от 0 до 100000: '))

    if number == 0:
        print('Вы ввели 0 и вернётесь в меню!')
        print(pf.list_of_tasks())
        function_menu()
    else:
        while True:
            if MIN < number < MAX:
                while i <= number - 1:
                    if number % i == 0:
                        counter += 1
                    i += 1
                if counter >= NOT_SIMPLE:
                    print('Число составное!')
                    simple_or_complex()
                else:
                    print('Число простое!')
                    simple_or_complex()
                break
            else:
                print('Недопустимое значение!')
                simple_or_complex()


# Задача из семинара про високосный год! "№6"
# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

def leap_year():
    year = int(input('Введите год для проверки его на високосность: '))
    if year == 0000:
        print('\nВы ввели 0 и вернётесь в меню!\n')
        print(pf.list_of_tasks())
        function_menu()
    else:
        if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
            print('Год високосный!')
            leap_year()
        else:
            print('Год не високосный!')
            leap_year()

# Задача из семинара про работу с числами! "№7"
# Пользователь вводит число от 1 до 999. 
# Используя операции с числами сообщите что введено: 
# цифра, двузначное число или трёхзначное число.

# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print
def what_is_the_number_entered():
    number = int(input('Введите число от 1 до 999: '))
    if number == 0:
        print('\nВы ввели 0 и вернётесь в меню!\n')
        print(pf.list_of_tasks())
        function_menu()
    else:
        if 0 < number < 1000:
            if 0 < number < 10:
                print('\nВы ввели однозначное число!')
                kvnum = number ** 2
                print(f'Квадрат введённой цифры {number} равен {kvnum}!\n')
                what_is_the_number_entered()
            elif 10 <= number < 100:
                print('\nВы ввели двузначное число!')
                num1 = (number % 100) // 10
                num2 = number % 10
                rezult = num1 * num2
                print(f'Произведение цифр числа {number} равно {rezult}!\n')
                what_is_the_number_entered()
            elif 100 <= number < 1000:
                print('\nВы ввели трёхзначное число!')
                numberKop = number
                n2 = 0
                while number > 0:
                    digit = number % 10
                    number = number // 10
                    n2 = n2 * 10
                    n2 = n2 + digit
                print(f'Для трёхзначного числа {numberKop} его зеркальное отображение равно {n2}!\n')
                what_is_the_number_entered()
        else:
            print('\nВы ввели неправильное число, повторите попытку!\n')
            what_is_the_number_entered()


# Задача из семинара нарисовать ёлку из *! "№8"
# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
def tree_star():
    p = int(input('Укажите число рядов ёлочки из звёздочек: '))
    if p == 0:
        print('\nВы ввели 0 и вернётесь в меню!\n')
        print(pf.list_of_tasks())
        function_menu()
    else:
        for i in range(p):
            print(' ' * (p - i), '*' * (2 * i + 1))
        print('')
        tree_star()


# Задача из семинара про таблицу умножения! "№9"
def multiplication_table():
    for i1 in range(1, 11):
        for k1 in range(2, 6):
            print(f'{k1} * {i1} = {i1 * k1}\t', end='')
        print('')
    print()
    for i2 in range(1, 11):
        for k2 in range(6, 10):
            print(f'{k2} * {i2} = {i2 * k2}\t', end='')
        print('')
    print()