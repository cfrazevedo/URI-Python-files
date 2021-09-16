from math import log2

while True:
    try:
        n = log2(int(input()))
        print(int(n))
    except EOFError:
        break