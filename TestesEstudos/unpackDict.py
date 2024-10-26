pessoa = {
    'Nome:': 'Pedro',
    'Idade:': 24
}

a, b = pessoa
print(a, b)

c, d = pessoa.values()
print(c, d)

print(pessoa.items())

for valor in pessoa.items():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)

pessoaCompleta = {**pessoa}

print(pessoaCompleta)

def mostroArgumentosNomeados(*args, **kwargs):
        print('não nomeados: ', args)
        print(kwargs)

mostroArgumentosNomeados('Zeca', 'Luiz', nome='Pedro', idade=24)
mostroArgumentosNomeados(**pessoaCompleta)