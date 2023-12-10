entrada = open("input_10")
lines = entrada.read().splitlines()
entrada.close()

graf = []

i = -1
j = -1

for l in lines:
    aux = "."+l+"."
    graf.append(list(aux))
    if(j == -1):
        i += 1
        j = l.find('S')

graf.append(["."]*len(graf[0]))
graf.insert(0,["."]*len(graf[0]))

original_graf = graf

start = [i+1,j+1]

# DFS
depth = -1

q = list()
q.append([-1, start[0], start[1]])
visited = set()
while q != []:
    d, i, j = q.pop(0)
    depth = max(depth, d)
    val = graf[i][j]
    if (i,j) not in visited:
        visited.add((i, j))
        # estic connectat amb el de dalt
        if (val == 'S' or val == '|' or val == 'L' or val=='J') and (graf[i-1][j] == '|' or graf[i-1][j] == '7' or graf[i-1][j] == 'F'):
            q.append([d+1, i-1, j])
        if (val == 'S' or val == '|' or val == '7' or val=='F') and (graf[i+1][j] == '|' or graf[i+1][j] == 'L' or graf[i+1][j] == 'J'):
            q.append([d+1, i+1, j])
        if (val == 'S' or val == '-' or val == 'J' or val=='7') and (graf[i][j-1] == '-' or graf[i][j-1] == 'L' or graf[i][j-1] == 'F'):
            q.append([d+1, i, j-1])
        if (val == 'S' or val == '-' or val == 'F' or val=='L') and  (graf[i][j+1] == '-' or graf[i][j+1] == 'J' or graf[i][j+1] == '7'):
            q.append([d+1, i, j+1])


print("First problem: ", depth)

acc = 0

files = len(graf)
columnes = len(graf[0])

# omplir de 0 lo de fora

for i in range(1,files-1):
    for j in range(1,columnes-1):
        if((i,j) not in visited and graf[i][j] != '.'):
            graf[i][j] = '.'

# DFS
depth = 0

q = list()
q.append([0,0])
while q != []:
    i, j = q.pop(0)
    val = graf[i][j]
    if val != '0':
        graf[i][j] = '0'
        # estic connectat amb el de dalt
        if (max(0,i-1),j) not in visited and graf[max(0,i-1)][j] != '0':
            q.append([max(0,i-1), j])
        if ((i+1)%files,j) not in visited and graf[(i+1)%files][j] != '0':
            q.append([(i+1)%files, j])
        if (i,max(0, j-1) ) not in visited and graf[i][max(0, j-1)] != '0' :
            q.append([i, max(0, j-1)])
        if (i,(j+1)%columnes  ) not in visited and graf[i][(j+1)%columnes ] != '0':
            q.append([i,(j+1)%columnes ])
        if (max(0,i-1),max(0,j-1)) not in visited and graf[max(0, i-1)][max(0, j-1)] != '0':
            q.append([max(0,i - 1), max(0, j-1)])
        if ((i+1)%files,(j+1)%columnes ) not in visited and graf[(i+1)%files][(j+1)%columnes ] != '0':
            q.append([(i+1)%files,(j+1)%columnes ])
        if ((i+1)%files,max(0,j-1) ) not in visited and graf[(i+1)%files][max(0,j-1)] != '0':
            q.append([(i+1)%files, max(0,j-1)])
        if (max(0,i-1),(j+1)%columnes  ) not in visited and graf[max(0,i-1)][(j+1)%columnes ] != '0':
            q.append([max(0,i-1), (j+1)%columnes ])

for a in range(1,files-1):
    for b in range(1,columnes-1):

        # vaig fins a l'exterior i segons quantes x em trobi soc dins o no
        cont = 0
        total = 0
        if(graf[a][b] != '0' and graf[a][b] != '1' and (a,b) not in visited):

            ultim = ''
            sortida = False

            #cap a dalt
            for k in range(a-1, -1, -1):
                if graf[k][b] == 'S':
                    sortida = True
                if graf[k][b] == '-':
                    cont += 1
                elif graf[k][b] == 'L' or graf[k][b] == 'J':
                    ultim = graf[k][b]
                elif graf[k][b] == '7' and ultim=='L':
                    cont += 1
                elif graf[k][b] == 'F' and ultim=='J':
                    cont += 1

            if sortida:
                #cap a baix
                cont = 0
                for k in range(a + 1, files,+1):
                    if graf[k][b] == '-':
                        cont += 1
                    elif graf[k][b] == '7' or graf[k][b] == 'F':
                        ultim = graf[k][b]
                    elif graf[k][b] == 'L' and ultim == '7':
                        cont += 1
                    elif graf[k][b] == 'J' and ultim == 'F':
                        cont += 1
            # topologia
            if ( cont % 2 == 1):
                q = list()
                q.append([a, b])
                while q != []:
                    i, j = q.pop(0)
                    val = graf[i][j]
                    if val != '1' and (i,j) not in visited:
                        total += 1
                        graf[i][j] = '1'
                        # estic connectat amb el de dalt
                        if graf[i - 1][j] != '0' and graf[i - 1][j] !='1' and graf[i - 1][j] !='X':
                            q.append([i - 1, j])
                        if graf[i + 1][j] != '0' and graf[i + 1][j] != '1' and graf[i + 1][j] not in visited:
                            q.append([i + 1, j])
                        if graf[i][j - 1] != '0' and graf[i][j - 1] != '1' and graf[i][j - 1] !='X':
                            q.append([i, j - 1])
                        if graf[i][j + 1] != '0' and graf[i][j + 1] != '1' and graf[i][j + 1] not in visited:
                            q.append([i, j + 1])
                        
                        if graf[i - 1][j-1] != '0' and graf[i - 1][j-1] != '1' and graf[i - 1][j-1] not in visited:
                            q.append([i - 1, j-1])
                        if graf[i + 1][j+1] != '0' and graf[i + 1][j+1] != '1' and graf[i + 1][j+1] not in visited:
                            q.append([i + 1, j+1])
                        if graf[i+1][j - 1] != '0' and graf[i+1][j - 1] != '1' and graf[i+1][j - 1] not in visited:
                            q.append([i+1, j - 1])
                        if graf[i-1][j + 1] != '0' and graf[i-1][j + 1] != '1' and graf[i-1][j + 1] not in visited:
                            q.append([i-1, j + 1])


        acc += total


print("Second problem: ",acc)