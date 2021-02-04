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
    print ("calcule o fatorial de", n) # isso foi feito antes de alterar n
    
    fat = 1
    while n > 0:
        fat = fat * n
        n = n - 1 # perdemos o valor de n (dado originalmente)
        
    print ("resposta = ", fat)
    print ()
    
# ------
main ()