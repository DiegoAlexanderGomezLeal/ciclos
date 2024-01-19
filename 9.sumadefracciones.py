def suma_fracciones():
    p = 1
    f = 0.5
    s= 0
    print("Potencia\tFraccion\tSuma")
    while f > 0.000001:
        print(f"{p}\t\t{f}\t\t{s}")
        s += f
        p+= 1
        f/= 2
suma_fracciones()