entrada = open("input_09")
lines = entrada.read().splitlines()
entrada.close()

acc = 0

for l in lines:
    sep = [(int)(i) for i in l.split()]

    while sep != [0]*len(sep):
        acc += sep[-1]
        for i in range(len(sep)-1):
            sep[i] = sep[i+1]-sep[i]
        sep.pop()

print("First problem: ", acc)

acc = 0

for l in lines:
    sep = [(int)(i) for i in l.split()]
    sep = sep[::-1]

    while sep != [0]*len(sep):
        acc += sep[-1]
        for i in range(len(sep)-1):
            sep[i] = sep[i+1]-sep[i]
        sep.pop()

print("Second problem: ",acc)