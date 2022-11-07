# Перевірка на високосний рік

year = int (input ('Enter the Year: '))
if year % 4 == 0 and year % 100 != 0:
    print ('YES')
elif year % 400 == 0:
    print('YES')
else:
    print ('NO')

#Високосний рік
year_1 = int(input('Year: '))
high_year = year_1 % 4 == 0 and year_1 % 100 != 0 or year_1 % 400 == 0
if high_year:
    print('Yes')
else:
    print('No')


# Задача fizz bizz

fizz = int(input('fizz: '))
buzz = int(input('buzz: '))
fizz_buzz = int(input('fizz_buzz: '))

for fizz_buzz in range(1, fizz_buzz + 1):
    if (fizz_buzz % fizz == 0) and (fizz_buzz % buzz == 0):
        print('FB')
    elif fizz_buzz % fizz == 0:
        print('F')
    elif fizz_buzz % buzz == 0:
        print('B')
    else:
        print(fizz_buzz)