

class Node:
    # valores a esquerda do rio e a direita do rio
    _leftValor = []
    _rightValor = []
    _childrenNodes = []
    _fatherNode = None

    def setValors(self, left, right):
        self._leftValor = left
        self._rightValor = right

    def setChildrenNode(self, node):
        node.setFather(self)
        self._childrenNodes.append(node)

    def setFather(self, node):
        self._fatherNode = node

    def setRules(self, rule):
        self.__rules.append(rule)

    def getLeftValor(self):
        return self._leftValor

    def getRightValor(self):
        return self._rightValor

    def getChildrenNodes(self):
        return self._childrenNodes

    def getFatherNode(self):
        return self._fatherNode

    def getRules(self):
        return self.__rules

    def printNode(self):
        print("[ ", end="")
        for valor in self._leftValor:
            print(valor, end=" ")
        print("], [ ", end="")
        for valor in self._rightValor:
            print(valor, end=" ")
        print("]")
