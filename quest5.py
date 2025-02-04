catalogo = [
    {'Título': 'The amazing Spider man', 'Ano de lançamento': 2014, 'Gênero': 'acao'},
    {'Título': 'The batman', 'Ano de lançamento': 2022, 'Gênero': 'drama'},
    {'Título': 'Joker', 'Ano de lançamento': 2019, 'Gênero': 'drama'},
    {'Título': 'Joker 2', 'Ano de lançamento': 2023, 'Gênero': 'drama'},
    {'Título': 'Matrix', 'Ano de lançamento': 1999, 'Gênero': 'Ficção Científica'},
    {'Título': 'Sonic 3', 'Ano de lançamento': 2024, 'Gênero': 'Ação'}
]

def filtrar_por_genero(catalogo: list, genero: str):
    filmes_filtrados = []
    for filme in catalogo:
        if(filme['Gênero'].lower() == genero.lower()):
            filmes_filtrados.append(filme)

    if(filmes_filtrados):
        print(f'Filmes do gênero {genero.capitalize()}:')
        for filme in filmes_filtrados:
            print(f'- {filme['Título']} ({filme['Ano de lançamento']})')
    else:
        print(f'Nenhum filme encontrado para o gênero {genero}')


genero_digitado = input('Digite o gênero de filme que deseja filtrar: ')
filtrar_por_genero(catalogo, genero_digitado)