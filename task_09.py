print('Задача 9. Коровы')

# Для коров есть 10 стойл.
# В каждом стойле разные условия для животных, поэтому и молока они дают по-разному.
# В первом стойле производят 2 литра в день,
# во втором 4, 
# в третьем - 6, потом 8, 10, 12, 14, 16, 18, 20. 
# Но коровы стоят не во всех стойлах. 
# Свободные и занятые обозначаются строкой из букв a и b,
# где a - свободное стойло, b - занятое.
# 
# Пользователь вводит строку из 10 символов a и b.
# Необходимо определить, сколько в итоге будет произведено молока за день.

stall = input('Введите строку для обозначения свободиных (a) и занятых (b) мест: ')
step = 0
milk_yield = 0
for place in stall:
    step += 2
    if place == 'b':
        milk_yield += step

print('За день будет получено', milk_yield, 'л молока')