class Vendedor:
    def __init__(self, id_vendedor, rut, nombre, apellido, seccion, comision):
        self.id_vendedor = id_vendedor
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = comision

    def get(self):
        return self.__dict__