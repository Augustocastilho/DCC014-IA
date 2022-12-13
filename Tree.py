from Node import Node


class Tree(object):
    _root = Node()

    def __init__(self):
        self._root.getChildren().clear()
        self._root.setValors(['B', 'M', 'M', 'M', 'C', 'C', 'C'], [])

    def getRoot(self):
        return self._root

    # apenas para teste, deve ser substituido por um printTree
    def printRoot(self):
        left = self._root.getLeftValor()
        print("[ ", end="")
        for valor in left:
            print(valor, end=" ")
        print("], [ ", end="")
        right = self._root.getRightValor()
        for valor in right:
            print(valor, end=" ")
        print("]")

    def printTree(self):
        print(self.getRoot().printNodes())