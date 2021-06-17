import math

n = int(input())
p = n / math.log(n)
m = 1.25506 * p
print(f'{p:.1f} {m:.1f}')