x = input().split()
p = int(x[0])
j1 = int(x[1])
j2 = int(x[2])
r = int(x[3])
a = int(x[4])
if r == 1 and a == 0 or r == 0 and a == 1:
    print('Jogador 1 ganha!')
elif r == 1 and a == 1:
    print('Jogador 2 ganha!')
elif r == 0 and a == 0:
    if (p + j1 + j2) % 2 == 0:
        print('Jogador 2 ganha!')
    else:
        print('Jogador 1 ganha!')