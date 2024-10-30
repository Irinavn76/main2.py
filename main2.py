try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print("Первое число:", num1)
    print("Второе число:", num2)
except ValueError:
    print("Ошибка: введено неверное значение!")


message = '''
Выберете математическую операцию:
+ : Сложение
- : Вычитание
/ : Деление
* : Умножение
Ваш выбор:
'''

operation = input(message)

if operation == '+':
    print('Сложение')
    result = num1 + num2
elif operation == '-':
    print('Вычитание')
    result = num1 - num2
elif operation == '*':
    print('Умножение')
    result = num1 * num2
elif operation == '/':
    print('Деление')
    if num2 != 0:
        result = num1 / num2
    else:
        print("На ноль делить нельзя!")
else:
    print('Неизвестная операция')


print("Результат:", result)