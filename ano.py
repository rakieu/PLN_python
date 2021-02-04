# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:09:02 2020

@author: raque
"""

a = int(input('Ano:'))
if a % 4 == 0 and (a % 100 != 0 or a % 400 ==0):
    print ('Bissexto')
else:
    print ('Não é bissexto')
input ()