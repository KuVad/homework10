# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# ыведите минимальное количество монет, которые нужно перевернуть

from random import randint

count_reshko = 0
count_orel = 0
for i in range(5):
    a = randint(0, 1)
    print(a, end = " ")
    if a == 1:
        count_orel += 1
    else:
        count_reshko += 1


print("")

if 5 == count_orel or 5 == count_reshko:  
    print("Ничего не надо переворачивать")
elif count_orel < count_reshko < 5:
    print(f'Необходимо перевернуть орлов: {count_orel}')
else:
    print(f'Необходимо перевернуть решок: {count_reshko}')