

class Node:
    # valores a esquerda do rio e a direita do rio
    __leftValor = []
    __rightValor = []
    __childrenNodes = []
    __fatherNode = None
    __rules = []

    def setValors(self, left, right):
        self.__leftValor = left
        self.__rightValor = right

    def setChildrenNode(self, node):
        node.setFather(self)
        self.__childrenNodes.append(node)

    def setFather(self, node):
        self.__fatherNode = node

    def setRules(self, rule):
        self.__rules.append(rule)

    def getLeftValor(self):
        return self.__leftValor

    def getRightValor(self):
        return self.__rightValor

    def getChildrenNodes(self):
        return self.__childrenNodes

    def getFatherNode(self):
        return self.__fatherNode

    def getRules(self):
        return self.__rules

    def printNode(self):
        print("[ ", end="")
        for valor in self.__leftValor:
            print(valor, end=" ")
        print("], [ ", end="")
        for valor in self.__rightValor:
            print(valor, end=" ")
        print("]")
