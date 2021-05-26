c = int(input())
s = []
for d in range(0, c):
    n = input().split()
    if n[0] == 'Thor':
        s.append('Y')
    else:
        s.append('N')
for d in s:
    print(d)