from abc import abstractmethod
from Tree import Tree


class Search():
    __tree = Tree()
    __initalState = None
    __goalState = None
    __currentNode = None
    __fail = False
    __success = False
    __deep = 0
    __deepLimit = 0
    __solutionPath = []

    def __init__(self, deepLimit=0):
        self.__initalState = self.__tree.getRoot()
        self.__goalState = [["V", "V", "V", "V", "V", "V", "V"],
                            ['B', 'M', 'M', 'M', 'C', 'C', 'C']]
        self.__currentNode = self.__tree.getRoot()
        self.__deepLimit = deepLimit

    def isGoal(self, node):
        node = node.getRightValor()
        result = set(node) & set(self.__goalState[1])
        # result eh a intersecao entre os dois conjuntos
        if result.__len__() == 7:
            return True
        else:
            return False

    # seleciona a regra a ser aplicada ou retorna None
    def rule(self, node):
        # implementar regras do problema
        return None

    def getSolutionPath(self):
        return self.__solutionPath

    @abstractmethod
    def expand(self, rule):
        pass
