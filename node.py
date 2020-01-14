class Node:

    isMarked = False
    weight = 999999

    def __init__(self, positionInVector, nodeId, links):

        self.positionInVector = positionInVector
        self.nodeId = nodeId
        self.links = links

    def getPositionInVector(self):
         return self.positionInVector

    def getNodeId(self):
        return self.nodeId

    def returnVisitBoolean(self):
        return self.isMarked

    def returnNodeWeight(self):
        return self.weight

    def returnLinks(self):
        return self.links

    def markAsVisited(self):
        self.isMarked = True

    def addToLink(self, newNode):
        self.links.add(newNode)

    def setNodeId(self, nodeId):
        self.nodeId = nodeId

    def setPositionInVector(self, positionInVector):
        self.positionInVector = positionInVector

    def setWeight(self, weight):
        self.weight = weight