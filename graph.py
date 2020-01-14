import node

class Graph:

    def __init__(self, nodes):
        self.nodes = nodes

    def getNodes(self):
        return self.nodes

    def getNodeAtPosition(self,pos):
        return self.nodes[pos]

    def getNodesSize(self):
        return self.nodes.size()

    def addToNodes(self, node):
        self.nodes.add(node)