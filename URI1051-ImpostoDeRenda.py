a = float(input())
if a > 4500:
    print(f'R$ {(((a - 4500) * 0.28) + (1500 * 0.18) + (1000 * 0.08)):.2f}')
elif 3000 < a <= 4500:
    print(f'R$ {(((a - 3000) * 0.18) + (1000 * 0.08)):.2f}')
elif 2000 < a <= 3000:
    print(f'R$ {((a - 2000) * 0.08):.2f}')
elif a <= 2000:
    print('Isento')