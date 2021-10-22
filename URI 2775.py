def mergeSort(lista):
    global tottempo
    if len(lista) > 1:
        meio = len(lista) // 2
        le = lista[:meio]
        ld = lista[meio:]
        mergeSort(le)
        mergeSort(ld)
        i = j = k = c = cont = 0
        for d in le:
            c += d[1]
            cont += 1
        while i < len(le) and j < len(ld):
            if le[i][0] < ld[j][0]:
                lista[k] = le[i]
                c -= le[i][1]
                cont -= 1
                i += 1
            else:
                lista[k] = ld[j]
                tottempo += c + (ld[j][1] * cont)
                j += 1
            k += 1
        while i < len(le):
            lista[k] = le[i]
            i += 1
            k += 1
        while j < len(ld):
            lista[k] = ld[j]
            j += 1
            k += 1
    return lista

while True:
    try:
        n = int(input())
        numero = [int(x) for x in input().split()]
        tempo = [int(x) for x in input().split()]
        nxt = [[numero[x], tempo[x]] for x in range(n)]
        global tottempo
        tottempo = 0
        numMS = mergeSort(nxt)
        print(tottempo)
    except EOFError:
        break