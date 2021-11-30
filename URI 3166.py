n, m, p = map(int, input().split())
palavras = []
for _ in range(n):
    palavras.append(input().lower())
matriz = []
dp = ''
pp = []
for i in range(m):
    matriz.append(input().lower())
    try:
        dp += matriz[i][i]
    except:
        pass
dpr = dp[::-1]
p2 = p - 1
pu = []
for i in range(p):
    f = ''
    for j in range(p2):
        i += 1
        try:
            f += matriz[j][i]
        except:
            pass
    fr = f[::-1]
    for palavra in palavras:
        if palavra in f or palavra in fr:
            pu.append(palavra)
    p2 -= 1
m2 = m - 1
pd = []
for i in range(m):
    f = ''
    for j in range(m2):
        i += 1
        try:
            f += matriz[i][j]
        except:
            pass
    fr = f[::-1]
    for palavra in palavras:
        if palavra in f or palavra in fr:
            pd.append(palavra)
    m2 -= 1
for palavra in palavras:
    if palavra in dp or palavra in dpr:
        print(f'1 Palavra "{palavra}" na diagonal principal')
    elif palavra in pu:
        print(f'2 Palavra "{palavra}" acima da diagonal principal')
    elif palavra in pd:
        print(f'3 Palavra "{palavra}" abaixo da diagonal principal')
    else:
        print(f'4 Palavra "{palavra}" inexistente')