from modules.producto import lista_productos
from modules.cliente import lista_clientes

class Vendedor:
    def __init__(self, id_vendedor, rut, nombre, apellido, seccion):
        self.id_vendedor = id_vendedor
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = 0.05

    def get(self):
        return self.__dict__
    
    def get_comision(self):
        return self.__comision
    
    @classmethod
    def venta(cls, producto, cantidad, cliente, comision):
        precio = int(lista_productos.buscar_producto(producto)['valor_neto'])
        precio_total = precio * (1 + comision) * lista_productos.buscar_producto(producto)['impuesto']
        precio_total *= cantidad
        cliente_ = lista_clientes.buscar_cliente(cliente)
        saldo_cliente = lista_clientes.comprar(precio_total, cliente)
        producto = lista_productos.stock_update(producto, cantidad)
        return f"Se han descontado {cantidad} unidades del producto {producto['nombre']}, quedan {producto['stock']} unidades. \nEl cliente {cliente_['nombre']} {cliente_['apellido']}, ha realizado una compra por {precio_total}. Su saldo es {saldo_cliente}. "