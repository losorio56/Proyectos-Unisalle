import csv
import os
from zipfile import ZipFile

# 1. RUTA DEL ARCHIVO

RUTA_CSV = os.path.join(os.path.dirname(_file_), "finanzas.csv")

# 2. CLASE

class Transaccion:
    def _init_(self, fecha, categoria, monto, tipo, descripcion):
        self.fecha = fecha
        self.categoria = categoria
        self.monto = float(monto)
        self.tipo = tipo.lower()
        self.descripcion = descripcion

    def es_gasto(self):
        return self.tipo == "expense"

    def es_ingreso(self):
        return self.tipo == "income"

    def _str_(self):
        return (
            f"{self.fecha} | {self.categoria} | "
            f"{self.monto} | {self.tipo} | {self.descripcion}"
        )
