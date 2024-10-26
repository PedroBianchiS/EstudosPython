lista = []

for i in range(1,16):
    lista.append(i)

print(lista)

print('intervalo de 1 a 9')

print(lista[:9])

print('intervalo de 8 a 13')

print(lista[7:13])

print('numeros pares e impares')

listaPares = []
listaImpares = []
for num in lista:
    if num % 2 == 0:
        listaPares.append(num)
    else:
        listaImpares.append(num)

print(listaPares)
print(listaImpares)

print('Multiplos de 2, 3 e 4')

print(lista[1::2])
print(lista[2::3])
print(lista[3::4])

print('lista reversa')

listaInvertida = []
lista.reverse()
for num in lista:
    listaInvertida.append(num)
print(listaInvertida)

print('Função enumerate')

lista = ['a','b','c','d','e']

for i, p in enumerate(lista):
    print(i + 1, '=>', p)

print('tirando Média com lista')

lisNotas = [5,6.5,7,9]
media = (lisNotas[0] + lisNotas[1] + lisNotas[2] + lisNotas[3]) / 4
print(f'{media:.1f}')