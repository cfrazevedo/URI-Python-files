lst = []
tsl = []
for c in range(0, 20):
    x = int(input())
    lst.append(x)
for c in range(1, 21):
    tsl.append(lst[-c])
for c, d in enumerate(tsl):
    print(f'N[{c}] = {d}')