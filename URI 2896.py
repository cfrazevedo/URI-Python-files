t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    g = n // k
    r = n % k
    print(g + r)