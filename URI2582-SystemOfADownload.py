lista = ["PROXYCITY", "P.Y.N.G.", "DNSUEY!", "SERVERS", "HOST!", "CRIPTONIZE", "OFFLINE DAY", "SALT", "ANSWER!", "RAR?", "WIFI ANTENNAS"]
mus = []
c = int(input())
for cont in range(c):
    x, y = [int(z) for z in input().split()]
    print(lista[x + y])