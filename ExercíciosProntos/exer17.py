def convertCelsius(temp):
    c = (5 * (temp - 32) / 9)
    return c

temp = int(input('Digite a temperatura em Fahrenheit: '))

print(f'A temperatura em Fahrenheit é {temp}')
print(f'A temperatura convertida para Celsius é {convertCelsius(temp):.2f}')