def imprimir_tabla_multiplicar(filas, columnas):
    for i in range(1, filas + 1):
        for j in range(1, columnas + 1):
            resultado = i * j
            print(str(resultado).rjust(4), end="")
        print()
filas_usuario = int(input("Ingrese el número de filas: "))
columnas_usuario = int(input("Ingrese el número de columnas: "))
imprimir_tabla_multiplicar(filas_usuario, columnas_usuario)