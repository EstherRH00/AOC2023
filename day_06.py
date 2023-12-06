time = [ 55, 82, 64, 90]
distance = [246, 1441, 1012, 1111]
acumulador = 1

for t, d in zip(time, distance):
    # bin search i ale

    trobat = False
    i_sup = t
    i = t // 2
    i_inf = 0

    while not trobat:
        recorregut = i * (t - i)
        rec_ant = (i-1) * (t - (i -1))

        if recorregut > d and rec_ant <= d:
            trobat = True
        elif recorregut < d:
            i_ant = i
            i = (i + i_sup)//2
        else:
            i_sup = i
            i = (i+i_inf) // 2

    acumulador *= (t - 2*i + 1)

print("First problem:", acumulador)

time = [ 55826490]
distance = [246144110121111]
acumulador = 1

for t, d in zip(time, distance):
    # bin search i ale

    trobat = False
    i_sup = t
    i = t // 2
    i_inf = 0

    while not trobat:
        recorregut = i * (t - i)
        rec_ant = (i-1) * (t - (i -1))

        if recorregut > d and rec_ant <= d:
            trobat = True
        elif recorregut < d:
            i_ant = i
            i = (i + i_sup)//2
        else:
            i_sup = i
            i = (i+i_inf) // 2

    acumulador *= (t - 2*i + 1)

print("Second problem:", acumulador)