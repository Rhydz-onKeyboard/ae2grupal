import inquirer
from models.proveedor import Proveedor
from modules import menus
from helpers import uuid_generator

lista_proveedores = []

new_supplier = [
    inquirer.Text( name = 'rut', message ='Cual es el rut del proveedor?'),
    inquirer.Text( name = 'l_name', message ='Cual es el nombre legal?'),
    inquirer.Text( name = 'rrss', message ='Cual es la razon social?'),
]

def supplier_menu(selected_option):
    if selected_option == '1':
        print(lista_proveedores)
    elif selected_option == '2':
        proveedor = menus.add_item(new_supplier)
        proveedor = Proveedor(
                        uuid_generator.create(4), 
                        proveedor['rut'], 
                        proveedor['l_name'], 
                        proveedor['rrss'],
                        )
        lista_proveedores.append(proveedor.get())
        print(f"Se agrego el proveedor: \n {proveedor.get()}")
    elif selected_option == '3':
        list_to_delete = [f"El proveedor: {_['razon_social']} - id: {_['id_proveedor']}" for _ in lista_proveedores]
        dato_eliminar = menus.to_delete('proveedor', list_to_delete)[-4:]
        for supplier in lista_proveedores:
            if supplier['id_proveedor'] == dato_eliminar:
                confirm = menus.confirm_remove('proveedor')
                if confirm:
                    lista_proveedores.remove(supplier)
                else:
                    print('Regresaras al menu principal')