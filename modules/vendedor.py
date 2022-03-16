import inquirer
from models.vendedor import Vendedor
from modules.producto import lista_productos
from modules.cliente import lista_clientes
from helpers import uuid_generator
from modules import menus

lista_vendedores = []

new_seller = [
    inquirer.Text( name = 'rut', message ='Cual es el rut del vendedor?'),
    inquirer.Text( name = 'name', message ='Cual es el nombre?'),
    inquirer.Text( name = 'last', message ='Cual es el apellido?'),
    inquirer.Text( name = 'section', message ='A que seccion pertenece?'),
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
                        )
        lista_vendedores.append(vendedor.get())
        print(f"Se agrego el vendedor: \n {vendedor.get()}")
    elif selected_option == '3':
        try:
            list_to_delete = [f"El vendedor: {_['nombre']} {_['apellido']} - id: {_['id_vendedor']}" for _ in lista_vendedores]
            dato_eliminar = menus.to_delete('vendedor', list_to_delete)[-4:]
            for seller in lista_vendedores:
                if seller['id_vendedor'] == dato_eliminar:
                    confirm = menus.confirm_remove('vendedor')
                    if confirm:
                        lista_vendedores.remove(seller)
                    else:
                        print('Regresaras al menu principal')
        except TypeError:
            print('Volveras al menu principal')
    elif selected_option == '4':
        product_to_update = [f"El producto: {_['nombre']} - sku: {_['SKU']}" for _ in lista_productos.get()]
        producto = menus.menu('productos', product_to_update)[-4:]
        cantidad = int(input('Indique la cantidad a vender, solo numeros enteros: '))
        client_to_update = [f"El cliente: {_['nombre']} - id: {_['id_cliente']}" for _ in lista_clientes.get()]
        cliente = menus.menu('clientes', client_to_update)[-4:]
        print(Vendedor.venta(producto, cantidad, cliente, lista_vendedores[0]['_Vendedor__comision']))