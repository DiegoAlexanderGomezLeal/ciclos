def estimar_pi(n):
    suma = 0
    signo = 1
    for i in range(1, 2 * n + 1, 2):
        termino = signo * (1 / i)
        suma += termino
        signo *= -1
    estimacion_pi = 4 * suma
    return estimacion_pi
n = int(input("Ingrese el número de términos (n): "))
r = estimar_pi(n)
print(r)