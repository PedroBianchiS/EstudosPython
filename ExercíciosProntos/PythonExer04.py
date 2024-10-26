import os

lista = []

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar [f]inalizar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Digite um tem para adicionar à lista: ')
        lista.append(valor)
    elif opcao == 'a':
        i = input('Digite o índice do item a ser apagado: ')

        try:
            indice = int(i)
            os.system('cls')
            del lista[indice]
        except IndexError:
            print('Não foi possível apagar este índice pois ele não existe')
        except ValueError:
            print('Por favor, digite um número inteiro')
        except Exception:
            print('Ocorreu um erro desconhecido')

    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Nada para listar!')

        for i, valor in enumerate(lista):
            print(i, valor)
    elif opcao == 'f':
        os.system('cls')

        for i, valor in enumerate(lista):
            print(i, valor)
        break
    else:
        print('Por favor, digite i, a ou l!!')