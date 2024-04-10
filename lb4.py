def number_1():
    def number(x):
        if x % 3 == 0:
            return True
        else:
            return False
    x = int(input("Введите число: "))
    if number(x):
        print("Число делится на 3")
    else:
        print("Число не делится на 3")
        
def number_2():
    def delenie(sto):
            vvod = 100 / sto
            return vvod
    try:
        x = float(input("Введите число: "))
        print(delenie(x))
    except ValueError:
        print("Это не число")
    except ZeroDivisionError:
            print("Это 0. На него не стоит делить")

def number_3():
    def date(da):
        day, month, year = map(int, da.split("."))
        got = year % 100
        if day * month == got:
            return True
        else:
            return False
    data = input("Введите дату! В формате дд.мм.гггг: ")
    if date(data):
        print("Это магическая дата!")
    else:
        print("Это не магическая дата")   
    
def number_4():
    def ticket(ticket_number):
        if len(ticket_number) % 2 != 0:
            return False
        z = len(ticket_number) // 2
        x = ticket_number[:z]
        y = ticket_number[z:]
        sum_x = sum(int(digit) for digit in x)
        sum_y = sum(int(digit) for digit in y)
        return sum_x == sum_y
        
    number = input("Введите номер: ")
    if ticket(number):
        print("Счастливый!")
    else:
        print("Несчастливый!")
        

while True:
    number = int(input("Введите номер задания: "))

    if number == 1:
        number_1()
    elif number == 2:
        number_2()
    elif number == 3:
        number_3()
    elif number == 4:
        number_4()
    else:
        print("Такого задания нет")