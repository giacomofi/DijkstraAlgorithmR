from graph import Graph
from node import Node
import time


class HeapDijkstra:

    def __init__(self):
        pass

    nodeLinkAndCost = []
    heaps = []
    finalHeap = []

    def createGraph(self):

        nodes = []
        g = Graph(nodes)
        f = open("GeneratedGraph.txt", "r")
        lines = f.readlines()
        linesSize = len(lines)
        f.close()
        numberOfNodes = int(lines[0])
        allNodeLinks = []

        for i in range(0, numberOfNodes):
            for j in range(1, numberOfNodes):
                nodeAndLinks = lines[j].split("->")
                links = nodeAndLinks[1].split(",")
                allNodeLinks.append(links)
            n = Node(i, i + 1, allNodeLinks[i])
            g.getNodes().append(n)

        for j in range(numberOfNodes, linesSize):
            arcAndCost = lines[j].split("=")
            arcElements = arcAndCost[0].split(",")
            self.heaps.append((int(arcElements[0]), int(arcElements[1]), int(arcAndCost[1])))

        finalHeaps = []
        actual = self.heaps[0][0]

        for i in range(0, len(self.heaps)):

            y = self.heaps[i][0]

            if (actual == y):
                finalHeaps.append(self.heaps[i])
            if (actual != y):
                actual = y
                self.nodeLinkAndCost.append(finalHeaps)
                finalHeaps = []
                finalHeaps.append(self.heaps[i])

            if (i == len(self.heaps) - 1):
                self.nodeLinkAndCost.append(finalHeaps)


        for i in range(0,len(self.nodeLinkAndCost)):
            self.finalHeap.append((sorted(self.nodeLinkAndCost[i], key=lambda tup: tup[2])))


        for i in range(0, numberOfNodes):
            if i == 0:
                g.getNodes()[i].setWeight(0)
            else:
                g.getNodes()[i].setWeight(999999)

        return g

    def dijkstraWithHeap(self):

        graph = self.createGraph()
        nodes = graph.getNodes()
        temporaryNodes = nodes
        selected = temporaryNodes[0].getNodeId()
        print("Init " + str(selected))
        sink = nodes[len(nodes) - 1].getNodeId()
        print("The sink is " + str(sink))
        predecessors = []
        trigger = selected
        next = 0

        start = time.clock()

        while trigger != sink:
             print("Node actually selected is: " + str(selected))
             trigger = selected

             if selected != sink:
                 tupleInExam = (self.finalHeap[next])[0]
                 elementInExam = tupleInExam[1]
                 next = elementInExam-1
                 predecessors.append(selected)
                 selected = elementInExam

        predecessors.append(sink)

        print("Dijkstra Algorithm performed in " + str((time.clock() - start)))

        return predecessors







