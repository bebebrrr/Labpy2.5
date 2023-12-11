#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = tuple(map(int, input().split()))
    if not a:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)
    
    count=0
    for i, _ in enumerate(a):
     if a[i-1] % 2 != 0 and a[i] % 2 != 0 and a[i] == a[i-1]:
        count += 1
            

    for i, _ in enumerate(a):
     if a[i-1] % 2 != 0 and a[i] % 2 != 0 and a[i] == a[i-1]:
            p1=i - 1
            p2=i 
            break

    print("Количество нечётных пар: ", count)
    print("Индексы первой нечётной пары: ", p1, p2)   
