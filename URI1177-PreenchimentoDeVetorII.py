x = int(input())
y = -1
for c in range(0, 1000):
    if y == x - 1:
        y = 0
    else:
        y +=1
    print(f'N[{c}] = {y}')