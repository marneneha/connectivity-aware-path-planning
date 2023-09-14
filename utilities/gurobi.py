import gurobipy as gp
from gurobipy import GRB
import numpy as np

m = gp.Model("qcp")
# non-convex parameter to true
m.params.NonConvex = 2

# Create variables
u = m.addMVar(lb= np.array([-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5]), shape=(12, ), vtype=GRB.CONTINUOUS, name="u")
x1 = m.addMVar(shape=(12, ), vtype=GRB.CONTINUOUS, name="x1")
obj = m.addVar(name="obj")
u_ref = np.array([1,0,1,0,1,0,1,0,1,0,1,0])
x0 = np.array([1,0,1,0,1,0,1,0,1,0,1,0])

obj =0
Rs=0
Rc=0.5
# set objective
for i in range(12):
    obj = obj+((u[i]-u_ref[i])*(u[i]-u_ref[i]))
m.setObjective(obj, GRB.MINIMIZE)

# # dynamics constraints
for i in range(12):
    m.addConstr(x1[i] == x0[i]+u[i]*0.1)

# safety constraints
for i in range(12):
    for j in range(12):
        if(i != j): 
            m.addConstr((x1[i]-x1[j])>=Rs)

# connectivity constraints
for i in range(12):
    for j in range(12):
        if(i != j): 
            m.addConstr((x1[i]-x1[j])<=Rc)

# disconnectivity constraints
# m.addConstr(np.linalg.norm(x-x)>Rdc)


m.optimize()
print(m.SolCount)
for v in m.getVars():
    print("i am here")
    print('%s %g' % (v.VarName, v.X))

print('Obj: %g' % obj.getValue())