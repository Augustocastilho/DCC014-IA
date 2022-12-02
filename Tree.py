from Node import Node


class Tree(object):
    __root = Node()

    def __init__(self):
        self.__root.setValors(['B', 'M', 'M', 'M', 'C', 'C', 'C'], [
                              "V", "V", "V", "V", "V", "V", "V"])

    def getRoot(self):
        return self.__root

    # apenas para teste, deve ser substituido por um printTree
    def printRoot(self):
        left = self.__root.getLeftValor()
        print("[ ", end="")
        for valor in left:
            print(valor, end=" ")
        print("], [ ", end="")
        right = self.__root.getRightValor()
        for valor in right:
            print(valor, end=" ")
        print("]")
