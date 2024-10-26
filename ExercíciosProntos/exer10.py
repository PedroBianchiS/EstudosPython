nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceire nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4 ) / 4

print(f'Sua média final é: {media:.1f}')
if media < 7:
    print('REPROVADO')
if media >= 7:
    print('APROVADO!')