from Search import Search


class Backtracking(Search):

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
