from Search import Search


class Backtracking(Search):

    def search(self):
        while not self.getSuccess() and not self.getFail():
            # se o limite de profundidade for atingido, volta para o pai
            if self.getDeepLimit() != 0 and self.getDeep() >= self.getDeepLimit():
                self.back()

            self.rules(self.getCurrentNode())
            rule = self.getCurrentNode().getRules()
            if rule != None:
                self.expand(rule)
                print(self.getVisiteds())
                # verifica se o estado atual é o estado objetivo
                if self.isGoal(self.getCurrentNode()):
                    self.setSuccess(True)
                    print("Sucesso")
            else:
                # se nao houver regra a ser aplicada, volta para o pai
                if self.equals(self.getCurrentNode().getLeftValor(), self.getInitalState().getLeftValor()):
                    self.setFail(True)
                    print("Falha")
                else:
                    self.back()
            self.getCurrentNode().printNode()

    # volta para o pai
    def back(self):
        self.setCurrentNode(self.getCurrentNode().getFatherNode())
        # self.setVisiteds(self.getCurrentNode(), "-")
        self.setDeep(self.getDeep()-1)

    # avança para o primeiro filho da lista 
    def expand(self, node):
        i=0
        j=0
        # verifica se o filho já foi visitado
        while i < len(node):
            for n in self.getVisiteds():
                if not self.equals(n.getLeftValor(), node[i].getLeftValor()):
                    j = i
                    i = len(node)
                    break
            i = i+1
        
        currentNode = self.getCurrentNode()
        currentNode.setChildrenNode(node[j])
        
        i=0
        j=0
        while i<len(currentNode.getChildrenNodes()):
            for n in self.getVisiteds():
                if not self.equals(n.getLeftValor(), currentNode.getChildrenNodes()[j].getLeftValor()):
                    j = i
                    i = len(currentNode.getChildrenNodes())
                    break
            i = i+1
        
        child = currentNode.getChildrenNodes()[j]
        self.setCurrentNode(child)
        currentNode = self.getCurrentNode()
        self.setVisiteds(currentNode, "+")
        self.setDeep(self.getDeep()+1)

    def rules(self, node):
        rule = self.rule1(node)
        self.auxRole(rule)
        rule = self.rule2(node)
        self.auxRole(rule)
        rule = self.rule3(node)
        self.auxRole(rule)
        rule = self.rule4(node)
        self.auxRole(rule)
        rule = self.rule5(node)
        self.auxRole(rule)

        return None

    def auxRole(self, rule):
        if rule != None:
            for n in self.getVisiteds():
                if not self.equals(n.getLeftValor(), rule.getLeftValor()):
                    self.getCurrentNode().setRules(rule)
    