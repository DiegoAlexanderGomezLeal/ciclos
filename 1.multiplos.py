a = int(input("ingrese un numero\n:"))
print(f"tabla de multiplicar de {a}")

for i in range(1, 11):
    multiplicacion = a * i
    print(f"{a} x {i}={multiplicacion}")