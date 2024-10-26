horaAula = int(input('Hora Aula: '))
numAulas = int(input('Aulas Lecionadas: '))
desconto = 0

salBruto = horaAula * numAulas

if salBruto <= 1450.00:
    desconto = 0.07
elif salBruto <= 2650.68:
    desconto = 0.09
elif salBruto <= 4000.00:
    desconto = 0.12
else:
    desconto = 0.14

desconto = (salBruto * desconto) / 100
salLiquido = salBruto - desconto

print(f'Seu salário líquido será de {salLiquido}')