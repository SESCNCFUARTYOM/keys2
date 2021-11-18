#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
if __name__ == "__main__":
    year = int(input("Введите год:"))
    if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 100 == 0) and (year % 400 == 0)):
        whatyear = 1
    else:
        whatyear = 0
    month = int(input("Введите номер месяца:"))
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("В этом месяце 31 день!")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("В этом месяце 30 дней!")
    else:
        if whatyear == 1:
            print("В этом месяце 29 дней!")
        else:
            print("В этом месяце 28 дней!")
