a = int(input())
b = []
for c in range(0, a):
    b.append(int(input()))
dt = fr = 0
for c in b:
    if 10 <= c <= 20:
        dt += 1
    else:
        fr += 1
print(f'{dt} in')
print(f'{fr} out')