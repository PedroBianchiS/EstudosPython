def checkNum(a):
    if a % 2 == 0:
        print('O número é par!')
    else:
        print('O número é ímpar!')
    if a > 0:
        print('O número é Positivo!')
    elif a == 0:
        print('O número não é positivo e nem negativo!')
    else:
        print('O número é negativo!')

num = int(input('Digite um número: '))

checkNum(num)