linha = input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])
d = int(linha[3])
if b > d:
    d += 60
    c -= 1
if c < a or c == a and d == b:
        c += 24
print(f'O JOGO DUROU {c - a} HORA(S) E {d - b} MINUTO(S)')