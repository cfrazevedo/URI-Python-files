lst = []
while True:
    n = int(input())
    if n < 0:
        break
    lst.append(n)
print(f'{(sum(lst) / len(lst)):.2f}')