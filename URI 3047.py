m = int(input())
f = []
f.append(int(input()))
f.append(int(input()))
f.append(m - (f[0] + f[1]))
print(max(f))