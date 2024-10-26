perguntas = [
    {
        'Pergunta:': 'Quanto é 2 + 2?',
        'Opções:': ['5', '3', '4'],
        'Resposta:': '4',
}, 
{
    'Pergunta:': 'Quem descobriu o Brasil?',
        'Opções:': ['Pedro Alvares Cabral', 'Tiradentes', 'Americo Vespúcio'],
        'Resposta:': 'Pedro Alvares Cabral',
}, 
{
    'Pergunta:': 'Quanto é 5 * 9?',
        'Opções:': ['50', '45', '40'],
        'Resposta:': '45',
}]

for pergunta in perguntas:
    print(pergunta['Pergunta:'])
    print()

    opcoes = pergunta['Opções:']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    
    print()

    escolha = input('Escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    qtd_opces = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opces:
            if opcoes[escolha_int] == pergunta['Resposta:']:
                acertou = True

    if acertou:
        print('Acertou!')
    else:
        print('Errou!')