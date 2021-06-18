n, m = input().split()
n = int(n)
m = int(m)
x = y = 0
t = []
for i in range(0, n):
    tj = [int(e) for e in input().split()]
    t.append(tj[:])
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if t[i][j] == 42:
            if t[i - 1][j - 1] == t[i - 1][j] == t[i - 1][j + 1] == 7:
                if t[i][j - 1] == t[i][j + 1] == 7:
                    if t[i + 1][j - 1] == t[i + 1][j] == t[i + 1][j + 1] == 7:
                        x = i + 1
                        y = j + 1
                        break
print(x, y)