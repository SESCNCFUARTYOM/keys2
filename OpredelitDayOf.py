#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
if __name__ == "__main__":
    days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 0: 'Sunday'}
    k = int(input("Введите порядковый номер дня:"))
    def dayof(k):
        day = days[k % 7]
        print(day)
    dayof(k)