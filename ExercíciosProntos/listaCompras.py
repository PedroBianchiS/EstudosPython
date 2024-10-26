import os

listaCompras = []

novoItem = input('Digite o item que deseja adicionar a sua lista: ')

while True:
    listaCompras.append(novoItem)
    print(listaCompras)
    novoItem = input('Digite outro item ou aperte Enter para finalizar: ')
    
    if novoItem == '':
        os.system('cls')
        print('Lista finalizada: ', listaCompras)
        break
    else:
        continue 