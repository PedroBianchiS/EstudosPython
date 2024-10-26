print('Digite a temperatura média em Celsius de: ')
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperatura = []

for mes in meses:
    temp = float(input(f'Digite a temperatura média de {mes}: '))
    temperatura.append(temp)

print('\nTemperaturas média do ano: ')
for i in range(12):
    print(f'{meses[i]}: {temperatura[i]}ºC')

soma = sum(temperatura)
mediaAno = soma / 12
print()
print(f'Média de Temperatura do ano: {mediaAno:.1f}')