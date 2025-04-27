# Задача: Подсчёт суммы всех цифр во введённых числах
# Описание: Программа считает сумму цифр из n введённых чисел.
# Ввод: Сначала n, затем n чисел
# Вывод: Сумма всех цифр

n = int(input())
total = 0

for _ in range(n):
    number = input()
    for digit in number:
        total += int(digit)

print(total)
