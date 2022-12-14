from Tree import Tree
from Backtracking import Backtracking
from BreadthFirst import BreadthFirst
from DepthFirst import DepthFirst
from BestFirst import BestFirst
from Greedy import Greedy
from AStar import AStar


def menu():
    print("Selecione o Algorigmo de Busca: ")
    print("1 - Backtracking")
    print("2 - Busca em Largura")
    print("3 - Busca em Profundidade")
    print("4 - Busca Ordenada")
    print("5 - Busca Gulosa")
    print("6 - Busca A*")
    print("7 - Sair")
    option = int(input("Opcao: "))
    print("")
    return option
 

if __name__ == '__main__':
    print("--------------------------------Problema dos Missionarios e Canibais--------------------------------")
    option = menu()
    
    while True:
        tree = Tree()
        match option:
            case 1:
                search = Backtracking()
            case 2:
                search = BreadthFirst()
            case 3:
                search = DepthFirst()
            case 4:
                search = BestFirst()
            case 5:
                search = Greedy()
            case 6:
                search = AStar()
            case 7:
                print("Saindo...")
                exit()
            case default:
                print("Opção Inválida")
                exit()
    
        tree.printRoot()
        search.search()
        print("\nÁrvore gerada:")
        tree.printTree()
        print("\nCaminho Solução: ")
        search.printSolution(search.getSolution())
        print("----------------------------------------------------------------------------------------------------\n")
        option = menu()
