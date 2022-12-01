from Tree.Node import Node


class Tree(object):
    __root = [Node]
    __leafs = []

    def __init__(self):
        self.__root.setValor([['B', 'M', 'M', 'M', 'C', 'C', 'C'], [0, 0, 0, 0, 0, 0, 0]])
        self.__leafs = self.__root

    def printRoot(self):
        print(self.__root)
