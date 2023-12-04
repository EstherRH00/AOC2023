entrada = open("input_04")
lines = entrada.readlines()
entrada.close()

acumulador = 0

for line in lines:
    if(line[-1] == '\n'): line = line[:-1]
    separated = line.split(" ")
    i = 2 #Ignoro el "Card n:"
    cont = -1
    winners = []
    while(separated[i] != "|"):
        if(separated[i].isdigit()):
            winners.append(separated[i])
        i += 1
    i += 1

    while(i < len(separated)):
        if separated[i] in winners:
            cont += 1
        i += 1
    acumulador += 2**cont if cont != -1 else 0

print("First problem: ", acumulador)

cards = dict() # {card id: amount}

acumulador = 0

k = 0
for line in lines:
    if(line[-1] == '\n'): line = line[:-1]
    separated = line.split(" ")
    key = (int)(line[5:8])

    if(key in cards.keys()):
        cards[key] += 1
    else:
        cards[key] = 1

    i = 2 #Ignoro el "Card n:"
    cont = 0
    winners = []
    while(separated[i] != "|"):
        if(separated[i].isdigit()):
            winners.append(separated[i])
        i += 1
    i += 1

    while(i < len(separated)):
        if separated[i] in winners:
            cont += 1
        i += 1


    for j in range(cont):
        k = key + j + 1
        if (k in cards.keys()):
            cards[k] += cards[key]
        else:
            cards[k] = cards[key]

    acumulador += cards[key]

print("Second problem: ", acumulador)