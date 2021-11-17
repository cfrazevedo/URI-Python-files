c = int(input())
for _ in range(c):
    n, m = [int(x) for x in input().split()]
    print(len(str(n ** m)))