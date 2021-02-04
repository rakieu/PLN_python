def main ():
    print ("Fornecer, um a um, vários números inteiros e terminar a coleção fornecendo o zero")
    soma = 0
    num = int(input("Forneça um número inteiro: "))

    while num != 0:
        soma = soma + num
        num = int(input("Digite um número inteiro: "))
        print (soma)

    print("Soma dos números inteiros dados = ", soma)

# ----
main ()
