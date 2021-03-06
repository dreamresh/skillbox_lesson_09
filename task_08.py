print('Задача 8. Колонтитул')

# Нам нужно написать программу для печати важных объявлений.
# Сверху объявления должен располагаться вот такой колонтитул:
#  ~~~~~~~~~~!!!!!!~~~~~~~~~~
# Восклицательные знаки всегда располагаются по центру строки,
# причём в зависимости от важности объявления количество восклицательных знаков может быть разным.
#
# Напишите программу,
# которая спрашивает у пользователя сначала общую длину колонтитула в символах,
# потом желаемое количество восклицательных знаков,
# после чего выводит на экран готовую строку.

total_length_footer = int(input('Укажите общую длину колонтитула в символах: '))
number_exclamation_marks = int(input('Укажите количество восклицательных знаков: '))

half_symbol_footer = (total_length_footer - number_exclamation_marks) // 2

footer = half_symbol_footer * '~' + number_exclamation_marks * '!' + half_symbol_footer * '~'

print(footer)