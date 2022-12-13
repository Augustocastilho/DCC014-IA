from Search import Search


# Busca em largura
class BreadthFirst(Search):
    def __init__(self):
        super().__init__()
        self._queue = []
        self._visited = set()
    
    def search(self):
        self._queue.append(self._initalState)
        self._visited.add(self._initalState)

        while self._queue:
            currentNode = self._queue.pop(0)
            self.setCurrentNode(currentNode)
            if self.isGoal(currentNode):
                self._solution = currentNode
                self.setSuccess(True)
                return
            self.applyRules(currentNode)
            for child in currentNode.getChildren():
                if child not in self._visited:
                    self._queue.append(child)
                    self._visited.add(child)
        self.setFail(True)
        return

    def applyRules(self, node):
        node.setChildren(self.rule1(node))
        if node.getChildren()[-1] == None:
            node.getChildren().pop()
        else:
            node.getChildren()[-1].setFather(node)
        node.setChildren(self.rule2(node))
        if node.getChildren()[-1] == None:
            node.getChildren().pop()
        else:
            node.getChildren()[-1].setFather(node)
        node.setChildren(self.rule3(node))
        if node.getChildren()[-1] == None:
            node.getChildren().pop()
        else:
            node.getChildren()[-1].setFather(node)
        node.setChildren(self.rule4(node))
        if node.getChildren()[-1] == None:
            node.getChildren().pop()
        else:
            node.getChildren()[-1].setFather(node)
        node.setChildren(self.rule5(node))
        if node.getChildren()[-1] == None:
            node.getChildren().pop()
        else:
            node.getChildren()[-1].setFather(node)