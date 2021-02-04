# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# ------
# este programa recebe dois inteiros a e n (n>=0) e calcula
#o valor de a elevado à potência n,
#definição:
#a^0 = 1 qualquer que seja o valor de a
# a^n = a * (a^(n-1)), se n > 0       1 * a * a * .... * a
def main ():
    a = int(input("Digite o valor da base (um inteiro a): "))
    n = int(input("Digite o valor do expoente ( um número inteiro não-negativo n): "))
    
    pot = 1
    cont = 0
    
    while cont < n:
        pot = pot * a
        cont = cont + 1
        print (pot, end= " ")
    print ("pot =", pot)

# ------

main ()

# pq nao começamos com pot = a e controlamos n-1 repetições?
# resposta: .......