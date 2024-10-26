""" Faça um algoritmo que calcule a quantidade de litros de combustível gastos em uma viagem, sabendo que o carro faz 12km com um litro. Deve-se fornecer ao usuário o tempo que será gasto na 
viagem a sua velocidade média, distância percorrida e a quantidade de litros utilizados para fazer a viagem.

Fórmula: distância = tempo x velocidade.

        litros usados = distância / 12. """
def calcularConsumoCombustível():
    kilMetragem = 12 #Km por litro
    tempo = float(input('Digite o tempo gasto na viagem (horas): '))
    velocidade = float(input('Digite a velocidade média do carro (km/h): '))

    distancia = tempo * velocidade

    litrosGastos = distancia / kilMetragem

    print(f"\nResultado da viagem:")
    print(f"\nVelocidade média: {velocidade} km/h")
    print(f"Tempo de viagem: {tempo} horas")
    print(f"Distância percorrida: {distancia} km")
    print(f"Combustível utilizado: {litrosGastos:.2f} litros")

calcularConsumoCombustível()