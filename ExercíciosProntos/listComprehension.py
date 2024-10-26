listaPrecos = [100, 200, 5200, 1400, 350, 75]

#dobre o valor dos produtos com list comprehension

novaListaPrecos = []
for preco in listaPrecos:
    listaPrecos.append(preco * 2)
print(novaListaPrecos)