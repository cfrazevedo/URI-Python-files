linha = input().split()
a = int(linha[0])
b = int(linha[1])
if b <= a:
    b += 24
print(f'O JOGO DUROU {b - a} HORA(S)')