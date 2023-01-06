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
            self._visited.add(currentNode)
            if self.isGoal(currentNode):
                self._solution = currentNode
                self.setSuccess(True)
                return
            self.applyRulesToCurrentNode(currentNode)
            for child in currentNode.getChildren():
                if child not in self._visited:
                    self._queue.append(child)
        self.setFail(True)
        return
