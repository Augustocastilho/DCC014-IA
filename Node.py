

class Node:
    # valores a esquerda do rio e a direita do rio
    _leftValor = []
    _rightValor = []
    _childrenNodes = []
    _fatherNode = None
    _ruleNumber = 0

    def setValors(self, left, right):
        self._leftValor = left
        self._rightValor = right

    def setChildrenNode(self, node):
        node.setFather(self)
        self._childrenNodes.append(node)

    def setFather(self, node):
        self._fatherNode = node

    def setRuleNumber(self, ruleNumber):
        self._ruleNumber = ruleNumber

    def getLeftValor(self):
        return self._leftValor

    def getRightValor(self):
        return self._rightValor

    def getChildrenNodes(self):
        return self._childrenNodes

    def getFatherNode(self):
        return self._fatherNode

    def getRuleNumber(self):
        return self._ruleNumber

    def printNode(self):
        print("[ ", end="")
        for valor in self._leftValor:
            print(valor, end=" ")
        print("], [ ", end="")
        for valor in self._rightValor:
            print(valor, end=" ")
        print("]")
