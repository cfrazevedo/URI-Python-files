t = int(input())
c = []
for d in range(0, t):
    r = input().split()
    rs = str(r[0])
    rr = str(r[1])
    if rs == rr:
        c.append('De novo!')
    elif rs == 'tesoura' and rr == 'papel' or rs == 'tesoura' and rr == 'lagarto' or rs == 'papel' and rr == 'pedra' or rs == 'papel' and rr == 'Spock' or rs == 'pedra' and rr == 'lagarto' or rs == 'pedra' and rr == 'tesoura' or rs == 'lagarto' and rr == 'Spock' or rs == 'lagarto' and rr == 'papel' or rs == 'Spock' and rr == 'tesoura' or rs == 'Spock' and rr == 'pedra':
        c.append('Bazinga!')
    else:
        c.append('Raj trapaceou!')
for d, e in enumerate(c):
    print(f'Caso #{d + 1}: {e}')