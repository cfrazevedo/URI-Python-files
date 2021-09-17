linha = input().split()
a = int(linha[0])
b = int(linha[1])
if b % a == 0 or a % b == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')