import math
# Задание 1
phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
if (len(phrase_1) > len(phrase_2)):
    print("Фраза 1 длиннее фразы 2")
elif (len(phrase_1) < len(phrase_2)):
    print("Фраза 2 длиннее фразы 1")
else:
    print("Фразы равной длины")

# Задание 2
year = 2019
if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
    print("Високосный год")
else:
    print("Обычный год")

# Задание 3
day = int(input("Введите день:"))
month = input("Введите месяц:")
if ((month == 'Март' and day >= 21) or (month == 'Апрель' and day <= 19)):
    zodiacSign = 'Овен'
elif ((month == 'Апрель' and day >= 20) or (month == 'Май' and day <= 20)):
    zodiacSign = 'Телец'
elif ((month == 'Май' and day >= 21) or (month == 'Июнь' and day <= 20)):
    zodiacSign = 'Близнецы'
elif ((month == 'Июнь' and day >= 21) or (month == 'Июль' and day <= 22)):
    zodiacSign = 'Рак'
elif ((month == 'Июль' and day >= 23) or (month == 'Август' and day <= 22)):
    zodiacSign = 'Лев'
elif ((month == 'Август' and day >= 23) or (month == 'Сентябрь' and day <= 22)):
    zodiacSign = 'Дева'
elif ((month == 'Сентябрь' and day >= 23) or (month == 'Октябрь' and day <= 22)):
    zodiacSign = 'Весы'
elif ((month == 'Октябрь' and day >= 23) or (month == 'Ноябрь' and day <= 21)):
    zodiacSign = 'Скорпион'
elif ((month == 'Ноябрь' and day >= 22) or (month == 'Декабрь' and day <= 21)):
    zodiacSign = 'Стрелец'
elif ((month == 'Декабрь' and day >= 22) or (month == 'Январь' and day <= 19)):
    zodiacSign = 'Козерог'
elif ((month == 'Январь' and day >= 20) or (month == 'Февраль' and day <= 18)):
    zodiacSign = 'Водолей'
elif ((month == 'Февраль' and day >= 19) or (month == 'Март' and day <= 20)):
    zodiacSign = 'Рыбы'
print("Ваш знак зодиака:", zodiacSign)

# Задание 4
width = 10
length = 205
height = 5
if (width < 15 and height < 15 and length < 15):
    print("Коробка №1")
elif ((width > 15 and width < 50) or (height > 15 and height < 50) or (length > 15 and length < 50)):
    print("Коробка №2")
elif (length > 200):
    print("Упаковка для лыж")
else:
    print("Стандартная коробка №3")

# Задание 5
number = 123321
number = str(number)
sumFirstTreeNumb = int(number[0]) + int(number[1]) + int(number[2])
sumSecondTreeNumb = int(number[3]) + int(number[4]) + int(number[5])
if (sumFirstTreeNumb == sumSecondTreeNumb):
    print("Счастливый билет")
else:
    print("Несчастливый билет")
    
# Задание 6
figureType = input("Введите тип фигуры:")
if (figureType == "Круг"):
    radius = int(input("Введите радиус круга:"))
    area = math.pi * (radius**2)
    print("Площадь круга:", area)
elif (figureType == "Треугольник"):
    sideA = int(input("Введите длину стороны A:"))
    sideB = int(input("Введите длину стороны B:"))
    sideC = int(input("Введите длину стороны C:"))
    p = (sideA + sideB + sideC) / 2
    area = math.sqrt(p * (p - sideA) * (p - sideB) * (p - sideC))
    print("Площадь треугольника:", area)
elif(figureType == "Прямоугольник"):
    width = int(input("Введите ширину прямоугольника:"))
    height = int(input("Введите высоту прямоугольника:"))
    area = width * height
    print("Площадь прямоугольника:", area)
    