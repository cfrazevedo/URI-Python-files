while True:
    try:
        d, l, p = input().split()
        if (d == 'pedra' and l == p == 'tesoura') or (d == 'papel' and l == p == 'pedra') or (d == 'tesoura' and l == p == 'papel'):
            print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
        elif (l == 'pedra' and d == p == 'tesoura') or (l == 'papel' and d == p == 'pedra') or (l == 'tesoura' and d == p == 'papel'):
            print("Iron Maiden's gonna get you, no matter how far!")
        elif (p == 'pedra' and d == l == 'tesoura') or (p == 'papel' and d == l == 'pedra') or (p == 'tesoura' and d == l == 'papel'):
            print("Urano perdeu algo muito precioso...")
        else:
            print("Putz vei, o Leo ta demorando muito pra jogar...")
    except EOFError:
        break