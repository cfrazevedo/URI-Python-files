x = []
n = int(input())
xp = input().split()
for c in range(0, n):
    x.append(int(xp[c]))
print(f'Menor valor: {min(x)}')
print(f'Posicao: {x.index(min(x))}')