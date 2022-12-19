import networkx as nx
import numpy as np
import pylab as plt

Graph = np.array([[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                  [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                  [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
                  [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
                  [1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
                  [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
                  [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
                  [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
                  [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0]])

Graph = nx.from_numpy_matrix(Graph)


def dfs(graph, start, visited=[], prev=None):
    if start not in visited:
        visited.append(start)
        if prev is not None:
            dict_of_skeleton_gpaph[prev].append(start)
            dict_of_skeleton_gpaph[start].append(prev)
        for neighbour in graph[start]:
            dfs(graph, neighbour, visited, start)
    return visited


global dict_of_skeleton_gpaph
dict_of_gpaph = nx.to_dict_of_lists(Graph)
dict_of_skeleton_gpaph = dict_of_gpaph.copy()
for key in dict_of_skeleton_gpaph.keys():
    dict_of_skeleton_gpaph[key] = []
print(dict_of_gpaph)
print(dfs(dict_of_gpaph, 5))
print(dict_of_skeleton_gpaph)
skeleton_graph = nx.from_dict_of_lists(dict_of_skeleton_gpaph)
nx.draw(Graph, with_labels=True)
plt.show()
nx.draw(skeleton_graph, with_labels=True)
plt.show()
