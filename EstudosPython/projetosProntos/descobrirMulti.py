resp = input('Digite o número que deseja saber os múltiplos até 100: ')
numero = int(resp)
cont = range(0, 100, numero)

for numeros in cont:
    print(numeros)

print('boa!')