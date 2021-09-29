a = [int(input()) for _ in range(3)]
l = [(a[1] + (a[2] * 2)) * 2, (a[0] + a[2]) * 2, (a[1] + (a[0] * 2)) * 2]
print(sorted(l)[0])