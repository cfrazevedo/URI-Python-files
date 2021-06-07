n = int(input())
s = []
jg = {'papel': 0, 'pedra': 1, 'ataque': 2}
for c in range(0, n):
    j1 = str(input())
    j2 = str(input())
    if j1 == j2:
        if j1 == 'papel':
            s.append('Ambos venceram')
        elif j1 == 'pedra':
            s.append('Sem ganhador')
        elif j1 == 'ataque':
            s.append('Aniquilacao mutua')
    elif jg[j1] > jg[j2]:
        s.append('Jogador 1 venceu')
    elif jg[j2] > jg[j1]:
        s.append('Jogador 2 venceu')
for c in s:
    print(c)