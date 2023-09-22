import gurobipy as gp
from gurobipy import GRB
import numpy as np
import matplotlib.pyplot as plt

m = gp.Model("qcp")
# non-convex parameter to true
m.params.NonConvex = 2
# ,ub= np.array([5,5,5,5,5,5,5,5,5,5,5,5])
# Create variables
ux = m.addMVar(lb= np.array([-20,-20,-20,-20,-20,-20]), shape=(6, ), vtype=GRB.CONTINUOUS, name="ux")
uy = m.addMVar(lb= np.array([-20,-20,-20,-20,-20,-20]), shape=(6, ), vtype=GRB.CONTINUOUS, name="uy")
x1 = m.addMVar(shape=(6, ), vtype=GRB.CONTINUOUS, name="x1")
y1 = m.addMVar(shape=(6, ), vtype=GRB.CONTINUOUS, name="y1")
obj = m.addVar(name="obj")
ux_ref = np.array([1,1,1,1,1,1])
uy_ref = np.array([0,0,0,0,0,0])
x0 = np.array([4,2,-2,-4,-2,2])
y0 = np.array([0,1.73,1.73,0,-1.73,-1.73])
disconnected_set = np.array([0,1])
connected_set = np.array([2,3,4,5])
obj=0
Rs=0
Rc=4
Rdc=6
# set objective
for i in range(6):
    obj = obj+((ux[i]-ux_ref[i])*(ux[i]-ux_ref[i])) + ((uy[i]-uy_ref[i])*(uy[i]-uy_ref[i]))
m.setObjective(obj, GRB.MINIMIZE)

# dynamics constraints
for i in range(6):
    m.addConstr(x1[i] == x0[i]+ux[i]*0.1)
    m.addConstr(y1[i] == y0[i]+uy[i]*0.1)

# safety constraints
for i in range(6):
    for j in range(6):
        if(i != j): 
            m.addConstr(((x1[i]-x1[j])*(x1[i]-x1[j]))+((y1[i]-y1[j])*(y1[i]-y1[j]))>=Rs)

# connectivity constraints
for i in connected_set:
    for j in connected_set:
        if(i != j): 
            m.addConstr(((x1[i]-x1[j])*(x1[i]-x1[j]))+((y1[i]-y1[j])*(y1[i]-y1[j]))<=Rc)

# disconnectivity constraints
for i in disconnected_set:
    for j in disconnected_set:
        if(i != j): 
            m.addConstr(((x1[i]-x1[j])*(x1[i]-x1[j]))+((y1[i]-y1[j])*(y1[i]-y1[j]))>=Rdc)

m.optimize()
print(m.SolCount)
for v in m.getVars():
    # print("i am here")
    print('%s %g' % (v.VarName, v.X))

print('Obj: %g' % obj.getValue())
print(ux_ref)
print(uy_ref)
f, ax = plt.subplots(1)
circle1 = plt.Circle((x0[0], y0[0]),0.05,color='r')
circle2 = plt.Circle((x0[1], y0[1]),0.05,color='r')
circle3 = plt.Circle((x0[2], y0[2]),0.05,color='r')
circle4 = plt.Circle((x0[3], y0[3]),0.05,color='r')
circle5 = plt.Circle((x0[4], y0[4]),0.05,color='r')
circle6 = plt.Circle((x0[5], y0[5]),0.05,color='r')
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)
ax.add_patch(circle4)
ax.add_patch(circle5)
ax.add_patch(circle6)
# ax.plot(x0[0], x0[1], color='r', label='robot1')
# ax.plot(x0[2], x0[3], color='g', label='robot2')
# ax.plot(x0[4], x0[5], color='b', label='robot3')
# ax.plot(x0[6], x0[7], color='black', label='robot4')
# ax.plot(x0[8], x0[9], color='brown', label='robot5')
# ax.plot(x0[10], x0[11], color='magenta', label='robot6')
ax.set_ylim(ymin=-5, ymax=8)
ax.set_xlim(xmin=-5, xmax=8)
plt.show()