a = input()
b = input()
c = input()
for cont in range(3):
    print(a + b + c)
    a, b, c = b, c, a
print(a[:10] + b[:10] + c[:10])