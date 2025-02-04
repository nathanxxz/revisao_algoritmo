carrinho = [
    {'nome': 'ps5', 'preco': 3500.00, 'qtd': 1},
    {'nome': 'psn', 'preco': 150.00, 'qtd': 2},
    {'nome': 'fifa21', 'preco': 200.00, 'qtd': 1}
]


def calcular_total(carrinho: list):
    total = 0
    for item in carrinho:
        total += item['preco'] * item['qtd']
    return total


total_compra = calcular_total(carrinho)
print(f'Total da compra: R$ {total_compra:.2f}')
print('Lista de itens no carrinho:')
for item in carrinho:
    print(f'- {item['nome']}, Quantidade: {item['quantidade']}, Preço unitário: R$ {item['preço']:.2f}')