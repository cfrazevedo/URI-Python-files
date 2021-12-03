n = int(input())
for _ in range(n):
    k, *o = map(int, input().split())
    t = 1
    for c in o:
        t += c - 1
    print(t)