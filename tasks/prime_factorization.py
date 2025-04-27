# Задача: Разложение числа на простые множители
# Описание: Программа раскладывает число n на произведение простых множителей.
# Ввод: Число n
# Вывод: Математическое выражение - произведение протсых множителей

n = int(input())

divisor = 2
first = True

while n > 1:
    if n % divisor == 0:
        if not first:
            print('*', end=' ')
        print(divisor, end=' ')
        n = n // divisor
        first = False
    else:
        divisor += 1
