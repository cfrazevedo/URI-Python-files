g = [int(x) for x in input().split()]
heax = g[0] + g[1] + g[2] + g[-1]
ow = g[3] + g[4]

if ow > heax:
    print('Sauron has returned.')
else:
    print('Middle-earth is safe.')