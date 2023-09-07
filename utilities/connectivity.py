import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
elist = [('a', 'b', 0.3), ('b', 'c', 0.9), ('c', 'd', 1.2), ('a', 'd', 0.7)]
G.add_weighted_edges_from(elist)
# finds overall connectivity of the graph
graph_connectivity = nx.node_connectivity(G)
print(graph_connectivity)

higher_K = 3
# code to increase the connectivity
while(graph_connectivity!=higher_K):
    add.edge()

lower_K = 1
# code to decrease the connectivity
while(graph_connectivity!=lower_K):
    remove.edge()



# print(G.edges[1, 2]['color'])
# G = nx.cubical_graph()
# subax1 = plt.subplot(121)
# nx.draw(G, with_labels=True)   # default spring_layout
# subax2 = plt.subplot(122)
# nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')