from modules.producto import lista_productos
from modules.cliente import lista_clientes

class Vendedor:
    def __init__(self, id_vendedor, rut, nombre, apellido, seccion, comision):
        self.id_vendedor = id_vendedor
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = float(comision)

    def get(self):
        return self.__dict__
    
    @classmethod
    def venta(cls, producto, cantidad, cliente):
        precio = int(lista_productos.buscar_producto(producto)['valor_neto'])
        cliente = lista_clientes.comprar(precio, cliente)
        producto = lista_productos.stock_update(producto, cantidad)
        return producto, cliente, precio