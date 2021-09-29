while True:
    try:
        m = float(input())
        ss = int((m * 240) + 21600)
        if ss >= 86400:
            ss -= 86400
        mm = ss // 60
        ss -= mm * 60
        hh = mm // 60
        mm -= hh * 60
        if 90 <= m < 180:
            print('Boa Tarde!!')
        elif 180 <= m < 270:
            print('Boa Noite!!')
        elif 270 <= m < 360:
            print('De Madrugada!!')
        else:
            print('Bom Dia!!')
        print(f'{hh:02}:{mm:02}:{ss:02}')
    except EOFError:
        break