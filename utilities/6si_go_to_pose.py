#!/usr/bin/python3
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Initial_pose_of_robots = 
np_Initial_pose_of_robots = np.array([[4,0,2,1.73,-2,1.73,-4,0,-2,-1.73,2,-1.73]])
print(np_Initial_pose_of_robots)
# velocity_dict = 
np_velocity_dict = np.array([[1,0,1,0,1,0,1,0,1,0,1,0]])
print(np_velocity_dict)
global previous_pose_of_robots
previous_pose_of_robots = np_Initial_pose_of_robots
global trajectory
trajectory= np_Initial_pose_of_robots
# print(trajectory)
trajectory = np.append(trajectory,np_Initial_pose_of_robots, axis=0)
trajectory = np.append(trajectory,np_Initial_pose_of_robots, axis=0)
# trajectory.append(np_Initial_pose_of_robots)
# trajectory.append(np_Initial_pose_of_robots)
print(trajectory)
def si_model():
    previous_pose_of_robots = np_Initial_pose_of_robots
    trajectory= np_Initial_pose_of_robots
    print("i am inside")
    for i in range(30):
        current_pose_of_robots = previous_pose_of_robots+np_velocity_dict*0.1
        previous_pose_of_robots = current_pose_of_robots
        trajectory = np.append(trajectory,current_pose_of_robots, axis=0)
    print(trajectory)
    f, ax = plt.subplots(1)
    ax.plot(trajectory[:,0], trajectory[:,1], color='r', label='robot1')
    ax.plot(trajectory[:,2], trajectory[:,3], color='g', label='robot2')
    ax.plot(trajectory[:,4], trajectory[:,5], color='b', label='robot3')
    ax.plot(trajectory[:,6], trajectory[:,7], color='black', label='robot4')
    ax.plot(trajectory[:,8], trajectory[:,9], color='brown', label='robot5')
    ax.plot(trajectory[:,10], trajectory[:,11], color='magenta', label='robot6')
    ax.set_ylim(ymin=-4)
    plt.show()

si_model()
G = nx.Graph()
arr = np.reshape(np_Initial_pose_of_robots, (6,2))
G.add_nodes_from(list(map(tuple, arr)))
nx.draw(G, pos=nx.circular_layout(G), with_labels = True)
plt.savefig('6SI_robots.png')
print(G)
print(list(map(tuple, arr)))