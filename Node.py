class Node:
    def __init__(self):
        super().__init__()
        self._leftValor = None
        self._rightValor = None
        self._father = None
        self._children = []
        self._edgeWeightInPath = 0
        self._heuristic = 0

    def setValors(self, left, right):
        self._leftValor = left
        self._rightValor = right
        self.setHeuristic(right)

    def setChildren(self, node):
        self._children.append(node)

    def setFather(self, node):
        self._father = node

    def setEdgeWeightInPath(self, valor):
        self._edgeWeightInPath = self._father.getEdgeWeightInPath() + valor

    def setHeuristic(self, right):
        self._heuristic = 6
        for val in right:
            if val == 'M' or val == 'C':
                self._heuristic -= 1

    def getLeftValor(self):
        return self._leftValor

    def getRightValor(self):
        return self._rightValor

    def getChildren(self):
        return self._children

    def getFather(self):
        return self._father

    def getEdgeWeightInPath(self):
        return self._edgeWeightInPath

    def getHeuristic(self):
        return self._heuristic

    def getEvaluationFunction(self):
        return self._edgeWeightInPath + self._heuristic

    def removeLastChild(self):
        self._children.pop()

    def printNode(self):
        print("[ ", end="")
        for valor in self._leftValor:
            print(valor, end=" ")
        print("], [ ", end="")
        for valor in self._rightValor:
            print(valor, end=" ")
        print("]")

    def printNodes(self, level = 0):
        ret = "\t"*level
        ret += str(self._edgeWeightInPath)
        ret += "[ "
        for valor in self._leftValor:
            ret += valor + " "
        ret += "], [ "
        for valor in self._rightValor:
            ret += valor + " "
        ret += "] \n"
        for child in self.getChildren():
            if(child != None):
                ret += child.printNodes(level+1)
        return ret
