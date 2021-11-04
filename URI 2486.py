l = {'suco de laranja': 120, 'morango fresco': 85, 'mamao': 85, 'goiaba vermelha': 70, 'manga': 56, 'laranja': 50, 'brocolis': 34}
while True:
    t = int(input())
    if t == 0:
        break
    x = 0
    for c in range(0, t):
        a = input().split()
        aq = int(a[0])
        at = l[str(' '.join(a[1:]))]
        q = aq * at
        x += q
    if 110 <= x <= 130:
        print(f'{x} mg')
    elif x < 110:
        x = 110 - x
        print(f'Mais {x} mg')
    elif x > 130:
        x -= 130
        print(f'Menos {x} mg')