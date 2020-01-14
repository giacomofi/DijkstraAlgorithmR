from graph import Graph
from node import Node
import time
from fibonacci_heap_mod import Fibonacci_heap


class FibonacciHeapDijkstra:

    def __init__(self):
        pass

    nodeLinkAndCost = []
    fibHeaps = []
    fibHeap = Fibonacci_heap()

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

        actual = 1

        for j in range(numberOfNodes, linesSize):
            arcAndCost = lines[j].split("=")
            arcElements = arcAndCost[0].split(",")
            entry = (int(arcElements[0]), int(arcElements[1]))
            priority = int(arcAndCost[1])

            if actual == int(arcElements[0]):
                self.fibHeap.enqueue(entry, priority)
            else:
                actual = int(arcElements[0])
                self.fibHeaps.append(self.fibHeap)
                self.fibHeap = Fibonacci_heap()
                self.fibHeap.enqueue(entry, priority)
            if j == linesSize - 1:
                self.fibHeaps.append(self.fibHeap)

        for i in range(0, numberOfNodes):
            if i == 0:
                g.getNodes()[i].setWeight(0)
            else:
                g.getNodes()[i].setWeight(999999)

        return g

    def dijkstraWithFibonacciHeap(self):

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
                elementInExam = ((self.fibHeaps[next]).dequeue_min()).get_value()[1]
                next = elementInExam - 1
                predecessors.append(selected)
                selected = elementInExam

        predecessors.append(sink)

        print("Dijkstra Algorithm performed in " + str((time.clock() - start)))

        return predecessors
