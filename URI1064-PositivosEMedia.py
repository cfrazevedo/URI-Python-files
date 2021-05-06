a = [float(input()), float(input()), float(input()), float(input()), float(input()), float(input())]
p = []
cont = 0
for c in a:
    if c > 0:
        p.append(c)
        cont += 1
print(f'{cont} valores positivos')
print(f'{(sum(p) / len(p)):.1f}')