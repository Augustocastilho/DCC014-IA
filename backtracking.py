

from Node import Node


class backtracking(object):
    __initalState = []
    __goalState = [["V", "V", "V", "V", "V", "V", "V"],
                   ['B', 'M', 'M', 'M', 'C', 'C', 'C']]
    __currentNode = Node()
    __fail = False
    __success = False
    __deepLimit = 0
    __deep = 0
    __solutionPath = []

    def __init__(self, initial, deepLimit=0):
        self.__initalState = initial
        self.__currentNode = initial
        self.__deepLimit = deepLimit

    def backtrackingSearch(self):
        while self.__success == False and self.__fail == False:
            # se o limite de profundidade for atingido, volta para o pai
            if self.__deepLimit != 0 and self.__deep >= self.__deepLimit:
                self.back()

            rule = self.rule(self.__currentNode)
            if rule != None:
                self.expand(rule)
                # verifica se o estado atual é o estado objetivo
                if self.isGoal(self.__currentNode):
                    self.__success = True
            else:
                # se nao houver regra a ser aplicada, volta para o pai
                if self.__currentNode == self.__initalState:
                    self.__fail = True
                else:
                    self.back()

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

    # volta para o pai
    def back(self):
        self.__currentNode = self.__currentNode.getFatherNode()
        self.__solutionPath.pop()
        self.__deep -= 1

    # avança para o filho
    def expand(self, node):
        self.__currentNode = self.__currentNode.setChildrenNode(node)
        self.__solutionPath.append(self.__currentNode)
        self.__deep += 1

    def getSolutionPath(self):
        return self.__solutionPath
