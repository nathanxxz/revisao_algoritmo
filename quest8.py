agenda_telefonica =[{'contato': {'nome': 'Zoro', 'telefone': '8888888', 'email': 'melhorespadachim@gmail.com'}},
                    {'contato': {'nome': 'Sanji', 'telefone': '7777777', 'email': 'allblue@gmail.com'}},
                    {'contato': {'nome': 'Luffy', 'telefone': '9999999', 'email': 'euvouseroreidospiratas@gmail.com'}}]


def buscar_contato(agenda_telefonica: list, nome: str):
    for contato in agenda_telefonica:
        if(contato['contato']['nome'].lower() == nome.lower()):
            return contato["contato"]
    return None

nome_desejado = input('Digite o nome do contato que deseja buscar: ')
contato_encontrado = buscar_contato(agenda_telefonica, nome_desejado)

if(contato_encontrado):
    print(f'Contato encontrado: {contato_encontrado}')
else:
    print('Contato não encontrado.')