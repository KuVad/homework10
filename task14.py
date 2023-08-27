# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

N = int(input("Введите число: "))

res = 0
stepen = 0

while res < N:
    res = 2 ** stepen
    if res < N:    
        print(res, end = " ")
    stepen += 1