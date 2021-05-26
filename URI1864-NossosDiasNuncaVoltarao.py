ct = 'LIFE IS NOT A PROBLEM TO BE SOLVED'
n = int(input())
for c in range(0, n):
    if c == n - 1:
        print(ct[c])
    else:
        print(ct[c], end='')