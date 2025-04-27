n = int(input())

divisor = 2  # Начинаем с самого маленького простого числа
first = True  # Флаг, чтобы не ставить '*' перед первым множителем

while n > 1:
    if n % divisor == 0:
        if not first:
            print('*', end=' ')
        print(divisor, end=' ')
        n = n // divisor  # Уменьшаем n
        first = False
    else:
        divisor += 1  # Пробуем следующий делитель
