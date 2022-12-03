import os
import networkx as nx
import numpy as np
import matplotlib as plt

menu = {
    1: "Граф G1",
    2: "Граф G2",
    3: "Граф G3",
    4: "Задание 2",
    0: "Завершение работы",
}


def cls():
    os.system("clear")


def pause():
    os.system("pause")


def input_graph():
    global G1
    global adjacencyMatrixG1
    adjacencyMatrixG1 = np.array(
        [
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        ]
    )
    G1 = nx.from_numpy_matrix(adjacencyMatrixG1)

    global G2
    global adjacencyMatrixG2
    global incidenceMatrixG2
    incidenceMatrixG2 = np.array(
        [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 2],
        ]
    )
    adjacencyMatrixG2 = (np.dot(incidenceMatrixG2, incidenceMatrixG2.T) > 0).astype(int)
    np.fill_diagonal(adjacencyMatrixG2, 0)
    for i in range(len(incidenceMatrixG2)):
        for j in range(len(incidenceMatrixG2)):
            if incidenceMatrixG2[i][j] == 2:
                adjacencyMatrixG2[i][i] = 1
    G2 = nx.DiGraph(np.matrix(adjacencyMatrixG2))

    global G3
    global adjacencyMatrixG3
    global incidenceMatrixG3
    incidenceMatrixG3 = np.array(
        [
            [1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [-1, -1, -1, -2, -1, -1, -1],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
        ]
    )
    adjacencyMatrixG3 = (np.dot(incidenceMatrixG3, incidenceMatrixG3.T) != 0).astype(
        int
    )
    np.fill_diagonal(adjacencyMatrixG3, 0)
    for i in range(len(incidenceMatrixG3)):
        for j in range(len(incidenceMatrixG3)):
            if abs(incidenceMatrixG3[i][j]) == 2:
                adjacencyMatrixG3[i][i] = 1
    G3 = nx.from_numpy_matrix(adjacencyMatrixG3)


def graph1():
    print("Граф G1, заданный матрицей смежности")
    for i in adjacencyMatrixG1:
        print(" ".join(list(map(str, i))))
    print("Число ребер: ", nx.number_of_edges(G1))
    print("Число вершин: ", nx.number_of_nodes(G1))

    al = {}
    for x, row in enumerate(adjacencyMatrixG1):
        al[x + 1] = []
        for i, v in enumerate(row):
            if v == 1 and i != x:
                al[x + 1].append(i + 1)
    print("Список смежности")
    print(al)
    incidenceMatrix = nx.incidence_matrix(G1)
    print("Мартрица инцидентности G1:")
    print(incidenceMatrix.todense())
    nx.draw(G1, with_labels=True)
    plt.savefig("graph1.png")
    plt.show()
    plt.close()
    return_menu()


def graph2():

    print("Мартрица инцидентности G2:")
    for i in incidenceMatrixG2:
        print(" ".join(list(map(str, i))))
    print("Граф G2, заданный матрицей смежности")
    for i in adjacencyMatrixG2:
        print(" ".join(list(map(str, i))))
    print("Число ребер: ", nx.number_of_edges(G2))
    print("Число вершин: ", nx.number_of_nodes(G2))

    adjacencyList = {}
    for x, row in enumerate(adjacencyMatrixG2):
        adjacencyList[x + 1] = []
        for i, v in enumerate(row):
            if v == 1 and i != x:
                adjacencyList[x + 1].append(i + 1)
    print("Список смежности")
    print(adjacencyList)
    nx.draw(G2, with_labels=True)
    plt.savefig("graph2.png")
    plt.show()
    plt.close()

    return_menu()


def graph3():
    print("Мартрица инцидентности G3:")
    for i in incidenceMatrixG3:
        print(" ".join(list(map(str, i))))
    print("Граф G3, заданный матрицей смежности")
    for i in adjacencyMatrixG3:
        print(" ".join(list(map(str, i))))
    G3 = nx.from_numpy_matrix(adjacencyMatrixG3)
    print("Число ребер: ", nx.number_of_edges(G3))
    print("Число вершин: ", nx.number_of_nodes(G3))

    adjacencyList = {}
    for x, row in enumerate(adjacencyMatrixG3):
        adjacencyList[x + 1] = []
        for i, v in enumerate(row):
            if v == 1 and i != x:
                adjacencyList[x + 1].append(i + 1)
    print("Список смежности")
    print(adjacencyList)
    nx.draw(G3, with_labels=True)
    plt.savefig("graph3.png")
    plt.show()
    plt.close()

    return_menu()


def ex2():
    global G4
    print("A)")
    G1.add_nodes_from([10, 11])
    G1.remove_node(1)
    nx.draw(G1, with_labels=True)
    plt.show()
    print("B)")
    G1.add_edges_from([(4, 10), (8, 9), (2, 11), (9, 11), (10, 11)])
    G1.remove_edges_from([(2, 6), (2, 8)])
    nx.draw(G1, with_labels=True)
    plt.show()
    print("C)")
    incidenceMatrix = nx.incidence_matrix(G1)
    print(incidenceMatrix.todense())
    G4 = nx.complement(G1)
    adjacencyMatrix = nx.adjacency_matrix(G4)
    print(adjacencyMatrix.todense())
    G5 = G3.copy()
    G3.add_nodes_from([7, 8, 9])
    G3.remove_node(5)
    G3.add_edges_from([(7, 0), (8, 0), (9, 1)])
    G3.remove_edge(3, 3)
    G5.add_edges_from([(7, 0), (8, 0), (9, 1)])
    G5.remove_edge(3, 3)
    G5.add_nodes_from([7, 8, 9])
    G5.remove_node(5)
    print("D)")
    print(nx.adjacency_matrix(G3).todense())
    print("E")
    print(nx.adjacency_matrix(G5).todense())
    return_menu()


def dfs():
    cls()


def return_menu():
    pause()
    cls()
    menu_()


def menu_():
    print("----------MЕНЮ----------")
    for key, value in menu.items():
        print(key, " - ", value)
    cmd = int(input(">"))
    if cmd == 1:
        graph1()
    elif cmd == 2:
        graph2()
    elif cmd == 3:
        graph3()
    elif cmd == 4:
        ex2()
    elif cmd == 0:
        print("Выход из программы")
        exit()
    else:
        print("Неправильно введена команда")
        cls()
        menu_()


input_graph()
menu_()
