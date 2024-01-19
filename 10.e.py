import math
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def aproximar_e():
    suma = 0
    n = 10  
    t_a= 0
    while abs(suma - t_a) >= 0.0001:
        t_ac = factorial(n)
        t_a = suma
        suma += t_ac / math.factorial(n)
        n += 1
    return suma
e_ap = aproximar_e()
print(f"Aproximación de e: {e_ap}")
