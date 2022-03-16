class Lista_productos():

    productos_ = []

    def get(self):
        return self.productos_

    def add(self, data):
        self.productos_.append(data)
    
    def remove(self, id_):
        self.productos_.pop(id_)
    
    def buscar_producto(self, sku):
        producto = [producto_buscado for producto_buscado in self.productos_ if producto_buscado['SKU'] == sku][0]
        return producto

    def stock_update(self, sku, cantidad):
        producto = self.buscar_producto(sku)
        if producto['stock'] >= cantidad:
            producto['stock'] -= cantidad
            return producto
        else:
            return 'No tenemos esa cantidad del producto'