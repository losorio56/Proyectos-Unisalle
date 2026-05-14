import csv
import os
from class_trans import Transaccion
from zipfile import ZipFile


# RUTA CSV
ruta_csv = os.path.join(os.path.dirname(_file_), "finanzas.csv")


# FUNCION FORMATO
def formato(numero):
    return f"{round(numero):,}".replace(",", ".")

# -----------------------------
# 4. LEER CSV
# -----------------------------
transacciones = []

with open(ruta_csv, newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        t = Transaccion(
            fila["Date"],
            fila["Category"],
            fila["Amount"],
            fila["Type"],
            fila["Transaction Description"],
        )
        transacciones.append(t)


# -----------------------------
# 5. ANALISIS BASICO
# -----------------------------
total_ingresos = 0
total_gastos = 0
gastos_por_categoria = {}

for t in transacciones:
    if t.es_ingreso():
        total_ingresos += t.monto

    elif t.es_gasto():
        total_gastos += t.monto

        if t.categoria not in gastos_por_categoria:
            gastos_por_categoria[t.categoria] = 0

        gastos_por_categoria[t.categoria] += t.monto


# -----------------------------
# 6. DIA CON MAS GASTO
# -----------------------------
gastos_por_dia = {}

for t in transacciones:
    if t.es_gasto():
        if t.fecha not in gastos_por_dia:
            gastos_por_dia[t.fecha] = 0

        gastos_por_dia[t.fecha] += t.monto

dia_mayor = ""
valor_mayor = 0

for dia in gastos_por_dia:
    if gastos_por_dia[dia] > valor_mayor:
        valor_mayor = gastos_por_dia[dia]
        dia_mayor = dia


# -----------------------------
# 7. CATEGORIA CON MAS GASTO
# -----------------------------
categoria_mayor = ""
valor_categoria = 0

for categoria in gastos_por_categoria:
    if gastos_por_categoria[categoria] > valor_categoria:
        valor_categoria = gastos_por_categoria[categoria]
        categoria_mayor = categoria


# -----------------------------
# 8. REPORTE
# -----------------------------
with open("reporte.txt", "w", encoding="utf-8") as archivo:
    archivo.write("REPORTE FINANCIERO\n")
    archivo.write("-----------------\n")

    archivo.write("Ingresos: $" + formato(total_ingresos) + "\n")
    archivo.write("Gastos: $" + formato(total_gastos) + "\n")
    archivo.write("Balance: $" + formato(total_ingresos - total_gastos) + "\n\n")


    archivo.write("\nDia con mas gasto: " + dia_mayor + "\n")
    archivo.write("Categoria con mas gasto: " + categoria_mayor + "\n")
