from Search import Search

# Busca em profundidade
class DepthFirst(Search):
    def __init__(self):
        super().__init__()
        self._heap = []
        self._visited = set()
    
    def search(self):
        self._heap.append(self._initalState)
        self._visited.add(self._initalState)

        while self._heap:
            currentNode = self._heap.pop(-1)
            self.setCurrentNode(currentNode)
            if self.isGoal(currentNode):
                self.setSuccess(True)
                return
            self.applyRules(currentNode)
            for child in currentNode.getChildren():
                if child not in self._visited:
                    self._heap.append(child)
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