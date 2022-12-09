from Search import Search

class Backtracking(Search):
    backs = 0
    
    def search(self):    
        self._solution = self._recursiveBacktracking(self._initalState)
        return self._solution

    def _recursiveBacktracking(self, currentNode):
        currentNode.setRuleNumber(currentNode.getRuleNumber() + 1)
        rule = None
        if not self.getSuccess() and not self.getFail():
            if self.getDeepLimit() != 0 and self.getDeep() > self.getDeepLimit():
                self.backs = self.backs + 1
                # self._recursiveBacktracking(currentNode.getFatherNode())
                return None
            match currentNode.getRuleNumber():
                case 1:
                    rule = self.rule1(currentNode)
                    if rule != None:
                        self._recursiveBacktracking(rule)
                    else:
                        self._recursiveBacktracking(currentNode)
                case 2:
                    rule = self.rule2(currentNode)
                    if rule != None:
                        self._recursiveBacktracking(rule)
                    else:
                        self._recursiveBacktracking(currentNode)
                case 3:
                    rule = self.rule3(currentNode)
                    if rule != None:
                        self._recursiveBacktracking(rule)
                    else:
                        self._recursiveBacktracking(currentNode)
                case 4:
                    rule = self.rule4(currentNode)
                    if rule != None:
                        self._recursiveBacktracking(rule)
                    else:
                        self._recursiveBacktracking(currentNode)
                case 5:
                    rule = self.rule5(currentNode)
                    if rule != None:
                        self._recursiveBacktracking(rule)
                    else:
                        self._recursiveBacktracking(currentNode)
                case default:
                    self.backs = self.backs + 1
                    # self._recursiveBacktracking(self.getCurrentNode().getFatherNode(), ruleNumber)
                    return None

            # self.rules(state, ruleNumber)
            # rule = self.getCurrentNode().getRules()
            # if rule != None:
            #     self._recursiveBacktracking(rule, ruleNumber)
            # else:
            #     self.setFail(True)
            #     return None
            if currentNode.getRuleNumber() > 5 and currentNode.equals(self._initalState):
                self.setFail(True)
                return None
        if self.isGoal(currentNode):
            self.setSuccess(True)
            return currentNode
        return None

    def rules(self, node, ruleNumber):
        match ruleNumber:
            case 1:
                rule = self.rule1(node)
                if rule != None:
                    self.getCurrentNode().setRules(rule)
                else:
                    return None
            case 2:
                rule = self.rule2(node)
                self.auxRule(rule)
            case 3:
                rule = self.rule3(node)
                self.auxRule(rule)
            case 4:
                rule = self.rule4(node)
                self.auxRule(rule)
            case 5:
                rule = self.rule5(node)
                self.auxRule(rule)
            case default:
                return None

    def auxRule(self, rule):
        if rule != None:
            self.getCurrentNode().setRules(rule)
    
# if not self.getSuccess() and not self.getFail():
        #     self.setVisiteds(state, "+")
        #     if self.isGoal(state):
        #         self.setSuccess(True)
        #         return self.solution(state)
        #     for action in self.rules(state):
        #         child = self.result(state, action)
        #         if child not in self.getVisiteds():
        #             solution = self._recursiveBacktracking(child)
        #             if solution != None:
        #                 return solution
        #     self.setFail(True)
        #     return None
        # if self._problem.isGoal(state):
        #     return self._problem.solution(state)
        # for action in self._problem.rules(state):
        #     child = self._problem.result(state, action)
        #     if self._recursiveBacktracking(child):
        #         return self._problem.solution(child)
        # return None

    # def solution(self):
    #     return self._solution

    
    # def search(self):
    #     while not self.getSuccess() and not self.getFail():
    #         # se o limite de profundidade for atingido, volta para o pai
    #         if self.getDeepLimit() != 0 and self.getDeep() >= self.getDeepLimit():
    #             self.back()

    #         self.rules(self.getCurrentNode())
    #         rule = self.getCurrentNode().getRules()
    #         if rule != None:
    #             self.expand(rule)
    #             print(self.getVisiteds())
    #             # verifica se o estado atual é o estado objetivo
    #             if self.isGoal(self.getCurrentNode()):
    #                 self.setSuccess(True)
    #                 print("Sucesso")
    #         else:
    #             # se nao houver regra a ser aplicada, volta para o pai
    #             if self.equals(self.getCurrentNode().getLeftValor(), self.getInitalState().getLeftValor()):
    #                 self.setFail(True)
    #                 print("Falha")
    #             else:
    #                 self.back()
    #         self.getCurrentNode().printNode()

    # # volta para o pai
    # def back(self):
    #     self.setCurrentNode(self.getCurrentNode().getFatherNode())
    #     # self.setVisiteds(self.getCurrentNode(), "-")
    #     self.setDeep(self.getDeep()-1)

    # # avança para o primeiro filho da lista 
    # def expand(self, node):
    #     i=0
    #     j=0
    #     # verifica se o filho já foi visitado
    #     while i < len(node):
    #         for n in self.getVisiteds():
    #             if not self.equals(n.getLeftValor(), node[i].getLeftValor()):
    #                 j = i
    #                 i = len(node)
    #                 break
    #         i = i+1
        
    #     currentNode = self.getCurrentNode()
    #     currentNode.setChildrenNode(node[j])
        
    #     i=0
    #     j=0
    #     while i<len(currentNode.getChildrenNodes()):
    #         for n in self.getVisiteds():
    #             if not self.equals(n.getLeftValor(), currentNode.getChildrenNodes()[j].getLeftValor()):
    #                 j = i
    #                 i = len(currentNode.getChildrenNodes())
    #                 break
    #         i = i+1
        
    #     child = currentNode.getChildrenNodes()[j]
    #     self.setCurrentNode(child)
    #     currentNode = self.getCurrentNode()
    #     self.setVisiteds(currentNode, "+")
    #     self.setDeep(self.getDeep()+1)