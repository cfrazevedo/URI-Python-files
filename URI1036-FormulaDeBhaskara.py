linha = input().split()
A = float(linha[0])
B = float(linha[1])
C = float(linha[2])
D = (B ** 2) - (4 * A * C)
if D < 0 or A == 0:
    print('Impossivel calcular')
else:
    r1 = (-B + (D ** (1 / 2))) / (2 * A)
    r2 = (-B - (D ** (1 / 2))) / (2 * A)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')