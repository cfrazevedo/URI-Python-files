def rq2(x):
    if x == 0:
        return 2
    else:
        x = 2 + (1 / rq2(x - 1))
        return x

n = int(input())
x = rq2(n) - 1
print(f'{x:.10f}')