lst = []
while len(lst) != 2:
    n = float(input())
    if n < 0 or n > 10:
        print('nota invalida')
    else:
        lst.append(n)
print(f'media = {(sum(lst) / 2):.2f}')