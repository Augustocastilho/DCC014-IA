

class Node:
    # valores a esquerda do rio e a direita do rio
    __leftValor = []
    __rightValor = []
    __childrenNodes = []
    __fatherNode = None

    def setValors(self, left, right):
        self.__leftValor = left
        self.__rightValor = right

    def setChildrenNode(self, node):
        self.__childrenNodes.append(node)

    def setFather(self, node):
        self.__fatherNode = node

    def getLeftValor(self):
        return self.__leftValor

    def getRightValor(self):
        return self.__rightValor

    def getChildrenNodes(self):
        return self.__childrenNodes

    def getFatherNode(self):
        return self.__fatherNode
