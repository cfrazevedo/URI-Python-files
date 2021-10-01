lista = []
while True:
    try:
        j = input()
        if j not in lista:
            lista.append(j)
    except EOFError:
        break
print(len(lista))

