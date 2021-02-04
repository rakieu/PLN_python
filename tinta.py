m = int(input("Digite o tamanho em m²"))
if m % 54 == 0:
    latas = m/54
else:
    latas = int(m/54) + 1

valor = latas * 80
print (f'{latas} latas')
print (f'Total: R$ {valor: .2f}')
input ()