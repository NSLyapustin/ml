import networkx as nx
import random
import matplotlib as plt

import numpy as np


def calc_dist_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j] = matrix[j][i] = random.uniform(10,99)
    return np.asmatrix(np.array(matrix))


if __name__ == '__main__':
    n = 10
    matrix = calc_dist_matrix(n)

    # print(matrix)
    G = nx.from_numpy_matrix(matrix)
    plt
    print(G)