class Proveedor:
    def __init__(self, id_proveedor, rut, nombre_legal, razon_social, juridica = True, pais = 'Chile'):
        self.id_proveedor = id_proveedor
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.juridica = juridica
        self.pais = pais

    def get(self):
        return self.__dict__  