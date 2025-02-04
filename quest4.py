
produto={
    'Nome do produto':'Camisa do batman','QTD em Estoque':12,'Preco unitario':29.87
}
def exibir(produto:dict):
    print(produto)
def atualizarEstoque(produto:dict,qtd:int):
    produto['QTD em Estoque']+=qtd
    return produto
produto_atu=atualizarEstoque(produto,10)
exibir(produto_atu)
