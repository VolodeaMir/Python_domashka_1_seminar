# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
#  7 -> "нельзя определить"

S = int(input('Введите общие количество журавликов: '))
if S % 6 == 0:
    print(f"Петя сделал {S//6}, Катя сделала {(S//6)*4}, Сережа сделал {S//6}")
else:
    print('Вы ввели неправильное количество журавликов')
