"""
The PageRank algorithm to prioritize search results given some kind of
network structure.
"""

# Imports ---------------------------------------------------------------------
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Functions -------------------------------------------------------------------
def createNetwork():
    # Define the network as a directed graph to track connections between pages
    # (synonymous with hyperlinks within pages)
    web = nx.DiGraph()

    # Define the number of pages as nodes in the graph
    pages = range(1, 5)

    # Define the connections between pages
    connections = [(1,3),(2,1),(2,3),(3,1),(3,2),(3,4),(4,5),(5,1),(5,4)]

    # Populate web with pages and connections
    web.add_nodes_from(pages)
    web.add_edges_from(connections)

    return web

def pageRank(G):
    # Get number of nodes from graph
    N = len(G)

    # Define matrix that will be probability matrix
    M = nx.to_numpy_array(G)

    # Define number of outbound connections
    outward_connections = np.sum(M, axis = 1)

    # Define outbound probability matrix
    # (correcting divide by zero issues)
    outward_probabilities = np.array([1.0/count if count > 0 else 0 for count in outward_connections])

    # Multiply binary network matrix by outward probabilities
    transition_matrix = M.T * outward_probabilities

    # Define node weights
    node_weights = 1/N * np.ones(N)

    return transition_matrix, node_weights

# Main ------------------------------------------------------------------------
def main():
    # Initialize network
    web = createNetwork()

    # Plot web
    # pos = nx.shell_layout(web)
    # nx.draw(web, pos, arrows = True, with_labels = True)
    # plt.show()

    # Execute page rank algorithm
    print(pageRank(web))

if __name__ == "__main__":
    main()