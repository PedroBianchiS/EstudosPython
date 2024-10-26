a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))

valores = [a, b, c]

valores.sort(reverse=True)

print('Os valores em ordem descrescente são: ')
for valor in valores:
    print(valor)