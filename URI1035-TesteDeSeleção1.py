linha = input().split()
A = int(linha[0])
B = int(linha[1])
C = int(linha[2])
D = int(linha[3])
if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')