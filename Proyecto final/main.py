import csv
import os
from class_trans import Transaccion
from zipfile import ZipFile

# RUTA CSV
ruta_csv = os.path.join(os.path.dirname(__file__), "finanzas.csv")

# FUNCION FORMATO
def formato(numero):
    return f"{round(numero):,}".replace(",", ".")

# LEER CSV

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

# FILTRO POR FECHA
año = input("Ingrese el año: ")
mes = input("Ingrese el mes (01-12): ")

# SI EL MES TIENE UN SOLO DIGITO
if len(mes) == 1:
    mes = "0" + mes

# ANALISIS BASICO
total_ingresos = 0
total_gastos = 0
gastos_por_categoria = {}

for t in transacciones:

    # SOLO DATOS DEL MES Y AÑO SELECCIONADO
    if t.fecha[:4] == año and t.fecha[5:7] == mes:

        if t.es_ingreso():
            total_ingresos += t.monto

        elif t.es_gasto():
            total_gastos += t.monto

            if t.categoria not in gastos_por_categoria:
                gastos_por_categoria[t.categoria] = 0

            gastos_por_categoria[t.categoria] += t.monto

# DIA CON MAS GASTO
gastos_por_dia = {}

for t in transacciones:

    # SOLO DATOS DEL MES Y AÑO SELECCIONADO
    if t.fecha[:4] == año and t.fecha[5:7] == mes:

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

# CATEGORIA CON MAS GASTO

categoria_mayor = ""
valor_categoria = 0

for categoria in gastos_por_categoria:
    if gastos_por_categoria[categoria] > valor_categoria:
        valor_categoria = gastos_por_categoria[categoria]
        categoria_mayor = categoria

# AHORRO

if total_ingresos < 1000:
    porcentaje_ahorro = 0.1

elif total_ingresos < 3000:
    porcentaje_ahorro = 0.15

else:
    porcentaje_ahorro = 0.2

meta_ahorro = total_ingresos * porcentaje_ahorro
ahorro_actual = total_ingresos - total_gastos

consejos = []

if ahorro_actual < meta_ahorro:
    consejos.append("Intenta ahorrar mas dinero")

else:
    consejos.append("Vas bien con tu ahorro")

# ALERTAS

alertas = []

if total_gastos > total_ingresos:
    alertas.append("Estas gastando mas de lo que ganas")

if valor_mayor > total_gastos * 0.3:
    alertas.append("Mucho gasto en un solo dia")

# REPORTE

with open("reporte.txt", "w", encoding="utf-8") as archivo:
    archivo.write("REPORTE FINANCIERO\n")
    archivo.write("-----------------\n")

    archivo.write("Ingresos: $" + formato(total_ingresos) + "\n")
    archivo.write("Gastos: $" + formato(total_gastos) + "\n")
    archivo.write("Balance: $" + formato(total_ingresos - total_gastos) + "\n\n")

    archivo.write("ALERTAS:\n")
    for a in alertas:
        archivo.write("- " + a + "\n")

    archivo.write("\nDia con mas gasto: " + dia_mayor + "\n")
    archivo.write("Categoria con mas gasto: " + categoria_mayor + "\n")

    archivo.write("\nMeta de ahorro: $" + formato(meta_ahorro) + "\n")
    archivo.write("Ahorro actual: $" + formato(ahorro_actual) + "\n")

    archivo.write("\nConsejos:\n")
    for c in consejos:
        archivo.write("- " + c + "\n")

with ZipFile("reporte.zip", "w") as zipf:
    zipf.write("reporte.txt")

print("Programa terminado correctamente")
