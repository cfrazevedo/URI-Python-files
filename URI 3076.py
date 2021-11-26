from math import ceil

while True:
    try:
        n = int(input())
        s = ceil(n / 100)
        print(s)
    except EOFError:
        break