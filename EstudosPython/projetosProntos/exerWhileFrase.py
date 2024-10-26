frase = 'O Python é uma linguagem de programação multiparadigma, e o Python foi criado por Guido Van Russom.'

i = 0
qtd_apareceu = 0
letra_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letras = frase.count(letra_atual)

    if qtd_apareceu < qtd_letras:
        qtd_apareceu = qtd_letras
        letra_mais_vezes = letra_atual

    #print(letra_atual, ' ', qtd_letras)
    i += 1

print(f'A letra que apareceu mais vezes foi o "{letra_mais_vezes}" que apareceu {qtd_apareceu}x')