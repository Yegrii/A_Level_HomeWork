# 1.Створити три рядки.
# 	Створити алгоритм виведення на екран
# 	середини(мається на увазі символ або символи які стоять в середині рядка)
# 	кожного із трьох рядків введених з клавіатури.

f_input = str(input('First: '))
s_input = str(input('Second: '))
t_input = str(input('Third: '))

if len(f_input) % 2 == 0:
    mid_f = len(f_input) // 2
    print('Your symbols are --> ', f_input[mid_f - 1], f_input[mid_f])
elif len(f_input) % 2 != 0:
    mid_f = len(f_input) // 2
    print('Your symbol is --> ', f_input[mid_f])

if len(s_input) % 2 == 0:
    mid_s = len(s_input) // 2
    print('Your symbols are --> ', s_input[mid_s - 1], s_input[mid_s])
elif len(s_input) % 2 != 0:
    mid_s = len(s_input) // 2
    print('Your symbol is --> ', s_input[mid_s])

if len(t_input) % 2 == 0:
    mid_t = len(t_input) // 2
    print('Your symbols are --> ', t_input[mid_t - 1], t_input[mid_t])
elif len(t_input) % 2 != 0:
    mid_t = len(t_input) // 2
    print('Your symbol is --> ', t_input[mid_t])

# 2.Створити рядок розмір, якого не менше 5 символів і не більше 15,
# 	Обміняти місцями половини рядка при чому в другій половині рядка перетворити останні 3 літери у великі.

str_1 = 'Qwertyasdfghzx'
if len(str_1) >= 5 and len(str_1) <= 15:
    str_1 = str_1[len(str_1)//2:] + str_1[:len(str_1)//2].replace('tya', 'TYA')
    print("Changed string: ", str_1)
else:
    print('This string is too short or too long')

# 3.Створити рядок розміром не більше 10 символів та останні три
# 	символи перетворити на маленькі літери та перемістити в середину остачі символів(окрім 3ох останніх) рядка.

str_2 = 'QWEASDZXCK'

if len(str_2) <= 10:
    if str_2.isupper():
        str_2 = str_2.replace(str_2[-3:], str_2[-3:].lower())
        str_2 = str_2[:(len(str_2) - 3) // 2] + str_2[-3:] + str_2[(len(str_2) - 3) // 2:-3]
        print('Upper string: ', str_2)
    elif str_2.islower():
        str_2 = str_2.replace(str_2[-3:], str_2[-3:].upper())
        str_2 = str_2[:(len(str_2) - 3) // 2] + str_2[-3:] + str_2[(len(str_2) - 3) // 2:-3]
        print('Lower string: ', str_2)
else:
    print('ERROR')

# 4. Створити алгоритм, який дозволить вивести на екран
# 	(порожній, тобто лише межі квадрата) квадрат із символів #
# 	Можна використовувати лише(всі інші можна окрім операторів виводу) наступні оператори print:
# 	print("#",end="")
# 	print(" ",end="")
# 	print("") #перехід на новий рядок, якщо треба.
# 	Вище буде оцінено рішення з введенням розміру квадрата з клавіатури)

num = int(input('Введіть розмір квадратy: '))
for i in range(num):
    for y in range(num):
        if i == 0 or y == 0 or i == num - 1 or y == num - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print("")