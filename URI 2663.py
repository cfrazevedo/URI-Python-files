n = int(input())
k = int(input())
l = [int(input()) for _ in range(n)]
l.sort(reverse=True)
v = k
while v < n and l[v] == l[k - 1]:
    v += 1
print(v)