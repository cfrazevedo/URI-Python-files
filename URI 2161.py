def rq10(x):
    if x == 0:
        return 6
    else:
        x = 6 + (1 / rq10(x - 1))
        return x

n = int(input())
x = rq10(n) - 3
print(f'{x:.10f}')