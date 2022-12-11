from Search import Search


class Backtracking(Search):
    backs = 0

    def search(self):
        self._solution = self._recursiveBacktracking(self._initalState)
        print("Backs: ", self.backs)
        return self._solution

    def _recursiveBacktracking(self, currentNode):
        if currentNode is None:
            return None
        if self.isGoal(currentNode):
            self.setSuccess(True)
            return currentNode
        if not self.getSuccess() and not self.getFail():
            if self.getDeepLimit() != 0 and self.getDeep() > self.getDeepLimit():
                self.backs = self.backs + 1
                return None
            if self.getSuccess():
                return currentNode
            self._recursiveBacktracking(self.rule1(currentNode))
            if self.getSuccess():
                return currentNode
            self._recursiveBacktracking(self.rule2(currentNode))
            if self.getSuccess():
                return currentNode
            self._recursiveBacktracking(self.rule3(currentNode))
            if self.getSuccess():
                return currentNode
            self._recursiveBacktracking(self.rule4(currentNode))
            if self.getSuccess():
                return currentNode
            self._recursiveBacktracking(self.rule5(currentNode))
            if self.getSuccess():
                return currentNode
            if self.equals(self._initalState.getLeftValor(), currentNode.getLeftValor()):
                self.setFail(True)
                return None
            else:
                if self.getSuccess():
                    return currentNode
                print("back")
                self.backs = self.backs + 1
                return None
        return None
