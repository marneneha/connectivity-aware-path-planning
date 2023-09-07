import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
elist = [((1,1), (1,2), 1.3), 
         ((1,2), (2,1), 0.9), 
         ((2,1), (2,2), 1.2), 
         ((1,1), (2,2), 0.7)]
G.add_weighted_edges_from(elist)
max_wieght = max(dict(G.edges).items(), key=lambda x: x[1]['weight'])
print("max_wieght")
print(max_wieght[0][0])
# finds overall connectivity of the graph
graph_connectivity = nx.node_connectivity(G)
# print(graph_connectivity)
min_wieght_edge = nx.stoer_wagner(G)
print(min_wieght_edge)

lower_K = 2
# code to decrease the connectivity
while(graph_connectivity!=lower_K):
    print("m here1")
    max_wieght = max(dict(G.edges).items(), key=lambda x: x[1]['weight'])
    print("m here2")
    G.remove_edge(max_wieght[0][0], max_wieght[0][1])
    print("m here3")
    graph_connectivity = nx.node_connectivity(G)
    print("m here4")

print(graph_connectivity)

    


higher_K = 3
# code to increase the connectivity
# while(graph_connectivity!=higher_K):
#     add.edge()




# print(G.edges[1, 2]['color'])
# G = nx.cubical_graph()
# subax1 = plt.subplot(121)
# nx.draw(G, with_labels=True)   # default spring_layout
# subax2 = plt.subplot(122)
# nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color=(1,2))