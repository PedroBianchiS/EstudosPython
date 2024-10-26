valor1 = input("Digite o primeiro valor booleano (True ou False): ")
valor2 = input("Digite o segundo valor booleano (True ou False): ")

valor1 = valor1.strip().lower() == 'true'
valor2 = valor2.strip().lower() == 'true'

if valor1 and valor2:
    print("Ambos são VERDADEIRO.")
elif not valor1 and not valor2:
    print("Ambos são FALSO.")
else:
    print("Os valores são diferentes.")