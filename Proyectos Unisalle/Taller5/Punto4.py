# EJERCICIO 4: Suma de Valores Máximos y Mínimos
print("Suma de Valores Máximos y Mínimos")

cantidadNumeros = int(input("Ingrese la cantidad de números positivos: "))

numero = float(input("Ingrese el dato 1: "))
mayor = numero
menor = numero

for i in range(2, cantidadNumeros + 1):
    numero = float(input(f"Ingrese el dato {i}: "))
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
suma = mayor + menor

print("El valor máximo es:", int(mayor))
print("El valor mínimo es:", int(menor))
print("La suma del máximo y mínimo es:", int(suma))
