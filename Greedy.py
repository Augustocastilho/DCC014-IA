from Search import Search


# Busca gulosa
class Greedy(Search):
    def __init__(self):
        super().__init__()
        self._queue = []
        self._visited = set()
    
    def search(self):
        self._queue.append(self._initalState)
        self._visited.add(self._initalState)

        while self._queue:
            print("Fila de abertos: ")
            for node in self._queue:
                print(node.getHeuristic(), end="  ")
            print("")
            currentNode = self._queue.pop(0)
            self.setCurrentNode(currentNode)
            self._visited.add(currentNode)
            if self.isGoal(currentNode):
                self._solution = currentNode
                self.setSuccess(True)
                print("\nCusto da solução: ", currentNode.getEdgeWeightInPath())
                return
            self.applyRulesToCurrentNode(currentNode)
            for child in currentNode.getChildren():
                if child not in self._visited:
                    self._queue.append(child)
            self._queue.sort(key=lambda x: x.getHeuristic())
            
        self.setFail(True)
        return