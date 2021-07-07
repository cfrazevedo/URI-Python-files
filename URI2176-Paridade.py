l = str(input())
x = 0
for c in l:
    if c == '1':
        x += 1
if x % 2 == 0:
    l += '0'
else:
    l += '1'
print(l)