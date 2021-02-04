a = int(input("num"))
b = int(input("num"))

while b!=0:
    resto = a % b
    a = b
    b = resto
print("mdc(a,b) = ", a)
