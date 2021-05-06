a = [int(input()), int(input()), int(input()), int(input()), int(input())]
cont = 0
for c in a:
    if c % 2 == 0:
        p.append(c)
        cont += 1
print(f'{cont} valores positivos')
print(f'{(sum(p) / len(p)):.1f}')