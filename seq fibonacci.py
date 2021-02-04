# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = int(input("Número: "))
b = int(input("Número 2: "))

while a % b != 0:
    a, b = b, a%b
    print (f'mdc = {b}')
