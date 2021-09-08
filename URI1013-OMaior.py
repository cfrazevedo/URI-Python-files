linha1 = input().split()
a = int(linha1[0])
b = int(linha1[1])
c = int(linha1[2])
maiorAB = (a + b + abs(a - b)) / 2
maior = int((maiorAB + c + abs(maiorAB - c)) / 2)
print(f'{maior} eh o maior')