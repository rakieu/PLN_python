# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ("calcula a soma de n numeros inteiros para um dado n")
n = int(input("Digite um inteiro positivo(valor de n): "))
soma = 0
cont = 0
while cont < n:
    num = int(input("Digite um numero inteiro qualquer: "))
    soma = soma + num
    cont = cont + 1
    print("Soma dos", cont, "primeiros elementos = ", soma)

print ("Soma dos", n, "numeros dados = ", soma)
