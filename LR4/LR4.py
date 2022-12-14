<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
import os
import networkx as nx
import warnings

def convert_adjacency_list_to_adjacency_matrix(adjacency_list: np.ndarray):
    count_of_vertices = len(adjacency_list)
    adjacency_matrix = np.array([[0] * count_of_vertices for i in range(count_of_vertices)])
    for i in range(count_of_vertices):
        if len(adjacency_list[i] > 1):
            for j in range(1, len(adjacency_list[i])):
                adjacency_matrix[i, adjacency_list[i]] = 1
    return adjacency_matrix


def convert_incidence_matrix_to_adjacency_matrix(incidence_matrix: np.ndarray):
    col = len(incidence_matrix[0])
    row = len(incidence_matrix)
    adjacency_matrix = np.array([[0] * row for j in range(row)])
    for j in range(col):
        values = [incidence_matrix[i, j] for i in range(row) if abs(incidence_matrix[i, j]) == 1]
        vertices = [i for i in range(row) if abs(incidence_matrix[i, j]) == 1]
        if values == [-1, 1]:
            values = values[::-1]
            vertices = vertices[::-1]
        adjacency_matrix[vertices[0], vertices[1]] = 1
        adjacency_matrix[vertices[1], vertices[0]] = 1 if values == [1, 1] else 0
    return adjacency_matrix


def print_information(g: nx.DiGraph, oriented_for_incidence_matrix=False):
    print('Вершины: ', nx.nodes(g), ' количество: ', g.number_of_nodes())
    print('Ребра: ', nx.edges(g), ' количество: ', g.number_of_edges())
    print('Список смежности: ', [[i, *[j[1] for j in nx.edges(g) if i == j[0]]] for i in nx.nodes(g)])
    print('Степени вершин графа:')
    for i in nx.nodes(g):
        deg_out = len([j for j in nx.edges(g) if j[0] == i])
        deg_in = len([j for j in nx.edges(g) if j[1] == i])
        print(f'deg+(v{i}) = {deg_out}, deg-(v{i}) = {deg_in}' if deg_out != deg_in else f'deg(v{i}) = {deg_out}')
    am = np.array(nx.adjacency_matrix(g).todense())
    for vb, ve in nx.edges(g):
        if vb == ve:
            am[vb, ve] = 2
    print('Матрица смежности:\n', am)
    im = nx.incidence_matrix(g, oriented=oriented_for_incidence_matrix).todense().astype('int')
    print('Матрица инцидентности:\n', im * -1 if oriented_for_incidence_matrix else im)


def enter_adjacency_matrix_of_graph():
    num = int(input('Введите количество вершин: '))
    print('Введите матрицу смежности:')
    return nx.DiGraph(np.array([[int(j) for j in input().split()] for i in range(num)]))


def enter_incidence_matrix_of_graph():
    num = int(input('Введите количество вершин: '))
    print('Введите матрицу инцидентности:')
    return nx.DiGraph(
        convert_incidence_matrix_to_adjacency_matrix(np.array([[int(j) for j in input().split()] for i in range(num)])))


def enter_adjacency_list_of_graph():
    num = int(input('Введите количество вершин: '))
    print('Введите список смежности:')
    return nx.DiGraph(
        convert_adjacency_list_to_adjacency_matrix(np.array([[int(j) for j in input().split()] for i in range(num)])))

def personal_task():
    A1 = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
                   [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                   [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 2, 0, 1, 0],
                   [0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                   [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]])

    I2 = np.array([[1, 1, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0, 0],
                   [0, 1, 0, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 1],
                   [0, 0, 0, 1, 1, 1]])

    I3 = np.array([[1, 0, 0, 0, -1],
                   [0, 1, 0, 0, 0],
                   [0, 0, 1, -1, 0],
                   [0, -1, 0, 0, 0],
                   [0, 0, -1, 0, 0],
                   [0, 0, 0, 1, 1],
                   [-1, 0, 0, 0, 0]])

    A2 = convert_incidence_matrix_to_adjacency_matrix(I2)
    A3 = convert_incidence_matrix_to_adjacency_matrix(I3)

    v = [11, 12, 4, 8, 9, 10, 2]
    e = [(7, 11), (9, 10), (4, 12), (1, 12), (11, 12), (7, 7), (3, 3)]
    f = [(1, 4), (3, 4), (3, 5), (1, 7)]


    G1 = nx.DiGraph(A1)
    print_information(G1)
    nx.draw(G1, pos=nx.circular_layout(G1), with_labels=True, node_color='r')
    plt.show()

    G2 = nx.DiGraph(A2)
    print_information(G2)
    nx.draw(G2, pos=nx.circular_layout(G2), with_labels=True, node_color='g')
    plt.show()

    G3 = nx.DiGraph(A3)
    print_information(G3, oriented_for_incidence_matrix=True)
    nx.draw(G3, pos=nx.circular_layout(G3), with_labels=True, node_color='b')
    plt.show()


    G1.add_node(v[0])
    G1.add_node(v[1])
    G1.remove_node(v[2])
    print_information(G1)
    nx.draw(G1, pos=nx.circular_layout(G1), with_labels=True, node_color='r')
    plt.show()


    for i in range(5):
        G1.add_edge(*e[i])
        G1.add_edge(*e[i][::-1])


    print_information(G1)
    nx.draw(G1, pos=nx.circular_layout(G1), with_labels=True, node_color='r')
    plt.show()


    G4 = nx.complement(G1)
    print_information(G4)
    nx.draw(G4, pos=nx.circular_layout(G4), with_labels=True, node_color='r')
    plt.show()


    G31 = G3
    for i in range(3, 6):
        G31.add_node(i)
    G31.remove_node(v[6])

    for i in range(3):
        G31.add_edge(*f[i])

    print_information(G31, oriented_for_incidence_matrix=True)
    nx.draw(G31, pos=nx.circular_layout(G31), with_labels=True, node_color='b')
    plt.show()


    G32 = G3
    for i in range(3):
        G32.add_edge(*f[i])

    for i in range(3, 6):
        G32.add_node(i)

    print_information(G32, oriented_for_incidence_matrix=True)
    nx.draw(G32, pos=nx.circular_layout(G32), with_labels=True, node_color='b')
    plt.show()

    intersection_of_graphs = nx.intersection(G1, G2)
    result_of_logical_expression = nx.compose(intersection_of_graphs, G4)
    print_information(result_of_logical_expression)
    nx.draw(result_of_logical_expression, pos=nx.circular_layout(result_of_logical_expression), with_labels=True,
            node_color='b')
    plt.show()

warnings.filterwarnings('ignore')
menu = ' 1. Задать первый граф в виде списка смежности\n' \
       ' 2. Задать первый граф в виде матрицы смежности\n' \
       ' 3. Задать первый граф в виде матрицы инцидентности\n' \
       ' 4. Задать второй граф в виде списка смежности\n' \
       ' 5. Задать второй граф в виде матрицы смежности\n' \
       ' 6. Задать второй граф в виде матрицы инцидентности\n' \
       ' 7. Объединение графов\n' \
       ' 8. Пересечение графов\n' \
       ' 9. Кольцевая сумма графов\n' \
       '10. Вывести информацию о первом графе\n' \
       '11. Вывести информацию о втором графе\n' \
       '12. Вывести первый граф\n' \
       '13. Вывести второй граф\n' \
       '14. Задание по варианту\n' \
       ' 0. Выход'
exit_menu = False
entered_first_graph, entered_second_graph = False, False
first_graph, second_graph = nx.DiGraph(), nx.DiGraph()
while not exit_menu:
    print(menu)
    command = int(input('Введите команду=> '))
    if command == 1:
        first_graph = enter_adjacency_list_of_graph()
        entered_first_graph = True
    elif command == 2:
        first_graph = enter_adjacency_matrix_of_graph()
        entered_first_graph = True
    elif command == 3:
        first_graph = enter_incidence_matrix_of_graph()
        entered_first_graph = True
    elif command == 4:
        second_graph = enter_adjacency_list_of_graph()
        entered_second_graph = True
    elif command == 5:
        second_graph = enter_adjacency_matrix_of_graph()
        entered_second_graph = True
    elif command == 6:
        second_graph = enter_incidence_matrix_of_graph()
        entered_second_graph = True
    elif command == 7:
        if not entered_first_graph:
            print('Вы не ввели первый граф')
        if not entered_second_graph:
            print('Вы не ввели второй граф')
        if entered_first_graph and entered_second_graph:
            RES = nx.compose(first_graph, second_graph)
            print_information(RES)
            nx.draw(RES, pos=nx.circular_layout(RES), with_labels=True, node_color='b')
            plt.show()
    elif command == 8:
        if not entered_first_graph:
            print('Вы не ввели первый граф')
        if not entered_second_graph:
            print('Вы не ввели второй граф')
        if entered_first_graph and entered_second_graph:
            RES = nx.intersection(first_graph, second_graph)
            print_information(RES)
            nx.draw(RES, pos=nx.circular_layout(RES), with_labels=True, node_color='b')
            plt.show()
    elif command == 9:
        if not entered_first_graph:
            print('Вы не ввели первый граф')
        if not entered_second_graph:
            print('Вы не ввели второй граф')
        if entered_first_graph and entered_second_graph:
            RES = nx.compose(nx.difference(first_graph, second_graph), nx.difference(second_graph, first_graph))
            print_information(RES)
            nx.draw(RES, pos=nx.circular_layout(RES), with_labels=True, node_color='b')
            plt.show()
    elif command == 10:
        if entered_first_graph:
            print_information(first_graph)
        else:
            print('Вы не ввели первый граф')
    elif command == 11:
        if entered_second_graph:
            print_information(second_graph)
        else:
            print('Вы не ввели второй граф')
    elif command == 12:
        if entered_first_graph:
            nx.draw(first_graph, pos=nx.circular_layout(first_graph), with_labels=True, node_color='b')
            plt.show()
        else:
            print('Вы не ввели первый граф')
    elif command == 13:
        if entered_second_graph:
            nx.draw(second_graph, pos=nx.circular_layout(second_graph), with_labels=True, node_color='b')
            plt.show()
        else:
            print('Вы не ввели второй граф')
    elif command == 14:
        personal_task()
    elif command == 0:
        exit_menu = True
    else:
        print('Неизвестная команда!')
os.system('clear')
=======
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
>>>>>>> origin/master
