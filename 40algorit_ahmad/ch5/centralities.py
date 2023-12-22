'''
Example of centrality calculations in python
Author: Nat Hawkins
Date (YYYY-MM-DD): 2023-12-22
'''

# Imports ----------------------------------------------------------------------
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Functions --------------------------------------------------------------------
def createNetwork():
    vertices = range(1,10)
    edges    = [
                (7,2), 
                (2,3), 
                (7,4), 
                (4,5), 
                (7,3), 
                (7,5), 
                (1,6), 
                (1,7), 
                (2,8), 
                (2,9)
               ]

    G = nx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(edges)

    return G

def plotNetwork(G):
    nx.draw(G, with_labels = True, node_color = 'y', node_size = 800)
    plt.show()

def calculateDegreeCentrality(G: nx.Graph):
    denominator = len(G.nodes) - 1
    degrees     = [nx.degree(G, n_) for n_ in G.nodes]
    return {i: degree/denominator for i, degree in enumerate(degrees)}

def calculateBetweennessCentrality(G: nx.Graph):
    centrality = {}
    for v in G.nodes:
        sigma_st_v = 0
        sigma_st   = 0
        paths = []
        for s in G.nodes:
            for t in G.nodes:
                if s == v or t == v or s == t: continue
                path = nx.shortest_path(G, s, t)
                if path not in paths:
                    if path[::-1] not in paths:
                        sigma_st += 1

                        if v in path:
                            sigma_st_v += 1
        centrality[v] = sigma_st_v/sigma_st
    return centrality

def calculateClosenessCentrality(G):
    centrality = {}
    for x in G.nodes:
        d_y = 0
        for y in G.nodes:
            if x == y: continue
            d_y += nx.shortest_path_length(G, x, y)
        centrality[x] = (len(G.nodes) - 1)/d_y
    return centrality

def calculateEigenvectorCentrality(G):
    A = nx.to_numpy_array(G)
    eigvals, eigvecs = np.linalg.eig(A)
    
    largest_eigval = eigvals == eigvals.max()
    largest_eigvec = eigvecs[:, largest_eigval]

    return {i+1: round(abs(val[0]), 3) for i, val in enumerate(largest_eigvec)}

# Main -------------------------------------------------------------------------
def main():
    G = createNetwork()
    print(calculateDegreeCentrality(G)) # Check
    print(calculateBetweennessCentrality(G)) # Check
    print(calculateClosenessCentrality(G)) # Check
    print(calculateEigenvectorCentrality(G)) # Check
    return 0

if __name__ == '__main__':
    main()