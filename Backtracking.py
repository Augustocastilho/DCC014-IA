from Search import Search


class Backtracking(Search):
    backs = 0

    def search(self):
        self._recursiveBacktracking(self._initalState)
        print("\nBacks:", self.backs)
        return

    def _recursiveBacktracking(self, currentNode):
        if currentNode is None:
            return
        if self.isGoal(currentNode):
            self._solution = currentNode
            self.setSuccess(True)
            return
        if not self.getSuccess() and not self.getFail():
            if self.getDeepLimit() != 0 and self.getDeep() > self.getDeepLimit():
                self.backs = self.backs + 1
                return
            if self.getSuccess():
                return
            self._recursiveBacktracking(self.rule1(currentNode))
            if self.getSuccess():
                return
            self._recursiveBacktracking(self.rule2(currentNode))
            if self.getSuccess():
                return
            self._recursiveBacktracking(self.rule3(currentNode))
            if self.getSuccess():
                return
            self._recursiveBacktracking(self.rule4(currentNode))
            if self.getSuccess():
                return
            self._recursiveBacktracking(self.rule5(currentNode))
            if self.getSuccess():
                return
            if self.equals(self._initalState.getLeftValor(), currentNode.getLeftValor()):
                self.setFail(True)
                return
            else:
                if self.getSuccess():
                    return
                print("back")
                self.backs = self.backs + 1
                return
        return
