n = int(input())
fn = []
a = 2
b = 3
c = 5
nn = 4
while len(fn) != n:
    if nn != c:
        fn.append(nn)
    else:
        a = b
        b = c
        c = a + b
    nn += 1
print(fn[-1])