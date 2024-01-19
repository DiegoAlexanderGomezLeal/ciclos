n1 = int(input("Ingrese el primer número entero:\n "))
n2 = int(input("Ingrese el segundo número entero:\n "))
if n1 > n2:
    n1, n2 = n2, n1

suma_entre_numeros = sum(range(n1 + 1, n2))

print(f"La suma de los números entre {n1} y {n2} es: {suma_entre_numeros}")