# EJERCICIO 10: Cálculo de números primos hasta M
print("Cálculo de números primos hasta M")

m = int(input("Ingrese un número entero positivo: "))
cantidadprimos = 0
primos = []
suma = 0

for n in range(1, m+1):
    divisores = 0

    for i in range(1, n+1):
        modulo = n % i
        if modulo == 0:
            divisores += 1
    if divisores == 2:
        cantidadprimos += 1
        suma += n
        primos.append(n)
        print(f"Primo #{cantidadprimos}: {n}")

print(f"La suma de primos desde 1 hasta {m} es: {suma}")
print(f"La cantidad de primos desde 1 hasta {m} es: {cantidadprimos}")
