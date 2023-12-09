#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = tuple(map(int, input().split()))
    if not a:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)
    
    count=0
    for i in range(1, len(a) + 1, 2):
     if a[i-1] % 2 != 0 and a[i] % 2 != 0:
        count += 1
    print(count)   
   