linha1 = input().split()
c = int(linha1[0]) - 1
q = int(linha1[1])
p = [4, 4.5, 5, 2, 1.5]
print(f'Total: R$ {(q * p[c]):.2f}')