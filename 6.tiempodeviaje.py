tiempo_total_minutos = 0
while True:
    tiempo_tramo = int(input("Ingrese el tiempo de viaje en minutos (ingrese 0 para finalizar): "))
    if tiempo_tramo == 0:
        break
    tiempo_total_minutos += tiempo_tramo
horas = tiempo_total_minutos // 60
minutos = tiempo_total_minutos % 60
print(f"El tiempo total de viaje es: {horas} horas y {minutos} minutos.")