n = int(input())
s = [int(x) for x in input().split()]
e = 1
for c in range(2, n):
    if s[c] - s[c - 1] != s[c - 1] - s[c - 2]:
        e += 1
print(e)