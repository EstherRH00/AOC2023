entrada = open("input_05")
lines = entrada.readlines()
entrada.close()

seeds = {val: False for val in lines[0].split()[1:]}
new = list()

for line in lines[3:]:
    vals = line.split()
    if (len(vals)) == 2:
        for s in seeds.keys():
            if not seeds[s]:
                new.append((int)(s))
        #print(seeds, new)
        seeds = {val: False for val in new}
        new = list()
    elif (len(vals)) == 3:
        for seed in seeds:
            s = (int)(seed)
            d = (int)(vals[0])
            o = (int)(vals[1])
            r = (int)(vals[2])
            if not seeds[seed] and o <= s and s < o+r:
                new.append(d+s-o)
                seeds[seed] = True
for s in seeds.keys():
    if not seeds[s]:
        new.append((int)(s))


print("First problem: ", min(new))

seeds = dict()
aux = lines[0].split()[1:]
for i in range(0, len(aux), 2):
    seeds[((int)(aux[i]), (int)(aux[i])+(int)(aux[i+1])-1)] = False

d2 = dict()

for line in lines[3:]:
    vals = line.split()
    if(len(vals)) == 2:
        seeds = {seed: False for seed in seeds.keys()}

    if (len(vals)) == 3:
        d2 = dict()
        for seed in seeds.keys():
            s_0 = seed[0]
            s_1 = seed[1]
            d = (int)(vals[0])
            o = (int)(vals[1])
            r = (int)(vals[2])

            if not seeds[seed]:
                if s_0 >= o and s_1 < o+r:
                    d2[( d + s_0-o, d + s_1-o)] = True
                elif s_0 >= o and s_0 < o+r:
                    d2[( d + s_0-o, d + r -1)] = True
                    d2[(o+r, s_1)] = False
                elif s_1 >= o and s_1 < o + r:
                    d2[(d, d + s_1 - o)] = True
                    d2[(s_0, o-1)] = False
                else:
                    d2[(s_0, s_1)] = False
            else:
                d2[(s_0, s_1)] = True
        seeds = d2



print("Second problem: ", min(seeds.keys())[0])