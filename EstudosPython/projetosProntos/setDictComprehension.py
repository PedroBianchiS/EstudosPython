produto = {
    'nome': 'Caneta azul',
    'preco': 2.50,
    'categoria': 'Escritório',
}

""" print(produto.items()) """
for chave, valor in produto.items():
    print(chave, valor)

dc = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

print(dc)