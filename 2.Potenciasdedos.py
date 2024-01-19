import math
a = int(input("ingrese un numero\n:"))
print(f"potencias de dos del {a}")

for i in range(a+1):
    potencia = math.pow(i, 2)
    print(f"{i}^2 = {potencia}")