n = int(input())
for _ in range(n):
    s = input()
    try:
        if len(s) == 8 and s[3] == '-' and s[0:2].isupper() and s[4:7].isnumeric():
            d = int(s[7])
            if d == 1 or d == 2:
                print('MONDAY')
            elif d == 3 or d == 4:
                print('TUESDAY')
            elif d == 5 or d == 6:
                print('WEDNESDAY')
            elif d == 7 or d == 8:
                print('THURSDAY')
            elif d == 9 or d == 0:
                print('FRIDAY')
        else:
            print('FAILURE')
    except:
        print('FAILURE')