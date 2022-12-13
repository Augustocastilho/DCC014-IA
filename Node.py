

class Node:
    def __init__(self):
        super().__init__()
        self._leftValor = None
        self._rightValor = None
        self._father = None
        self._children = []

    def setValors(self, left, right):
        self._leftValor = left
        self._rightValor = right

    def setChildren(self, node):
        self._children.append(node)

    def setFather(self, node):
        self._father = node

    def getLeftValor(self):
        return self._leftValor

    def getRightValor(self):
        return self._rightValor

    def getChildren(self):
        return self._children

    def getFather(self):
        return self._father

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
        ret += "[ "
        for valor in self._leftValor:
            ret += valor
        ret += "], [ "
        for valor in self._rightValor:
            ret += valor
        ret += "] \n"
        for child in self.getChildren():
            if(child != None):
                ret += child.printNodes(level+1)
        return ret
