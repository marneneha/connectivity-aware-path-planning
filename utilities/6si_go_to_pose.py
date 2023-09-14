#!/usr/bin/python3
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from math import dist

# Initial_pose_of_robots = 
np_Initial_pose_of_robots = np.array([[4,0,2,1.73,-2,1.73,-4,0,-2,-1.73,2,-1.73]])
# print(np_Initial_pose_of_robots)
# velocity_dict = 
np_velocity_dict = np.array([[1,0,1,0,1,0,1,0,1,0,1,0]])
# print(np_velocity_dict)
global previous_pose_of_robots
previous_pose_of_robots = np_Initial_pose_of_robots
global trajectory
trajectory= np_Initial_pose_of_robots
# print(trajectory)
trajectory = np.append(trajectory,np_Initial_pose_of_robots, axis=0)
trajectory = np.append(trajectory,np_Initial_pose_of_robots, axis=0)
# trajectory.append(np_Initial_pose_of_robots)
# trajectory.append(np_Initial_pose_of_robots)
# print(trajectory)
def si_model():
    previous_pose_of_robots = np_Initial_pose_of_robots
    trajectory= np_Initial_pose_of_robots
    # print("i am inside")
    for i in range(30):
        current_pose_of_robots = previous_pose_of_robots+np_velocity_dict*0.1
        previous_pose_of_robots = current_pose_of_robots
        trajectory = np.append(trajectory,current_pose_of_robots, axis=0)
    # print(trajectory)
    update_graph(current_pose_of_robots)
    
    f, ax = plt.subplots(1)
    ax.plot(trajectory[:,0], trajectory[:,1], color='r', label='robot1')
    ax.plot(trajectory[:,2], trajectory[:,3], color='g', label='robot2')
    ax.plot(trajectory[:,4], trajectory[:,5], color='b', label='robot3')
    ax.plot(trajectory[:,6], trajectory[:,7], color='black', label='robot4')
    ax.plot(trajectory[:,8], trajectory[:,9], color='brown', label='robot5')
    ax.plot(trajectory[:,10], trajectory[:,11], color='magenta', label='robot6')
    ax.set_ylim(ymin=-4)
    # plt.show()

def update_graph(current_pose_of_robots):
    # reinitialize the graph 
    Rc=6
    G = nx.Graph()
    arr = np.reshape(current_pose_of_robots, (6,2))
    current_node_poses = list(map(tuple, arr))
    arr = np.array([[1,0],[1,0],[1,0],[1,0],[1,0],[1,0]])
    print(arr.shape)
    G.add_nodes_from(current_node_poses)
    for i in current_node_poses:
        for j in current_node_poses:
            if(dist(i,j)<=Rc and i!=j):
                G.add_weighted_edges_from([(i,j,dist(i,j))])

        # print("i am here")
        # print(i)
    # G.add_edge()
    # G.add_edge((i,j)for (i,j) in (current_pose_i, current_pose_j): if(dist(current_pose_i,current_pose_j)<1))
    # nx.draw(G, pos=nx.circular_layout(G), with_labels = True)
    # nx.draw_networkx_labels(G, pos=nx.circular_layout(G))
    # labels = nx.get_edge_attributes(G, 'weight')
    # nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels=labels)
    # plt.savefig('6SI_robots.png')
    # print(G)
    # print(list(map(tuple, arr)))
    decrease_the_connectivity(G,1)

def decrease_the_connectivity(G, lower_K):
    graph_connectivity = nx.node_connectivity(G)
    print(graph_connectivity)
    print(lower_K)
    while(graph_connectivity!=lower_K):
        print("m here1")
        max_wieght = min(dict(G.edges).items(), key=lambda x: x[1]['weight'])
        print("m here2")
        print(max_wieght)
        G.remove_edge(max_wieght[0][0], max_wieght[0][1])
        print("m here3")
        graph_connectivity = nx.node_connectivity(G)
        print("m here4")
        print(graph_connectivity)
        nx.draw(G, pos=nx.circular_layout(G))
    # nx.draw_networkx_labels(G, pos=nx.circular_layout(G))
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels=labels)
    plt.savefig('roads.png')
# update_graph(previous_pose_of_robots)
si_model()
