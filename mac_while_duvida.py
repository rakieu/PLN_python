# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# ------
# este programa recebe um inteiro nao negativo n e  calcula o fatorial de n
#definição de fatorial de n, denotado por n!
#0! = 1
# n! = n * (n-1)! = n (n-1) * (n-2) * ... * 2 * 1,
# ------

print (" Digite uma sequência de numéros,para que seja somado, a soma termina quando você digita 0") 
soma = 0
valor = 1
while valor != 0:
    valor = int(input(" Digite um valor a ser somado: "))
    soma = soma + valor
    
print("A soma dos valores digitados são:", soma)

