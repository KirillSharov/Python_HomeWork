"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
5 -> 1 0 1 1 0
2
"""
import random

coins = int(input("Введите количество монет: "))
count_eagle, count_tails = 0, 0
print(coins, "->", end=" ")
for i in range(coins):
    coin = random.randrange(0, 2)
    print(coin, end=" ")
    if coin == 0:
        count_eagle += 1
    else:
        count_tails += 1
print()
if count_eagle < count_tails:
    print(count_eagle)
else:
    print(count_tails)