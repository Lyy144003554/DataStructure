from ASFunction.VertexFunction import Vertex

'''
Basic graph function
Version 1.0
2022.07.18 Made by R.e.
'''


class Graph:
    def __init__(self):
        self.vertexList = {}
        self.Vertexnum = 0
        self.Edgenum = 0
        self.MSTnum = 0

    def getEgdeNum(self):
        return self.Edgenum

    def getVertexNum(self):
        return self.Vertexnum

    def addVertex(self, vertexID):
        self.Vertexnum += 1
        self.vertexList[vertexID] = Vertex(vertexID)

    def getVertex(self, vertexID):
        if vertexID in self.vertexList:
            return self.vertexList[vertexID]
        else:
            return None

    def addEdge(self, fromVertex, toVertex, weight):
        if fromVertex not in self.vertexList:
            self.addVertex(fromVertex)
        if toVertex not in self.vertexList:
            self.addVertex(toVertex)
        self.vertexList[fromVertex].addADJ(toVertex, weight)
        self.Edgenum += 1

    def delEdge(self, fromVertex, toVertex):
        if fromVertex in self.vertexList and toVertex in self.vertexList:
            self.vertexList[fromVertex].delADJ(toVertex)
            self.Edgenum -= 1

    def cost(self, fromVertex, toVertex):
        if fromVertex in self.vertexList:
            if toVertex in self.vertexList[fromVertex].getADJ():
                return self.vertexList[fromVertex].getWeight(toVertex)
        return -1

    def __str__(self):
        res = 'numEdge = ' + str(self.Edgenum) + '\n' + 'numVertex = ' + str(self.Vertexnum) + '\n'
        for v in self.vertexList.values():
            res += str(v) + '\n'
        return res
