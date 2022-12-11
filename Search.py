from abc import abstractmethod
from Node import Node
from Tree import Tree


class Search():
    _tree = Tree()
    _initalState = None
    _goalState = None
    _currentNode = None
    _fail = False
    _success = False
    _deep = 0
    _deepLimit = 0

    def __init__(self, deepLimit=0):
        self._initalState = self._tree.getRoot()
        self._goalState = [[], ['B', 'M', 'M', 'M', 'C', 'C', 'C']]
        self._currentNode = self._tree.getRoot()
        self._deepLimit = deepLimit

    def isGoal(self, node):
        node = node.getRightValor()
        if node.__len__() == self._goalState[1].__len__():
            return True
        else:
            return False

    # regra 1: mover 1 missionario
    def rule1(self, node):
        newNode = Node()
        newNode.setFather(node)
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

        newNode.setValors(left, right)
        if self.validate(newNode):
            print("Regra 1")
            newNode.printNode()
            return newNode
        return None
    
    # regra 2: mover 2 missionarios
    def rule2(self, node):
        newNode = Node()
        newNode.setFather(node)
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

        newNode.setValors(left, right)
        if self.validate(newNode):
            print("Regra 2")
            newNode.printNode()
            return newNode
        return None
    
    # regra 3: mover 1 canibal
    def rule3(self, node):
        newNode = Node()
        newNode.setFather(node)
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
        
        newNode.setValors(left, right)
        if self.validate(newNode):
            print("Regra 3")
            newNode.printNode()
            return newNode
        return None
    
    # regra 4: mover 2 canibais
    def rule4(self, node):
        newNode = Node()
        newNode.setFather(node)
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
        
        newNode.setValors(left, right)
        if self.validate(newNode):
            print("Regra 4")
            newNode.printNode()
            return newNode
        return None

    # regra 5: mover 1 missionario e 1 canibal
    def rule5(self, node):
        newNode = Node()
        newNode.setFather(node)
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
        
        newNode.setValors(left, right)
        if self.validate(newNode):
            print("Regra 5")
            newNode.printNode()
            return newNode
        return None

    
    def validate(self, node):
        left = node.getLeftValor().copy()
        right = node.getRightValor().copy()
        return self.verifyCannibals(left, right) and not self.verifyInPath(node)

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

    # verifica se o estado ja esta no caminho, True se estiver, False se não estiver
    def verifyInPath(self, node):
        left = node.getLeftValor()
        father = node.getFather()
        while father != None:
            if self.equals(left, father.getLeftValor()):
                return True
            father = father.getFather()
        return False

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

    @abstractmethod
    def search(self):
        pass

    # getters and setters
    def getTree(self):
        return self._tree

    def getInitalState(self):
        return self._initalState

    def getGoalState(self):
        return self._goalState

    def getCurrentNode(self):
        return self._currentNode

    def setCurrentNode(self, currentNode):
        self._currentNode = currentNode

    def getFail(self):
        return self._fail

    def setFail(self, fail):
        self._fail = fail

    def getSuccess(self):
        return self._success

    def setSuccess(self, success):
        self._success = success

    def getDeep(self):
        return self._deep

    def setDeep(self, deep):
        self._deep = deep

    def getDeepLimit(self):
        return self._deepLimit