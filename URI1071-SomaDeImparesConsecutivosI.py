a = int(input())
b = int(input())
if a <= b:
    x = a
    y = b
else:
    x = b
    y = a
soma = 0
for c in range(x + 1, y):
    if c % 2 == 1:
        soma += c
print(soma)