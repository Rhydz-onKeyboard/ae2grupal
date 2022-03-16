import inquirer
from models.producto import Producto
from models.lista_productos import Lista_productos
from modules import menus
from helpers import uuid_generator

lista_productos = Lista_productos()

new_product = [
    inquirer.Text( name = 'name', message ='Cual es el nombre del producto?'),
    inquirer.Text( name = 'category', message ='A que categoria pertenece?'),
    inquirer.Text( name = 'stock', message ='Cual es el stock que tienes?'),
    inquirer.Text( name = 'value', message ='Cual es valor neto?'),
    inquirer.Text( name = 'made_in', message ='Donde fue hecho?'),
    inquirer.Text( name = 'rut', message ='Cual es el rut del proveedor?'),
    inquirer.Text( name = 'l_name', message ='Cual es el nombre legal?'),
    inquirer.Text( name = 'rrss', message ='Cual es la razon social?'),
]

def products_menu(selected_option):
    if selected_option == '1':
        print(lista_productos.get())
    elif selected_option == '2':
        producto = menus.add_item(new_product)
        producto = Producto(
                        uuid_generator.create(4), 
                        producto['name'], 
                        producto['category'],
                        producto['stock'],
                        producto['value'],
                        producto['made_in'],
                        uuid_generator.create(4), 
                        producto['rut'],
                        producto['l_name'],
                        producto['rrss']
                    )
        lista_productos.productos_.append(producto.get())
        print(f"Se agrego el producto: \n {producto.get()}")
    elif selected_option == '3':
        list_to_delete = [f"El producto: {_['nombre']} - SKU: {_['SKU']}" for _ in lista_productos.productos_]
        dato_eliminar = menus.to_delete('producto', list_to_delete)[-4:]
        for product in lista_productos.productos_:
            if product['SKU'] == dato_eliminar:
                confirm = menus.confirm_remove('producto')
                if confirm:
                    lista_productos.productos_.remove(product)
                else:
                    print('Regresaras al menu principal')