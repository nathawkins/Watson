'''
Determining fraud risk using the guilt-by-association principle
applied to homophilic networks.

Author: Nat Hawkins
Date (YYYY-MM-DD): 2023-12-22
'''

# Imports ----------------------------------------------------------------------
import networkx as nx
import matplotlib.pyplot as plt

# Functions --------------------------------------------------------------------
def constructNetwork():
    vertices = range(1,10)
    edges= [(7,2), (2,3), (7,4), (4,5), (7,3), (7,5), (1,6), (1,7), (2,8), (2,9)]

    G = nx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(edges)

    return G

def plotNetwork(G, f_nodes, nf_nodes):
    pos = nx.spring_layout(G)
    labels = {}
    for node in f_nodes:
        labels[node] = f"{node} F"

    for node in nf_nodes:
        labels[node] = f"{node} NF"

    nx.draw_networkx_nodes(G,
                           pos,
                           nodelist = f_nodes,
                           node_color = 'r',
                           node_size = 1300)
    nx.draw_networkx_nodes(G,
                           pos,
                           nodelist = nf_nodes,
                           node_color = 'g',
                           node_size = 1300)
    nx.draw_networkx_labels(G,
                            pos,
                            labels,
                            font_size=16)
    nx.draw_networkx_edges(G,
                           pos,
                           width=3,
                           alpha=0.5,
                           edge_color='b')
    
    plt.show()

def calculateNaiveRisk(G, target, labels):
    # Count number of implicated nodes are in the neighborhood of the point
    # of interest
    implicated_neighbors = 0

    for neighbor in G[target]:
        if neighbor in labels['F']: implicated_neighbors += 1

    return round(implicated_neighbors/len(G[target]), 3)

def calculateComplexCentrality(G, target, labels, risks, include_target = True):
    # Check to see if new target node should factor into centrality calculations
    # If we want to remove it, first extract the neighborhood, then remove the node
    # from the graph
    target_neighborhood = G[target]
    if not include_target:
        G.remove_node(target)

    # Calculate various centrality measurements
    degree_of_centrality   = nx.degree_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)
    closeness_centrality   = nx.closeness_centrality(G)
    eigenvector_centrality = nx.eigenvector_centrality(G)

    centrality_measurements = [degree_of_centrality, betweenness_centrality, closeness_centrality, eigenvector_centrality]

    # Find the mean centrality across nodes
    mean_centrality = {k:sum([method[k] for method in centrality_measurements])/len(centrality_measurements) for k in G.nodes}

    # Weight risk scores by centrality
    centralitry_weighted_risk = {k: mean_centrality[k]*risks[k] for k in risks.keys()}

    # Normalize weighted risk scores by the largest risk observed
    degree_of_suspicion = {k: centralitry_weighted_risk[k]/max(centralitry_weighted_risk.values()) for k in centralitry_weighted_risk.keys()}

    # Determine risk level of target node
    target_suspicion = 0
    for node in target_neighborhood:
        if node in labels['F']:
            target_suspicion += degree_of_suspicion[node]
    
    return target_suspicion/len(target_neighborhood)


# Main -------------------------------------------------------------------------
def main():
    # Construct initial graph
    G = constructNetwork()
    # plotNetwork(G, f_nodes = [2,5,6,7], nf_nodes = [1,3,4,8,9])

    # Introduce new, unknown node into the network
    G.add_node(10)
    G.add_edges_from([(10, 1), (10, 7), (10, 5)])

    # Define labels for known nodes
    f_nf_labels = {'F': [2, 5, 6, 7], 'NF': [1, 3, 4, 8, 9]}

    # Basic method - guilt by association without considering weights, severity, etc.
    print(calculateNaiveRisk(G, 10, f_nf_labels))

    # Complex method - consider centrality and risk score
    risk_scores = {1:0, 2:6, 3:0, 4:0, 5:7, 6:8, 7:10, 8:0, 9:0}
    print(calculateComplexCentrality(G, 10, f_nf_labels, risk_scores))
    

if __name__ == '__main__':
    main()