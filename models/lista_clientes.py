class Lista_clientes():

    clientes_ = []

    def get(self):
        return self.clientes_

    def add(self, data):
        self.clientes_.append(data)
    
    def remove(self, id_):
        self.clientes_.pop(id_)

    def buscar_cliente(self, id_):
        cliente = [cliente_buscado for cliente_buscado in self.clientes_ if cliente_buscado['id_cliente'] == id_][0]
        return cliente

    def comprar(self, precio_compra, id_):
        cliente = self.buscar_cliente(id_)
        if (cliente['_Cliente__saldo']) >= precio_compra:
            cliente['_Cliente__saldo'] -= precio_compra
            return cliente['_Cliente__saldo']
        else:
            return 'El cliente no tiene el saldo suficiente'
