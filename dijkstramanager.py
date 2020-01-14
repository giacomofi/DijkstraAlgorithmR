from graph import Graph
from node import Node
import time

class DijkstraManager:

    arcCost = {}
    permanentNodes = []
    temporaryNodes = []
    minimumPath = []

    def __init__(self):
        pass

    def findMinimum(self,selected,graphNodes):

        links = selected.returnLinks()
        size = len(selected.returnLinks())
        node = graphNodes[int(selected.returnLinks()[0])-1]
        actual = int(self.arcCost.get((selected.getNodeId(),graphNodes[int(links[0])-1].getNodeId())))

        if size > 1:

            for i in range(0,size-1):
                if(actual > int(self.arcCost.get((selected.getNodeId(), graphNodes[int(links[i+1])- 1].getNodeId())))):
                    actual = int(self.arcCost.get((selected.getNodeId(), graphNodes[int(links[i+1]) - 1].getNodeId())))
                    node = graphNodes[int(links[i+1])-1]
            return node

        else:
            return node

    def createGraph(self):

        nodes = []
        g = Graph(nodes)
        f = open("GeneratedGraph.txt","r")
        lines = f.readlines()
        linesSize = len(lines)
        f.close()
        numberOfNodes = int(lines[0])
        allNodeLinks = []

        for i in range(0,numberOfNodes):
            for j in range(1,numberOfNodes):
                nodeAndLinks = lines[j].split("->")
                links = nodeAndLinks[1].split(",")
                allNodeLinks.append(links)
            n = Node(i,i+1,allNodeLinks[i])
            g.getNodes().append(n)

            for j in range(numberOfNodes,linesSize):
                arcAndCost = lines[j].split("=")
                arcElements = arcAndCost[0].split(",")


                self.arcCost.update({(int(arcElements[0]),int(arcElements[1])) : int(arcAndCost[1])})
                print(time.clock())
        for i in range(0,numberOfNodes):
            if i == 0:
                g.getNodes()[i].setWeight(0)
            else:
                g.getNodes()[i].setWeight(999999)




        return g



    def dijkstra(self):

        graph = self.createGraph()
        nodes = graph.getNodes()
        self.temporaryNodes = nodes
        selected = self.temporaryNodes[0]
        sink = nodes[len(nodes)-1]
        predecessors = []
        trigger = selected


        start = time.clock()


        while trigger != sink :
            print("Node actually selected is: " + str(selected.getNodeId()))
            trigger = selected

            if selected.getNodeId() != sink.getNodeId():
                links = selected.returnLinks()




                for i in range(0,len(links)):

                    alt = selected.returnNodeWeight() + int(self.arcCost.get((selected.getNodeId(), nodes[int(links[i])-1].getNodeId())))
                    if alt < nodes[int(links[i])-1].returnNodeWeight():
                        print("Updating weight of " + str(selected.getNodeId()) + " and " + str(nodes[int(links[i])-1].getNodeId()) + " with " + str(alt) )
                        nodes[int(links[i]) - 1].setWeight(alt)
                    else:
                        print("Nothing to update for arc " + str(selected.getNodeId()) + "," +  str(nodes[int(links[i])-1].getNodeId()))


                self.permanentNodes.append(selected)
                selected = self.findMinimum(selected, nodes)

            predecessors.append(trigger.getNodeId())


        print("Dijkstra Algorithm performed in " + str((time.clock() - start)))

        return predecessors








































