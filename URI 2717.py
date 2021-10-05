n = int(input())
a, b = [int(x) for x in input().split()]
if a + b > n:
    print('Deixa para amanha!')
else:
    print('Farei hoje!')