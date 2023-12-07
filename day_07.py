from collections import Counter

entrada = open("input_07")
lines = entrada.readlines()
entrada.close()

# 5 of a kind
# 4 of a kind
# full house (3-2)
# 3 of a kind
# 2 pair
# 1 pair
# high card

n = len(lines)
acc = 0
cards = {5: [], 4: [], '3-2': [], 3: [], 2: [], 1: [], 0: []}
bids = {}

for l in lines:
    c, bid = l.split()
    bid = (int)(bid)
    contador = Counter(c).values()

    bids[c] = bid
    
    if max(contador) == 5:
        cards[5].append(c)
    elif max(contador) == 4:
        cards[4].append(c)
    elif set(contador) == {3,2}:
        cards['3-2'].append(c)
    elif max(contador) == 3:
        cards[3].append(c)
    elif list(contador) == [2,2,1] or list(contador) == [2,1,2] or list(contador) == [1,2,2]:
        cards[2].append(c)
    elif 2 in contador:
        cards[1].append(c)
    else:
        cards[0].append(c)

custom_order = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

for k in [5,4,'3-2',3,2,1,0]:
    c = cards[k]
    c_sorted = sorted(c, key=lambda x: [custom_order.get(ch) for ch in x], reverse=True)

    for card in c_sorted:
        acc += bids[card] * n
        n -= 1

print("First problem: ", acc)

n = len(lines)
acc = 0
cards = {5: [], 4: [], '3-2': [], 3: [], 2: [], 1: [], 0: []}
bids = {}

for l in lines:
    c, bid = l.split()
    bid = (int)(bid)
    contador = Counter(c).values()

    bids[c] = bid

    n_j = c.count('J')

    if(n_j != 5):
        c_mod = c.replace('J', '')
        lletra_mes_comuna = Counter(c_mod).most_common(1)[0][0]
        contador = Counter(c.replace('J', lletra_mes_comuna)).values()

    if max(contador) == 5:
        cards[5].append(c)
    elif max(contador) == 4:
        cards[4].append(c)
    elif set(contador) == {3, 2}:
        cards['3-2'].append(c)
    elif max(contador) == 3:
        cards[3].append(c)
    elif list(contador) == [2, 2, 1] or list(contador) == [2, 1, 2] or list(contador) == [1, 2, 2]:
        cards[2].append(c)
    elif 2 in contador:
        cards[1].append(c)
    else:
        cards[0].append(c)

custom_order = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
                '2': 2}

for k in [5, 4, '3-2', 3, 2, 1, 0]:
    c = cards[k]
    c_sorted = sorted(c, key=lambda x: [custom_order.get(ch) for ch in x], reverse=True)

    for card in c_sorted:
        acc += bids[card] * n
        n -= 1

print("Second problem: ", acc)