from math import lcm

entrada = open("input_08")
lines = entrada.readlines()
entrada.close()

right_left = lines[0][:-1]

text_map = lines[2:]
mapa = dict()

for l in text_map:
    a,b,c,d = l.split()
    mapa[a]=(c[1:-1], d[:-1])

current = 'AAA'
cont = 0

while(current != 'ZZZ'):
    instr = right_left[cont%len(right_left)]

    if(instr == 'R'):
        current = mapa[current][1]
    else:
        current = mapa[current][0]

    cont += 1

print("First problem: ", cont)

res = []

for c in mapa.keys():
    if(c[2]=='A'):

        current = c
        cont = 0

        while(current[2] != 'Z'):
            instr = right_left[cont%len(right_left)]

            if(instr == 'R'):
                current = mapa[current][1]
            else:
                current = mapa[current][0]

            cont += 1

        res.append(cont)


print("Second problem: ", lcm(*res))