livro = {
    'titulo': 'titulo : One piece, saga do East blue',
    'autor': 'Oda',
    "ano_publicacao": 1999,
    'numero_copias': 6
}


def emprestar_livro(livro: dict):
    if(livro['numero_copias'] > 0):
        livro['numero_copias'] -= 1
        print('Manga emprestado com sucesso. Cuide bem e devolva após terminar a leitura.')
        return True
    else:
        print('Infezlimente acabaou')
        return False


print(f'Quantidade de cópias disponíveis: {livro['numero_copias']}')
emprestar_livro(livro)