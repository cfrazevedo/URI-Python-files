for linha in range(0, 12):
    for coluna in range(0, 12):
        if coluna < linha and coluna + linha < 11:
            print("X", end=' ')
        else:
            print(' ', end=' ')
    print()