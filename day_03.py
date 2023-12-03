entrada = open("input_03")
lines = entrada.readlines()
entrada.close()

# Parsing
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    lines[i] = "." + lines[i][:] + "."

lines.insert(0, "."*len(lines[0]))
lines.append("."*len(lines[0]))

n_files = len(lines)
n_cols = len(lines[0])

acumulador = 0

for i in range(1,n_files-1):
    num_act = ""
    for j in range(1,n_cols):
        if lines[i][j].isdigit():
            num_act += lines[i][j]
        elif not lines[i][j].isdigit() and num_act != "":
            # buscar si te un simbol al voltant
            k = j - len(num_act) - 1
            trobat = False
            while k <= j and not trobat:
                trobat = (not lines[i][k].isdigit() and lines[i][k] != ".") \
                         or (not lines[i-1][k].isdigit() and lines[i-1][k] != ".") \
                         or (not lines[i+1][k].isdigit() and lines[i+1][k] != ".")
                k += 1
            if trobat:
                acumulador += (int)(num_act)
            num_act = ""

print("First problem: ", acumulador)

acumulador = 0
gears = dict()

for i in range(1,n_files-1):
    num_act = ""
    for j in range(1,n_cols):
        if lines[i][j].isdigit():
            num_act += lines[i][j]
        elif not lines[i][j].isdigit() and num_act != "":
            # buscar si te un simbol al voltant
            k = j - len(num_act) - 1
            trobat = False
            key = ""
            while k <= j and not trobat:
                if (not lines[i][k].isdigit() and lines[i][k] == "*"):
                    trobat = True
                    key = (str)(i) + "-" + (str)(k)
                if (not lines[i-1][k].isdigit() and lines[i-1][k] == "*"):
                    trobat = True
                    key = (str)(i-1) + "-" + (str)(k)
                if (not lines[i+1][k].isdigit() and lines[i+1][k] == "*"):
                    trobat = True
                    key = (str)(i+1) + "-" + (str)(k)
                k += 1
            n = (int)(num_act)
            if key in gears:
                gears[key].append(n)
            else:
                gears[key] = [n]

            num_act = ""


for key, val in gears.items():
    if len(val) == 2:
        acumulador += val[0] * val[1]

print("Second problem: ", acumulador)