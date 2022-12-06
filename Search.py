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
    __visiteds = []

    def __init__(self, deepLimit=0):
        self.__initalState = self.__tree.getRoot()
        self.__goalState = [[], ['B', 'M', 'M', 'M', 'C', 'C', 'C']]
        self.__currentNode = self.__tree.getRoot()
        self.__deepLimit = deepLimit
        self.__visiteds.append(self.__initalState)

    def isGoal(self, node):
        node = node.getRightValor()
        if node.__len__() == self.__goalState[1].__len__():
            return True
        else:
            return False

    # regra 1: mover 1 missionario
    def rule1(self, node):
        newNode = Node()
        try:
            if "B" in node.getLeftValor():
                left = node.getLeftValor().copy()
                left.remove("B")
                left.remove("M")
                right = node.getRightValor().copy()
                right.append("B")
                right.append("M")
            else:
                left = node.getLeftValor().copy()
                left.append("B")
                left.append("M")
                right = node.getRightValor().copy()
                right.remove("B")
                right.remove("M")
        except: # se nao houverem missionarios suficientes para mover
            return None

        if self.validate(left, right):
            newNode.setValors(left, right)
            return newNode
        return None
    
    # regra 2: mover 2 missionarios
    def rule2(self, node):
        newNode = Node()
        try:
            if "B" in node.getLeftValor():
                left = node.getLeftValor().copy()
                left.remove("B")
                left.remove("M")
                left.remove("M")
                right = node.getRightValor().copy()
                right.append("B")
                right.append("M")
                right.append("M")
            else:
                left = node.getLeftValor().copy()
                left.append("B")
                left.append("M")
                left.append("M")
                right = node.getRightValor().copy()
                right.remove("B")
                right.remove("M")
                right.remove("M")
        except:
            return None

        if self.validate(left, right):
            newNode.setValors(left, right)
            return newNode
        return None
    
    # regra 3: mover 1 canibal
    def rule3(self, node):
        newNode = Node()
        try:
            if "B" in node.getLeftValor():
                left = node.getLeftValor().copy()
                left.remove("B")
                left.remove("C")
                right = node.getRightValor().copy()
                right.append("B")
                right.append("C")
            else:
                left = node.getLeftValor().copy()
                left.append("B")
                left.append("C")
                right = node.getRightValor().copy()
                right.remove("B")
                right.remove("C")
        except:
            return None
        
        if self.validate(left, right):
            newNode.setValors(left, right)
            return newNode
        return None
    
    # regra 4: mover 2 canibais
    def rule4(self, node):
        newNode = Node()
        try:
            if "B" in node.getLeftValor():
                left = node.getLeftValor().copy()
                left.remove("B")
                left.remove("C")
                left.remove("C")
                right = node.getRightValor().copy()
                right.append("B")
                right.append("C")
                right.append("C")
            else:
                left = node.getLeftValor().copy()
                left.append("B")
                left.append("C")
                left.append("C")
                right = node.getRightValor().copy()
                right.remove("B")
                right.remove("C")
                right.remove("C")
        except:
            return None
        
        if self.validate(left, right):
            newNode.setValors(left, right)
            return newNode
        return None

    # regra 5: mover 1 missionario e 1 canibal
    def rule5(self, node):
        newNode = Node()
        try:
            if "B" in node.getLeftValor():
                left = node.getLeftValor().copy()
                left.remove("B")
                left.remove("M")
                left.remove("C")
                right = node.getRightValor().copy()
                right.append("B")
                right.append("M")
                right.append("C")
            else:
                left = node.getLeftValor().copy()
                left.append("B")
                left.append("M")
                left.append("C")
                right = node.getRightValor().copy()
                right.remove("B")
                right.remove("M")
                right.remove("C")
        except:
            return None
        
        if self.validate(left, right):
            newNode.setValors(left, right)
            return newNode
        return None

    
    def validate(self, left, right):
        return self.verifyCannibals(left, right) and self.verifyInPath(left)

    # verifica se o numero de canibais eh maior que o numero de missionarios
    def verifyCannibals(self, left, right):
        numM = 0
        numC = 0

        for valor in left:
            if valor == "M":
                numM += 1
            elif valor == "C":
                numC += 1
        if numM != 0 and numC > numM:
            return False
        
        numM = 0
        numC = 0
        for valor in right:
            if valor == "M":
                numM += 1
            elif valor == "C":
                numC += 1
        if numM != 0 and numC > numM:
            return False
        return True

    # verifica se o estado ja esta no caminho, True se nao estiver, False se estiver
    def verifyInPath(self, left):
        for value in self.getVisiteds():
            if self.equals(left, value.getLeftValor()):
                return False
        return True

    # compara se os valores de M, C e B sao iguais em ambos os vetores
    def equals(self, value1, value2):
        numM1 = 0
        numC1 = 0
        numB1 = 0

        numM2 = 0
        numC2 = 0
        numB2 = 0

        for valor in value1:
            if valor == "M":
                numM1 += 1
            elif valor == "C":
                numC1 += 1
            elif valor == "B":
                numB1 = 1
        
        for valor in value2:
            if valor == "M":
                numM2 += 1
            elif valor == "C":
                numC2 += 1
            elif valor == "B":
                numB2 = 1

        if numM1 == numM2 and numC1 == numC2 and numB1 == numB2:
            return True
        return False

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

    # getters and setters
    def getTree(self):
        return self.__tree

    def getInitalState(self):
        return self.__initalState

    def getGoalState(self):
        return self.__goalState

    def getCurrentNode(self):
        return self.__currentNode

    def setCurrentNode(self, currentNode):
        self.__currentNode = currentNode

    def getFail(self):
        return self.__fail

    def setFail(self, fail):
        self.__fail = fail

    def getSuccess(self):
        return self.__success

    def setSuccess(self, success):
        self.__success = success

    def getDeep(self):
        return self.__deep

    def setDeep(self, deep):
        self.__deep = deep

    def getDeepLimit(self):
        return self.__deepLimit

    def getSolutionPath(self):
        self.__solutionPath.append(self.__currentNode)
        while self.__currentNode.getFatherNode() != None:
            self.__currentNode = self.__currentNode.getFatherNode()
            self.__solutionPath.append(self.__currentNode)
        return self.__solutionPath

    def getVisiteds(self):
        return self.__visiteds

    def setVisiteds(self, node, operation):
        if operation == "+":
            self.__visiteds.append(node)
        elif operation == "-":
            self.__visiteds.remove(node)
        