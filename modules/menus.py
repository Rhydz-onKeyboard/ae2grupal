import inquirer

def pause():
    key_input = [inquirer.Text( name = 'pausa', message= 'Presione ENTER para continuar')]
    return inquirer.prompt(key_input)

def menu(titulo, questions_list):
    print('=================================')
    print(f'           {titulo}')
    print('=================================')

    questions = [
        inquirer.List(titulo,
            message='Que desea hacer?',
            choices= questions_list,
            carousel=True
        ),
    ]

    result = inquirer.prompt(questions)
    return result[titulo]

def add_item(input_list = []):
    return inquirer.prompt(input_list)

def to_delete( to, list_ = []):
    to_delete = [inquirer.List(to, 
        message = f'Seleccione el {to} a eliminar', 
        choices = list_)
    ]
    item = inquirer.prompt(to_delete)
    return item[to]

def confirm_remove(text):
    question = [
        inquirer.Confirm('confirmar',
            message = f'Se eliminara el {text}, quieres continuar?'
        )
    ]
    confirmacion = inquirer.prompt(question)
    return confirmacion['confirmar']