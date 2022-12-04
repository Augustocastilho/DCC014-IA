from abc import abstractmethod
from Node import Node
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
        self.__goalState = [[], ['B', 'M', 'M', 'M', 'C', 'C', 'C']]
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

    # regra 1: mover 1 missionario
    def rule1(self, node):
        newNode = Node()
        if "B" in node.getLeftValor():
            left = node.getLeftValor().copy().remove("B").remove("M")
            right = node.getRightValor().copy().append("B").append("M")
        else:
            left = node.getLeftValor().copy().append("B").append("M")
            right = node.getRightValor().copy().remove("B").remove("M")

        if self.validate(left, right):
            newNode.setValors(left, right)
            return newNode
        return None
    
    # regra 2: mover 2 missionarios
    def rule2(self, node):
        newNode = Node()
        if "B" in node.getLeftValor():
            left = node.getLeftValor().copy().remove("B").remove("M").remove("M")
            right = node.getRightValor().copy().append("B").append("M").append("M")
        else:
            left = node.getLeftValor().copy().append("B").append("M").append("M")
            right = node.getRightValor().copy().remove("B").remove("M").remove("M")

        if self.validate(left, right):
            newNode.setValors(left, right)
            return newNode
        return None
    
    # regra 3: mover 1 canibal
    def rule3(self, node):
        newNode = Node()
        if "B" in node.getLeftValor():
            left = node.getLeftValor().copy().remove("B").remove("C")
            right = node.getRightValor().copy().append("B").append("C")
        else:
            left = node.getLeftValor().copy().append("B").append("C")
            right = node.getRightValor().copy().remove("B").remove("C")
        
        if self.validate(left, right):
            newNode.setValors(left, right)
            return newNode
        return None
    
    # regra 4: mover 2 canibais
    def rule4(self, node):
        newNode = Node()
        if "B" in node.getLeftValor():
            left = node.getLeftValor().copy().remove("B").remove("C").remove("C")
            right = node.getRightValor().copy().append("B").append("C").append("C")
        else:
            left = node.getLeftValor().copy().append("B").append("C").append("C")
            right = node.getRightValor().copy().remove("B").remove("C").remove("C")
        
        if self.validate(left, right):
            newNode.setValors(left, right)
            return newNode
        return None

    # regra 5: mover 1 missionario e 1 canibal
    def rule5(self, node):
        newNode = Node()
        if "B" in node.getLeftValor():
            left = node.getLeftValor().copy().remove("B").remove("M").remove("C")
            right = node.getRightValor().copy().append("B").append("M").append("C")
        else:
            left = node.getLeftValor().copy().append("B").append("M").append("C")
            right = node.getRightValor().copy().remove("B").remove("M").remove("C")
        
        if self.validate(left, right):
            newNode.setValors(left, right)
            return newNode
        return None

    def validate(self, left, right):
        numM = 0
        numC = 0

        for valor in left:
            if valor == "M":
                numM += 1
            elif valor == "C":
                numC += 1
        if numC > numM:
            return False
        
        numM = 0
        numC = 0
        for valor in right:
            if valor == "M":
                numM += 1
            elif valor == "C":
                numC += 1
        if numC > numM:
            return False
        return True

    def getSolutionPath(self):
        return self.__solutionPath

    # seleciona as regras a serem aplicadas ou retorna None
    @abstractmethod
    def rules(self, node):
        pass

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def expand(self, rule):
        pass
