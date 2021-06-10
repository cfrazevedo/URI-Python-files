caso = 0
while True:
    try:
        n1 = input()
        n2 = input()
        qt = n2.count(n1)
        caso += 1
        print(f'Caso #{caso}:')
        if qt == 0:
            print('Nao existe subsequencia')
        else:
            print(f'Qtd.Subsequencias: {qt}')
            p = n2.rfind(n1) + 1
            print(f'Pos: {p}')
        print()
    except EOFError:
        break