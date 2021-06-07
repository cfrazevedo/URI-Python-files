mp = {'1001': 1.5, '1002': 2.5, '1003': 3.5, '1004': 4.5, '1005': 5.5}
p = int(input())
t = 0
for c in range(0, p):
    q = input().split()
    t += mp[str(q[0])] * int(q[1])
print(f'{t:.2f}')