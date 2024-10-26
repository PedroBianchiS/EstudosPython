peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)
condicao = ''

if imc < 18.5:
    condicao = 'Abaixo do peso'
elif imc < 24.9:
    condicao = 'Peso ideal'
elif imc < 29.9:
    condicao = 'Levemente acima do peso'
elif imc < 34.9:
    condicao = 'Obesidade grau I '
elif imc < 39.9:
    condicao = 'Obesidade grau II (severa)'
elif imc >= 40:
    condicao = 'Obesidade grau III (mórbida)'

print('Sua condição é:', condicao)