# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
nota = float(input("Digite a nota: "))
while nota < 0 or nota > 10:
    print ('Notas entre 0 e 10: ')
    nota = float(input('Digite uma nota: '))
else:
    print ("Correto!")
