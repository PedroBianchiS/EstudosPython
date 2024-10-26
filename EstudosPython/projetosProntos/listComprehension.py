""" print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)

print(lista)

lista = [1 for numero in range(10)]
print(lista)

lista = [numero for numero in range(10)]
print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista) """

############################
import pprint

def printBonito(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, }
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

""" printBonito(novos_produtos) """
lista = [n for n in range(10) if n < 5]
print(lista)