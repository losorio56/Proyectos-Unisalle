class Transaccion:
    def __init__(self, fecha, categoria, monto, tipo, descripcion):
        self.fecha = fecha
        self.categoria = categoria
        self.monto = float(monto)
        self.tipo = tipo.lower()
        self.descripcion = descripcion

    def es_gasto(self):
        return self.tipo == "expense"

    def es_ingreso(self):
        return self.tipo == "income"

    def __str__(self):
        return (
            f"{self.fecha} | {self.categoria} | "
            f"{self.monto} | {self.tipo} | {self.descripcion}"
        )
