# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ("inteiros positivos ímpares")

n = int(input("Digite um int positivo para n: "))

print ("Os", n, "primeiros inteiros positivos ímpares são:")

impar = 1 #impar armazena os inteiros positivos impares
cont = 0 # cont representa a quantidade de ímpares impressos
while cont < n:
    print (impar)
    impar = impar + 2
    cont = cont + 1
