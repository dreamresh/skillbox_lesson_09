print('Задача 2. Я стал новым пиратом!')

#Старому капитану необходимо пополнить команду.
# Но попадут на его корабль только достойные!
# Он отобрал 10 человек и те, кто из них крикнет слово “Карамба”, попадут на борт.
#
# Пользователь вводит 10 слов.
#
# Напишите программу,
# которая определяет, сколько из них совпадают со словом “Карамба”.

count = 0
for _ in range(10):
    alarm = input('Что кричит пират!?\n').lower().strip('! ,.?+=')
    if alarm == 'карамба':
        count += 1

if count == 0:
    print('Карамба! Пойдём искать в другом месте!')
else:
    print('Отлично! У нас', count, 'достойнейших пиратов!')
    