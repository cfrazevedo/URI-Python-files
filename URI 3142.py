def numCol(letras):
    if len(letras) > 3 or len(letras) == 3 and (letras[0] > 'X' or (letras[0] == 'X' and (letras[1] > 'F' or (letras[1] == 'F' and letras[2] > 'D')))):
        return 'Essa coluna nao existe Tobias!'
    r = 0
    p = 26 ** (len(letras) - 1)
    for i in range(len(letras)):
        r += (ord(letras[i]) - 64) * p
        p //= 26
    return r

while True:
    try:
        s = input()
        n = numCol(s)
        print(n)
    except EOFError:
        break