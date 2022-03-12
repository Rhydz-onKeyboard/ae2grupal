from models.proveedor import Proveedor

class Producto:
    def __init__(self, SKU, nombre, categoria, stock, valor_neto, pais_origen, *args):
        self.SKU = SKU
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = 1.19
        self.pais_origen = pais_origen
        self.proveedor = Proveedor(*args)

    def get(self):
        return self.__dict__       