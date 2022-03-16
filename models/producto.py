from models.proveedor import Proveedor

class Producto:
    def __init__(self, SKU, nombre, categoria, stock, valor_neto, pais_origen, *args):
        self.SKU = SKU
        self.nombre = nombre
        self.categoria = categoria
        self.stock = int(stock)
        self.valor_neto = int(valor_neto)
        self.__impuesto = 1.19
        self.pais_origen = pais_origen
        self.proveedor = Proveedor(*args)

    def get(self):
        return {
            'SKU': self.SKU,
            'nombre': self.nombre,
            'categoria': self.categoria,
            'stock': self.stock,
            'valor_neto': self.valor_neto,
            'impuesto': self.__impuesto,
            'pais_origen': self.pais_origen,
            'proveedor': self.get_supplier(),
        }

    def get_supplier(self):
        return self.proveedor.get()

    def get_impuesto(self):
        return self.__impuesto