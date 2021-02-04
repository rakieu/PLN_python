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
    n = int(input("Digite um numero inteiro positivo (n): "))
    soma = 1
    k = 1
    while soma <= n:
        k = k + 1
        soma = soma + k
        #print ("a soma de 1 até", k, "é ", soma)
        
    print ("o menor inteiro k tal que a +..... + k > ", n, "é", k)
    

# ------
main ()