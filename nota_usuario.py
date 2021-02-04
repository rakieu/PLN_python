# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = 80000
b = 200000
anos = 0
while a <= b:
    a = a + b * 0.03
    b = b + b * 0.015
    anos = anos + 1
print (anos)