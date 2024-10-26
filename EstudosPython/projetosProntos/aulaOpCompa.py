primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro = int(primeiro_valor)
segundo = int(segundo_valor)

if primeiro > segundo:
    print(
        f'{primeiro} é maior '
        f'do que {segundo}!')
elif segundo > primeiro:
    print(
        f'{segundo} é maior '
        f'do que {primeiro}')
else:
    print('Os Valores são iguais!')