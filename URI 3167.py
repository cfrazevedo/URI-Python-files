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
        dp += matriz[i][m - i - 1]
    except:
        pass
dpr = dp[::-1]
p2 = p - 1
pu = []
for i in range(p - 1, -1, -1):
    f = ''
    for j in range(p2):
        i -= 1
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
    for j in range(m2, -1, -1):
        i += 1
        try:
            f += matriz[i][j]
        except:
            pass
    fr = f[::-1]
    for palavra in palavras:
        if palavra in f or palavra in fr:
            pd.append(palavra)
for palavra in palavras:
    if palavra in dp or palavra in dpr:
        print(f'1 Palavra "{palavra}" na diagonal secundaria')
    elif palavra in pu:
        print(f'2 Palavra "{palavra}" acima da diagonal secundaria')
    elif palavra in pd:
        print(f'3 Palavra "{palavra}" abaixo da diagonal secundaria')
    else:
        print(f'4 Palavra "{palavra}" inexistente')