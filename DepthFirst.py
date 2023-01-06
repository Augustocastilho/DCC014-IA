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
            self._visited.add(currentNode)
            if self.isGoal(currentNode):
                self._solution = currentNode
                self.setSuccess(True)
                return
            self.applyRulesToCurrentNode(currentNode)
            for child in currentNode.getChildren():
                if child not in self._visited:
                    self._heap.append(child)
        self.setFail(True)
        return
