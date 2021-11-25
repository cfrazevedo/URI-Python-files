n = int(input())
pi = ord(input()) - 65
abc = [0, 0, 0]
abc[pi] = 1
for _ in range(n):
    m = int(input())
    if m == 1:
        abc[0], abc[1] = abc[1], abc[0]
    elif m == 2:
        abc[2], abc[1] = abc[1], abc[2]
    elif m == 3:
        abc[0], abc[2] = abc[2], abc[0]
pf = chr(abc.index(1) + 65)
print(pf)