'''
Implementation of BFS and DFS on a simple network
Author: Nat Hawkins
Date (YYYY-MM-DD): 2023-12-22
'''

# Imports ----------------------------------------------------------------------
import networkx as nx
from argparse import ArgumentParser

# Functions --------------------------------------------------------------------
def constructCommandLineArguments():
    parser = ArgumentParser()
    parser.add_argument("-m", "--method", 
                        help = "Breadth-first search (bfs) or depth-first search (dfs).",
                        default = 'bfs')
    return parser

def initializeNetwork():
    graph={'Amin' : ['Wasim', 'Nick', 'Mike'],
           'Wasim' : ['Imran', 'Amin'],
           'Imran' : ['Wasim','Faras'],
           'Faras' : ['Imran'],
           'Mike' : ['Amin'],
           'Nick' : ['Amin']}
    return nx.from_dict_of_lists(graph)

def breadthFirstSearch(G: nx.Graph, start):
    # Define two data structures
    # 1. The nodes we have visited (which will start out as empty)
    # 2. A queue (implemented as a list) of nodes to visit
    visited_nodes = []
    nodes_queue   = [start]

    # Continue until no more nodes to visit
    while len(nodes_queue) > 0:
        # Remove node from queue
        current_node = nodes_queue.pop(0)

        # Make sure node has not been visited yet
        if current_node not in visited_nodes:
            # We visit the node
            visited_nodes.append(current_node)

            # Get nodes connected to current node
            for neighbor in G[current_node]:
                nodes_queue.append(neighbor) # FIFO - new nodes added to the end of the queue

    # Return nodes in order visited
    return visited_nodes

def depthFirstSearch(G: nx.Graph, start, visited = None):
    # Initialize visited nodes on the first iteration
    if visited is None:
        visited = []
    # Add the current node to the list of nodes visited
    visited.append(start)
    # Get neighborhood associated with node
    for next_node in [node for node in G[start] if node not in visited]:
        # At each node, recursively call the DFS function to traverse down the tree
        depthFirstSearch(G, next_node, visited)
    return visited

# Main -------------------------------------------------------------------------
def main():
    parser = constructCommandLineArguments()
    args   = parser.parse_args()

    G = initializeNetwork()

    if args.method == 'bfs':
        print(breadthFirstSearch(G, 'Amin'))

    if args.method == 'dfs':
        print(depthFirstSearch(G, 'Amin'))

if __name__ == '__main__':
    main()