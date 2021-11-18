e, d = [int(x) for x in input().split()]
if e > d:
    print('Eu odeio a professora!')
elif e < d - 2:
    print('Muito bem! Apresenta antes do Natal!')
else:
    print('Parece o trabalho do meu filho!')
    if e > 21:
        print('Fail! Entao eh nataaaaal!')
    else:
        print('TCC Apresentado!')