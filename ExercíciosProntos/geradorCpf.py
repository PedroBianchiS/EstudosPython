import random
import re

noveDigitos = ''

for i in range(9):
    noveDigitos += str(random.randint(0, 9))
print(noveDigitos)

cpfRecebido = re.sub(r'[^0-9]', '', noveDigitos)
contadorRegressivo = 10
resultado = 0

for numero in cpfRecebido:
    resultado += int(numero) * contadorRegressivo
    contadorRegressivo -= 1
print(f'soma dos valores é igual a: {resultado}')

digitoValidado = resultado * 10 % 11

digitoValidado = digitoValidado if digitoValidado <= 9 else 0

print('O primeiro dígito validado do CPF deve ser:', digitoValidado, '\n')

print('Validando o segundo dígito...\n')

cpf2 = cpfRecebido + str(digitoValidado)
contadorRegressivo = 11
resultado = 0

for numero in cpf2:
    resultado += int(numero) * contadorRegressivo
    contadorRegressivo -= 1
print(f'soma dos valores é igual a: {resultado}')

digitoValidado2 = resultado * 10 % 11

digitoValidado2 = digitoValidado2 if digitoValidado2 <= 9 else 0

print('O segundo dígito validado do CPF deve ser:', digitoValidado2, '\n')

cpfGerado = f'{cpfRecebido}{digitoValidado}{digitoValidado2}'
print('O CPF gerado foi: ', cpfGerado)