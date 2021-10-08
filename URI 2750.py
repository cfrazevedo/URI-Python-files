for c in range(20):
    if c == 0 or c == 2 or c == 19:
        print('-' * 39)
    elif c == 1:
        print('| decimal   |  octal  |  Hexadecimal  |')
    else:
        x = c - 3
        if len(oct(x)[2:]) == 2:
            if len(str(x)) == 2:
                print('|' + (' ' * 5) + str(x) + (' ' * 4) + '|' +
                      (' ' * 3) + oct(x)[2:] + (' ' * 4) + '|' +
                      (' ' * 7) + hex(x)[2:].upper() + (' ' * 7) + '|')
            else:
                print('|' + (' ' * 6) + str(x) + (' ' * 4) + '|' +
                      (' ' * 3) + oct(x)[2:] + (' ' * 4) + '|' +
                      (' ' * 7) + hex(x)[2:].upper() + (' ' * 7) + '|')
        else:
            print('|' + (' ' * 6) + str(x) + (' ' * 4) + '|' +
                  (' ' * 4) + oct(x)[2:] + (' ' * 4) + '|' +
                  (' ' * 7) + hex(x)[2:].upper() + (' ' * 7) + '|')