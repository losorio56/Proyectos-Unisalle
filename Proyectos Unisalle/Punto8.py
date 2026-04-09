# EJERCICIO 8: Análisis de Temperaturas
print("Análisis de Temperaturas diarias en un mes (30 días)")

temperaturas = []
cantidadDias = 30
suma = 0

for i in range(1, cantidadDias + 1):
    temp = float(input(f"Ingrese la temperatura del día {i}: "))
    temperaturas.append(temp)
    suma += temp

promedio = suma/cantidadDias

mayor = temperaturas[0]
menor = temperaturas[0]
encimadelpromedio = 0
debajodelpromedio = 0

for temp in temperaturas:
    if temp > promedio:
        encimadelpromedio += 1
    if temp < promedio:
        debajodelpromedio += 1
    if temp > mayor:
        mayor = temp
    if temp < menor:
        menor = temp

print("Temperatura promedio del mes:", promedio)
print("Cantidad de días por encima del promedio:", encimadelpromedio)
print("Cantidad de días por debajo del promedio:", debajodelpromedio)
print("Temperatura máxima registrada:", mayor)
print("Temperatura mínima registrada:", menor)
