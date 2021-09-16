linha1 = input().split()
n1 = float(linha1[0])
n2 = float(linha1[1])
n3 = float(linha1[2])
n4 = float(linha1[3])
mp = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10
print(f'Media: {mp:.1f}')
if mp >= 7:
    print('Aluno aprovado.')
elif mp < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    mr = (mp + exame) / 2
    if mr >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {mr:.1f}')