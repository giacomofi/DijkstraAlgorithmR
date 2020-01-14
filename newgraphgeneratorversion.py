import random

nodes = int(input(
    "Hello! This is an auto Graph Generator. This generator creates a random graph with ranndom arcs and random weights. Insert the number of nodes to start the fun!"))
counter = 0
f = open("GeneratedGraph.txt", "w")
f.write(str(nodes))
f.write("\n")

accumulator = 0
for x in range(1, nodes):
    f.write(str(x) + "->")
    if (x == 1):
        f.write(str(x + 1) + ",")
        f.write(str(x + 2) + ",")
        f.write(str(x + 3))

    else:
        if (x == nodes - 3 or x == nodes - 2 or x == nodes - 1):
            f.write(str(nodes))
        else:
            if(accumulator == 1):
                f.write(str(x + 1) + ",")
                f.write(str(x + 3) + ",")
                f.write(str(x + 4) + ",")
                f.write(str(x + 5))
            if (accumulator == 2):
                f.write(str(x + 1) + ",")
                f.write(str(x + 2) + ",")
                f.write(str(x + 3) + ",")
                f.write(str(x + 4))
            if (accumulator == 3):
                f.write(str(x + 1) + ",")
                f.write(str(x + 2) + ",")
                f.write(str(x + 3))
                accumulator = 0
    accumulator += 1

    f.write("\n")

f.close()

f = open("GeneratedGraph.txt", "r")

lines = f.readlines()

f.close()

f = open("GeneratedGraph.txt", "a")

for i in range(1, nodes):
    actualLine = lines[i].split("->")
    nodeExaminated = actualLine[0]
    restOfLine = actualLine[1]
    linksInFile = restOfLine.split(",")
    for x in linksInFile:

        if x == linksInFile[-1]:
            x = x.replace("\n", "")
        arcCost = random.randint(2, 100)
        f.write(str(nodeExaminated) + "," + str(x) + "=" + str(arcCost))
        f.write("\n")

f.close()

with open('GeneratedGraph.txt', 'r') as f:
    lines = f.readlines()

lines = [line.replace(' ', '') for line in lines]

with open('GeneratedGraph.txt', 'w') as f:
    f.writelines(lines)

f.close()
