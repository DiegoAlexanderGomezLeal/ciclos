altura = int(input("Altura: "))
ancho = int(input("Ancho: "))
for i in range(altura):
    print('*' * ancho)



# altura = int(input("Altura: "))
# for i in range(1, altura + 1):
#     print('*' * i)



# lado = int(input("Lado: "))
# for i in range(-lado + 1, lado):
#     espacios = abs(i)
#     asteriscos = lado - espacios
#     print(' ' * espacios + '*' * (2 * asteriscos - 1))