def collatz_sequence(n):
    s = [n]
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        s.append(n)
    
    return s

n = int(input("Ingrese un número para generar la secuencia de Collatz: "))

r = collatz_sequence(n)
print("Secuencia de Collatz:", r)
