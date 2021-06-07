n = int(input())
n = str(n)
ni = ''
for c in range(0, len(n)):
    ni += n[len(n) -1 - c]
print(ni)