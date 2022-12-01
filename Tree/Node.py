

class Node:
    __valor = []
    __childrenNodes = []
    __fatherNode = None

    def setValor(self, valor: []):
        self.__valor = valor

    def setNextNode(self, node):
        self.__childrenNodes.append(node)

    def setFather(self, node):
        self.__fatherNode = node

    def getValor(self):
        return self.__valor

    def getChildrenNodes(self):
        return self.__childrenNodes

    def getFatherNode(self):
        return self.__fatherNode
