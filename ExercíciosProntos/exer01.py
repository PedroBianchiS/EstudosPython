def soma(x, y):
    return x + y

a = int(input('Insira o valor A: '))
b = int(input('Insira o valor B: '))
c = int(input('Insira o valor C: '))

result = soma(a, b)
print(result)

if result < c:
    print('A soma é menor do que', c)
else:
    print('A soma não é menor que', c)