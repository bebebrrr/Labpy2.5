#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = tuple(map(int, input().split()))
    if not a:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)
    
    count=0
    p1 = None
    p2 = None
    for i, j in zip(a[:-1], a[1:]):
        if i % 2 != 0 and j % 2 != 0 and i == j:
            count += 1
            if p1 is None:
             p1 = a.index(i)
             p2 = a.index(j, p1+1)
                

    print("Количество нечётных пар: ", count)
    print("Индексы первой нечётной пары: ", p1, p2)   
