# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

soma = 0
n = 0
while True:
    x = int(input('n (zero sai): '))
    if x == 0:
        break
    else:
        n = n + 1
        soma = soma + x
print (f'Média: {soma/n:.1f}')
