import random


def readFile():
    def readFile(filename):
    global rows
    global cols
    global minIngredient
    global maxCells
    
    f = open(filename+".in", 'r')
    params = f.readline()
    paramlist = params.split(" ")

    rows.append(int(paramlist[0]))
    cols.append(int(paramlist[1]))
    minIngredient.append(int(paramlist[2]))
    maxCells.append(int(paramlist[3]))

    pizza = []
    
    for row in range(rows[-1]):
        pizza.append(f.readline()[:-1])

    return pizza


random.seed()

data = readFile()
