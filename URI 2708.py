ent = input()
jo = to = 0
while ent != 'ABEND':
    j, t = ent.split()
    if j == 'SALIDA':
        jo += 1
        to += int(t)
    elif j == 'VUELTA':
        jo -= 1
        to -= int(t)
    ent = input()
print(to, jo, sep='\n')
