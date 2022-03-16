import inquirer
from models.cliente import Cliente
from models.lista_clientes import Lista_clientes
from modules import menus
from helpers import uuid_generator
from datetime import datetime

lista_clientes = Lista_clientes()

new_client = [
    inquirer.Text( name = 'rut', message ='Cual es el rut del cliente?'),
    inquirer.Text( name = 'name', message ='Cual es el nombre del cliente?'),
    inquirer.Text( name = 'last', message ='Cual es el apellido del cliente?'),
    inquirer.Text( name = 'email', message ='Escribe su email'),
    inquirer.Text( name = 'saldo', message ='Cual es su saldo?'),
]

def clients_menu(selected_option):
    if selected_option == '1':
        print(lista_clientes.get())
    elif selected_option == '2':
        cliente = menus.add_item(new_client)
        cliente = Cliente(
                        uuid_generator.create(4),
                        cliente['rut'], 
                        cliente['name'], 
                        cliente['last'], 
                        cliente['email'],
                        datetime.today().strftime('%d-%m-%Y'),
                        cliente['saldo']
                        )
        lista_clientes.add(cliente.get())
        print(f"Se agrego el cliente: \n {cliente.get()}")
    elif selected_option == '3':
        list_to_delete = [f"El cliente: {_['nombre']} {_['apellido']} - id: {_['id_cliente']}" for _ in lista_clientes.clientes_]
        dato_eliminar = menus.to_delete('cliente', list_to_delete)[-4:]
        for client in lista_clientes.clientes_:
            if client['id_cliente'] == dato_eliminar:
                confirm = menus.confirm_remove('cliente')
                if confirm:
                    lista_clientes.clientes_.remove(client)
                else:
                    print('Regresaras al menu principal')
