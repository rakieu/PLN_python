# -*- coding: utf-8 -*-
  
"""
     Nome do aluno: Raquel de Paula Guets
     Número USP: 9823644
     Curso: Letras (Português e Inglês)
     Disciplina: MAC0110 Introdução à Computação
     Turma: 47
     Exercício-Programa: EP0

     DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
     TODAS AS PARTES ORIGINAIS DESTE EXERCÍCIO-PROGRAMA FORAM
     DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
     DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
     OU PLÁGIO.
     DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESTE
     PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
     ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA
     SERÃO TRATADOS SEGUNDO OS CRITÉRIOS DIVULGADOS NA PÁGINA DA
     DISCIPLINA.
  
     Programa baseado no material didático disponível da disciplina MAC0110.
"""

def main():
    
    x = int(input("Digite x (para imprimir os x primeiros termos da sequência de Tribonacci):  "))
  
#Definição das variáveis que compõem o cálculo da sequência:
    
    n0 = 0      
    n1 = 0   
    n2 = 1
    cont = 0
        
    while (cont <= x):   
        print("Número de Tribonacci T(%d) = %4d" %(cont, n0)) #Impressão dos termos desde o termo 0 até o termo x 
        n = n0 + n1 + n2   
        n2 = n1
        n1 = n0
        n0 = n
        cont = cont + 1

# ----

main ()