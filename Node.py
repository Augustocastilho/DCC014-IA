

class Node:
    # valores a esquerda do rio e a direita do rio
    _leftValor = []
    _rightValor = []
    _children = []
    _father = None

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
