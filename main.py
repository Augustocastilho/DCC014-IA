from Tree import Tree
from Backtracking import Backtracking
from BreadthFirst import BreadthFirst
from DepthFirst import DepthFirst

if __name__ == '__main__':
    tree = Tree()

    tree.printRoot()

    # search = Backtracking()
    # search.search()

    search = BreadthFirst()
    search.search()