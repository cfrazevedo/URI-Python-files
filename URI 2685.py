while True:
    try:
        m = int(input())
        if 90 <= m < 180:
            print('Boa Tarde!!')
        elif 180 <= m < 270:
            print('Boa Noite!!')
        elif 270 <= m < 360:
            print('De Madrugada!!')
        else:
            print('Bom Dia!!')
    except EOFError:
        break