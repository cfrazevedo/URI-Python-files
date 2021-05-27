n = input().split()
s = []
for c in n:
    s.append(int(c))
ns = sorted(s, reverse=True)
if ns[0] < ns[1] + ns[2] or ns[1] < ns[2] + ns[3]:
    print('S')
else:
    print('N')