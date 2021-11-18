#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
if __name__ == "__main__":
   n = int(input("Введите кол-во месяце, прошедших с начала года:"))
   match n:
       case 0:
           print("Январь")
       case 1:
           print("Февраль")
       case 2:
           print("Март")
       case 3:
           print("Апрель")
       case 4:
           print("Май")
       case 5:
           print("Июнь")
       case 6:
           print("Июль")
       case 7:
           print("Август")
       case 8:
           print("Сентябрь")
       case 9:
           print("Октябрь")
       case 10:
           print("Ноябрь")
       case 11:
           print("Декабрь")