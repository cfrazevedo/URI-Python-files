while True:
    try:
        papagaio = {'esquerda': 'ingles',
                    'direita': 'frances',
                    'nenhuma': 'portugues',
                    'as duas': 'caiu'}
        s = input()
        print(papagaio[s])
    except EOFError:
        break