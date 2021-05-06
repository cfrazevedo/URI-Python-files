a = [float(input()), float(input()), float(input()), float(input()), float(input()), float(input())]
cont = 0
for c in a:
    if c > 0:
        cont += 1
print(f'{cont} valores positivos')