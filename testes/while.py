def main ():
    soma = 0
    n = 0
    while True:
        x = int(input('n (zero sai): '))
        if x == 0:
            break
        else:
            n = n + 1
            soma = soma + x
    print ("Soma é igual a", soma)
    print ("A média é igual a", soma / n)

# ----

main ()