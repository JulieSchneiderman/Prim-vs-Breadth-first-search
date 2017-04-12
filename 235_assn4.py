#CISC 235 Assignment 4
#Julie Schneiderman - 10201092
''' “I confirm that this
submission is my own work and is consistent with the Queen's regulations on Academic
Integrity.”'''

import random

#Creates a Graph object with the following attributes
class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def addEdge(self,f,t,cost=0):
        if f not in self.vertexList:
            newVertex = self.addVertex(f)
        if t not in self.vertexList:
            newVertex = self.addVertex(t)
        self.vertexList[f].addNeighbor(self.vertexList[t], cost)

    def getVertices(self):
        return self.vertexList.keys() #vertices

    def __iter__(self):
        return iter(self.vertexList.values()) #weights


#Creates a Vertex object with the following attributes
class Vertex:
    def __init__(self,key):
        self.vNum = key #vertex
        self.connectedTo = {} #dictionary for vertex's neigbours
        self.inT = False
        self.connector = None
        self.cost = None

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getVNum(self):
        return self.vNum

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

#Creates a Queue object with the following attributes
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def remove_first(self):
        return self.items.pop()
    
#Breadth-first search function
#input - graph object and a random starting vertex
#output - the total weight of the edges the search selects
def bfs(g,start):
    Q = Queue()
    total = 0
    visited = [False]*len(g.vertexList)
    #set start as visited
    visited[start] = True
    Q.insert(g.vertexList[start]) #add it to the queue
    while (not(Q.isEmpty())):
           y = Q.remove_first() 
           for x in y.getConnections():
                vNum = x.vNum
                if visited[vNum] == False:
                   visited[vNum] = True
                   Q.insert(x)
                   total += x.getWeight(y)
    return total


#Prims algorithm
#input - graph object
#ouput - the total weight of the edges it selects
def prim(g):
    v = g.vertexList[0]
    totalWeight = 0
    v.inT = True
    v.cost = 100000 #infinity
    for y in g.getVertices():
        vert = g.vertexList[y]
        vert.inT == False
        vert.cost = 100000
        vert.connector = None
    for x in v.getConnections():
        vNum = x.vNum
        vert = g.vertexList[vNum]
        vert.cost = v.getWeight(vert)
        vert.connector = 0
    for count in range(1,(len(g.vertexList))):
        smallestCost = 100000 
        for x in g.getVertices():
            vert = g.vertexList[x]
            if vert.inT == False: 
                if vert.cost < smallestCost:
                    smallestV = vert
                    smallestCost = vert.cost
        totalWeight += smallestCost
        smallestV.inT = True
        smallestV.cost = 100000
        smallestV.connector = None
        for y in smallestV.getConnections():
            vNum = y.vNum
            vert = g.vertexList[vNum]
            if vert.inT == False:
                if vert.getWeight(smallestV) < vert.cost:
                    vert.cost = vert.getWeight(smallestV)
                    vert.connector = smallestV
    return totalWeight

#runs the search algorithms and sends a list of all the % differences to
#getAvgPercentDifference()
def comparison():
    dlist = []
    for k in range(250): #number of random graphs generated
        g = Graph() #new graph object
        for i in range(2,62): #create graph with (2,n) vertices
            x = random.randint(1,i-1) 
            S = random.sample(range(i-1),x)
            for s in S:
                w = random.randint(10,100)
                g.addEdge(i,s,w) #new vertex i, old vertex s, weight w
                g.addEdge(s,i,w) #creates edge going in both directions

        start = random.randint(1,20)
        B = bfs(g,start)
        P = prim(g)
        Diff = (B/P -1)*100 #Percent Different Calculation
        dlist.append(Diff)
        #print("bfs total weight: ", B)
        #print("prim total weight: ", P)
        #print("% Diff is: ",Diff,"\n")
    print("Average Percent Difference is", getAvgPercentDifference(dlist), "%")

#computes the results and returns the average percent difference
def getAvgPercentDifference(lst):
    print("results:")
    num = 0
    for i in lst:
        num +=i
    averagePercentDifference = num/len(lst)
    averagePercentDifference = round(averagePercentDifference,3)
    return averagePercentDifference

 
def main():
    comparison()

main()


