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

def main ():
    n = int(input("Digit um número inteiro não-negativo: "))
    fat = 1
    k = 2
    while k <= n:
        fat = fat * k
        k = k + 1
        
    print ("\n O fatorial de", n, "é igual a", fat)
    print ()
    
# ------
main ()