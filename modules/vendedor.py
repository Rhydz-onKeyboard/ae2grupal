import inquirer
from models.vendedor import Vendedor
from helpers import uuid_generator, instancia
from modules import menus

lista_vendedores = []

new_seller = [
    inquirer.Text( name = 'rut', message ='Cual es el rut del vendedor?'),
    inquirer.Text( name = 'name', message ='Cual es el nombre?'),
    inquirer.Text( name = 'last', message ='Cual es el apellido?'),
    inquirer.Text( name = 'section', message ='A que seccion pertenece?'),
    inquirer.Text( name = 'commission', message ='Cual es la comision de venta?'),
]

def seller_menu(selected_option):
    if selected_option == '1':
        print(lista_vendedores)
    elif selected_option == '2':
        vendedor = menus.add_item(new_seller)
        vendedor = Vendedor(
                        uuid_generator.create(4), 
                        vendedor['rut'], 
                        vendedor['name'], 
                        vendedor['last'],
                        vendedor['section'],
                        vendedor['commission'],
                        )
        lista_vendedores.append(vendedor.get())
        print(f"Se agrego el producto: \n {vendedor.get()}")
    elif selected_option == '3':
        list_to_delete = [f"El vendedor: {_['nombre']} {_['apellido']} - id: {_['id_vendedor']}" for _ in lista_vendedores]
        dato_eliminar = menus.to_delete('vendedor', list_to_delete)[-4:]
        for seller in lista_vendedores:
            if seller['id_vendedor'] == dato_eliminar:
                confirm = menus.confirm_remove('vendedor')
                if confirm:
                    lista_vendedores.remove(seller)
                else:
                    print('Regresaras al menu principal')