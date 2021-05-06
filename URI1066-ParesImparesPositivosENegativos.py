a = [int(input()), int(input()), int(input()), int(input()), int(input())]
pcont = icont = scont = ncont = 0
for c in a:
    if c % 2 == 0:
        pcont += 1
    else:
        icont += 1
    if c > 0:
        scont += 1
    elif c < 0:
        ncont += 1
print(f'{pcont} valor(es) par(es)')
print(f'{icont} valor(es) impar(es)')
print(f'{scont} valor(es) positivo(s)')
print(f'{ncont} valor(es) negativo(s)')