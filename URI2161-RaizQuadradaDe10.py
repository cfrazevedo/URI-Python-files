def raiz(x):
    if x == 0:
        return 6
    else:
        x = 6 + (1/raiz(x-1))
        return x

n = int(input())
x = raiz(n) - 3
print(f'{x:.10f}')