def coisaFavorita(coisa=''):
    if coisa == '':
        print('Você não gosta de nada? :(')
    elif coisa[-1] == 's':
        print('Sua coisa favorita são',coisa,'!!')
    else:
        print('Sua coisa favorita é', coisa, '!!')

coisaFavorita('comidas gostosas!')
coisaFavorita('Meu gato')

