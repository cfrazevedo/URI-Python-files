n = int(input())
r = [int(x) for x in input().split()]
s = 0
for c in range(1, n):
    if r[c] < r[c - 1]:
        s = c + 1
        break
print(s)