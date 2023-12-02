entrada = open("input_02")
lines = entrada.readlines()
entrada.close()

acumulador = 0

for l in lines:
    game_id, games = l.split(':')
    # 12 R, 13G, 14B
    info = games.split()
    i = 0
    trobat = False
    while (i < len(info) and not trobat):
        val = (int) (info[i])
        color = info[i+1][0]

        if(val > 12 and color == 'r') or (val > 13 and color == 'g') or (val > 14 and color == 'b'):
            trobat = True

        i += 2
    if not trobat:
        acumulador += (int) (game_id.split()[1])

print("First problem: ", acumulador)

acumulador = 0

for l in lines:
    game_id, games = l.split(':')
    # 12 R, 13G, 14B
    info = games.split()
    i = 0
    maxR = 0
    maxB = 0
    maxG = 0
    while (i < len(info)):
        val = (int) (info[i])
        color = info[i+1][0]

        if(val > maxR and color == 'r'):
            maxR = val
        elif (val > maxB and color == 'b'):
            maxB = val
        elif(val > maxG and color == 'g'):
            maxG = val

        i += 2

    acumulador += (maxG * maxB * maxR)

print("Second problem: ", acumulador)