for c in range(7):
    if c == 0 or c == 6:
        print('-' * 39)
    elif c == 1:
        print('|' + 'x = 35' + (' ' * 31) + '|')
    elif c == 3:
        print('|' + (' ' * 15) + 'x = 35' + (' ' * 16) + '|')
    elif c == 5:
        print('|' + (' ' * 31) + 'x = 35' + '|')
    else:
        print('|' + (' ' * 37) + '|')