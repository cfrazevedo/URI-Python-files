def add_walls(wlist, x, y):
    wlist.append([x, y])
    wlist.append([y, x])
    return wlist

t = int(input())
for _ in range(t):
    n = int(input())
    h_comb = [[0]]

    if n == 1:
        print(0)

    else:
        n_layers = n // 2
        n_cell = (sum(x + 1 for x in range(n_layers)) * 6) + 1
        number = 0

        for i in range(n_layers):
            layer = []
            for j in range(6*(i + 1)):
                number += 1
                layer.append(number)
            h_comb.append(layer)

    walls = []


    for nc, c in enumerate(h_comb):
        if nc == 0:
            for a in h_comb[1]:
                walls = add_walls(walls, 0, a)
        else:
            if n/2 > nc:
                for a in c:
                    walls = add_walls(walls, h_comb[nc][c.index(a) - 1], a)

                if nc < n_layers:
                    nro_add = 0
                    for a in c:
                        walls = add_walls(walls, h_comb[nc + 1][c.index(a) + nro_add - 1], a)
                        walls = add_walls(walls, h_comb[nc + 1][c.index(a) + nro_add], a)
                        if c.index(a) % nc == 0:
                            nro_add += 1
                            walls = add_walls(walls, h_comb[nc + 1][c.index(a) + nro_add], a)

    walls_index = []

    for i in range(n_cell):
        sub = []
        for wall in walls:
            if wall[0] == i:
                sub.append(wall)
        walls_index.append(sub)

    path = [[0,0]]

    for step in range(n):
        f_path = []
        for i in path:
            f_path.extend(walls_index[i[1]])
        if n - step <= n//2:
            f_path_copy = f_path.copy()
            for p_step in f_path_copy:
                if p_step[1] > h_comb[n - step - 1][-1]:
                    f_path.remove(p_step)
        path = f_path.copy()

    print(len(path))
