#clase cliente
class Cliente:
    def __init__(self, id_cliente, rut, nombre, apellido, correo, fecha_registro, saldo):
        self.id_cliente = id_cliente
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.__saldo = int(saldo)
    # obtengo en formato diccionario el objeto  
    def get(self):
        return self.__dict__
    
    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self, saldo):
        self.__saldo -= saldo

