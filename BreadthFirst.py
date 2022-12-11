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


    # def search(self):
    #     while self._success == False and self._fail == False:
    #         pass
    #     queue = [[self.start]]
    #     visited = set()
    #     while queue:
    #         path = queue.pop(0)
    #         node = path[-1]
    #         if node not in visited:
    #             neighbours = self.graph[node]
    #             for neighbour in neighbours:
    #                 new_path = list(path)
    #                 new_path.append(neighbour)
    #                 queue.append(new_path)
    #                 if neighbour == self.goal:
    #                     return new_path
    #             visited.add(node)
    #     return "No path found"

    # def __str__(self):
    #     return str(self.BreadthFirstSearch())