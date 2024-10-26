import re

entrada = input('CPF: ')
cpfRecebido = re.sub(r'[^0-9]', '', entrada)

cpf = cpfRecebido[:9]
contadorRegressivo = 10
resultado = 0

for numero in cpf:
    resultado += int(numero) * contadorRegressivo
    contadorRegressivo -= 1
print(f'soma dos valores é igual a: {resultado}')

digitoValidado = resultado * 10 % 11

digitoValidado = digitoValidado if digitoValidado <= 9 else 0

print('O primeiro dígito validado do CPF deve ser:', digitoValidado, '\n')

print('Validando o segundo dígito...\n')

cpf2 = cpf + str(digitoValidado)
contadorRegressivo = 11
resultado = 0

for numero in cpf2:
    resultado += int(numero) * contadorRegressivo
    contadorRegressivo -= 1
print(f'soma dos valores é igual a: {resultado}')

digitoValidado2 = resultado * 10 % 11

digitoValidado2 = digitoValidado2 if digitoValidado2 <= 9 else 0

print('O segundo dígito validado do CPF deve ser:', digitoValidado2, '\n')

cpfGerado = f'{cpf}{digitoValidado}{digitoValidado2}'

if cpfGerado == cpfRecebido:
    print(f'O CPF {cpfGerado} é válido!')
else:
    print(f'O CPF {cpfGerado} não é válido!')