ln1 = input().split()
ln2 = input().split()
x = 0
for c in range(0, int(ln1[1])):
    if c != 0:
        if abs(int(ln2[c]) - int(ln2[c - 1])) > int(ln1[0]):
            x = 1
            break
if x == 0:
    print('YOU WIN')
else:
    print('GAME OVER')