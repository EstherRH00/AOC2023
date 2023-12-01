entrada = open("input_01")
lines = entrada.readlines()
entrada.close()

nombres = []

for l in lines:
    n1 = ""
    n2 = ""
    for c in l:
        if(c.isdigit()):
            if(len(n1) == 0):
                n1 = c
            else:
                n2 = c
    n = (int) (n1 + n2) if n2 != "" else (int) (n1+n1)
    nombres.append(n)

print("First problem: ", sum(nombres))

nombres = []

for l in lines:
    n1 = ""
    n2 = ""
    i = 0
    while i < len(l):
        k= i
        if l[i] == "1" or l[i] == "2" or l[i] == "3" or l[i] == "4" or l[i] == "5" or l[i] == "6" or l[i] == "7" or l[i] == "8" or l[i] == "9" or l[i] == "0":
            if n1 == "":
                n1 = l[i]
            else:
                n2 = l[i]
            i += 1
        if i < len(l) - 3 and k == i:
            if l[i:i+3] == "one":
                if n1 == "":
                    n1 = "1"
                else:
                    n2 = "1"
                i += 1
            if l[i:i+3] == "two":
                if n1 == "":
                    n1 = "2"
                else:
                    n2 = "2"
                i += 1
            if l[i:i+3] == "six":
                if n1 == "":
                    n1 = "6"
                else:
                    n2 = "6"
                i += 1

        if i < len(l) - 4 and k == i:
            if l[i:i+4] == "four":
                if n1 == "":
                    n1 = "4"
                else:
                    n2 = "4"
                i += 1
            if l[i:i+4] == "five":
                if n1 == "":
                    n1 = "5"
                else:
                    n2 = "5"
                i += 1
            if l[i:i+4] == "nine":
                if n1 == "":
                    n1 = "9"
                else:
                    n2 = "9"
                i += 1

        if i < len(l) - 5 and k == i:
            if l[i:i+5] == "three":
                if n1 == "":
                    n1 = "3"
                else:
                    n2 = "3"
                i += 1
            if l[i:i+5] == "seven":
                if n1 == "":
                    n1 = "7"
                else:
                    n2 = "7"
                i += 1
            if l[i:i+5] == "eight":
                if n1 == "":
                    n1 = "8"
                else:
                    n2 = "8"
                i += 1
        if k == i:
            i += 1

    n = (int)(n1 + n2) if n2 != "" else (int)(n1 + n1)
    nombres.append(n)

print("Second problem: ", sum(nombres))