from itertools import combinations

entrada = open("input_11")
lines = entrada.read().splitlines()
entrada.close()

graf = []

for l in lines:
    aux = list(l)
    # doble fila si buida
    if('#' not in aux):
        graf.append(aux)
    graf.append(aux)

cols = []
for col_index in range(len(graf[0])):
    # Check if '#' is present in the column
    if '#' not in [row[col_index] for row in graf]:
        cols.append(col_index + len(cols))

for i in range(len(graf)):
    r = graf[i].copy()
    for col in cols:
        r.insert(col, '.')
    graf[i] = r


files = len(graf)
cols = len(graf[0])


idx = []

for i in range(files):
    for j in range(cols):
        if graf[i][j] == '#':
            idx.append((i,j))

pairs = list(combinations(idx, 2))

acc = 0
for p1, p2 in pairs:
    acc += abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

print("First problem: ", acc)

graf = []
rows = []

for i in range(len(lines)):
    aux = list(lines[i])
    # doble fila si buida
    if('#' not in aux):
        rows.append(i)
        graf.append(['1'] * len(aux))
    else:
        graf.append(aux)

cols = []
for col_index in range(len(graf[0])):
    # Check if '#' is present in the column
    if '#' not in [row[col_index] for row in graf]:
        cols.append(col_index)

for i in range(len(graf)):
    r = graf[i].copy()
    for col in cols:
        r[col] = '1'
    graf[i] = r

files = len(graf)
columnes = len(graf[0])

idx = []

for i in range(files):
    for j in range(columnes):
        if graf[i][j] == '#':
            idx.append((i,j))

pairs = list(combinations(idx, 2))

acc = 0
for p1, p2 in pairs:
    x2 = max(p1[0], p2[0])
    x1 = min(p1[0], p2[0])
    y2 = max(p1[1], p2[1])
    y1 = min(p1[1], p2[1])

    for i in range(x1, x2+1):
        if i in rows:
            acc += 1000000-1

    for i in range(y1, y2 + 1):
        if i in cols:
            acc += 1000000-1

    acc += abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

print("Second problem: ",acc)