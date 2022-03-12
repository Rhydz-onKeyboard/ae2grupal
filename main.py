from modules import menus, cliente, producto, vendedor, proveedor

main_questions = [
    {'value': 1, 'name':'Clientes'},
    {'value': 2, 'name':'Productos'},
    {'value': 3, 'name':'Vendedores'},
    {'value': 4, 'name':'Proveedores'},
    {'value': 5, 'name':'Salir'},
]
main_questions_list = [f"{_['value']}. {_['name']}" for _ in main_questions]

clients_questions = [
    {'value': 1, 'name':'Mostrar Clientes'},
    {'value': 2, 'name':'Agregar Cliente'},
    {'value': 3, 'name':'Eliminar Cliente'},
    {'value': 4, 'name':'Atras'},
]
clients_questions_list = [ f"{_['value']}. {_['name']}" for _ in clients_questions]

products_questions = [
    {'value': 1, 'name':'Mostrar Productos'},
    {'value': 2, 'name':'Agregar Producto'},
    {'value': 3, 'name':'Eliminar Producto'},
    {'value': 4, 'name':'Atras'},
]
products_questions_list = [ f"{_['value']}. {_['name']}" for _ in products_questions]

seller_questions = [
    {'value': 1, 'name':'Mostrar Vendedores'},
    {'value': 2, 'name':'Agregar Vendedor'},
    {'value': 3, 'name':'Eliminar Vendedor'},
    {'value': 4, 'name':'Atras'},
]
seller_questions_list = [ f"{_['value']}. {_['name']}" for _ in seller_questions]

supplier_questions = [
    {'value': 1, 'name':'Mostrar proveedores'},
    {'value': 2, 'name':'Agregar proveedor'},
    {'value': 3, 'name':'Eliminar proveedor'},
    {'value': 4, 'name':'Atras'},
]
supplier_questions_list = [ f"{_['value']}. {_['name']}" for _ in supplier_questions]

value_opt = lambda funcion : funcion.split('.')[0]

def run():
    #funcion principal
    opt = ''
    while opt != '5':
        opt = value_opt(menus.menu('Comercializadora', main_questions_list))
        if opt == '1':
            clients_opt = value_opt(menus.menu('Clientes', clients_questions_list))
            cliente.clients_menu(clients_opt)
        elif opt == '2':
            product_opt = value_opt(menus.menu('Productos', products_questions_list))
            producto.products_menu(product_opt)
        elif opt == '3':
            seller_opt = value_opt(menus.menu('Vendedores', seller_questions_list))
            vendedor.seller_menu(seller_opt)
        elif opt == '4':
            supplier_opt = value_opt(menus.menu('Proveedores', supplier_questions_list))
            proveedor.supplier_menu(supplier_opt)
        else:
            print('Nos vemos')

        if opt != '5':
            menus.pause()

if __name__ == '__main__':
    run()