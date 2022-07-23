"""
Basic vertex function
Version 1.0
2022.07.18 Made by R.e.
"""


class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacency = {}
        self.isVisited = 0

    def getId(self):
        return self.id

    def getADJ(self):
        return self.adjacency.keys()

    def addADJ(self, neighbor, weight):
        self.adjacency[neighbor] = weight

    def delADJ(self, neighbor):
        if neighbor in self.adjacency.keys():
            del self.adjacency[neighbor]

    def getWeight(self, neighbor):
        if neighbor in self.adjacency.keys():
            return self.adjacency[neighbor]
        return -1

    def __str__(self):
        res = str(self.id) + \
              '\tadjacency: ' + str([(k, v) for (k, v) in self.adjacency.items()])
        return res
