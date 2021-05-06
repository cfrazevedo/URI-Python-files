for c in range (1,128):
    print(c, end=" ")
    if c % 4 == 1:
        print('w')
    elif c % 4 == 2:
        print('x')
    elif c % 4 == 3:
        print('y')
    elif c % 4 == 0:
        print('z')