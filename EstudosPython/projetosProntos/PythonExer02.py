"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')
numero_int = int(numero)
if numero_int % 2 == 0:
    print('Este número é par!')
elif numero_int % 2 != 0:
    print('Este número é ímpar!')
else:
    print('Este não é um número válido!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Informe as horas: ')

try:
    hora_int = int(hora)
    if hora_int <= 11:
        print('Bom Dia!')
    elif hora_int <= 17:
        print('Boa Tarde!')
    elif hora_int <= 23:
        print('Boa Noite!')
    else:
        print('Não conheço esta hora!')
except:
    print('Por favor digite apenas números inteiros!')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Informe o seu Nome: ')
tamanho_nome = len(nome)
if tamanho_nome < 4:
    print('Seu nome é curto.')
elif tamanho_nome < 6:
    print('Seu nome é médio.')
else:
    print('Seu nome é grande!')