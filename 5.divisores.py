numero = int(input("Ingrese un número entero: "))
divisores = []
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)
print(f"Divisores de {numero}:")
for divisor in divisores:
    print(divisor, end=" ")