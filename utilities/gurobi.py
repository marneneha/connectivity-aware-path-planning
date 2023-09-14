import gurobipy as gp
from gurobipy import GRB
import numpy as np

m = gp.Model("qcp")
# non-convex parameter to true
m.params.NonConvex = 2

# Create variables
# lb= np.array([[-5,-5],[-5,-5],[-5,-5],[-5,-5],[-5,-5],[-5,-5]]), 
u = m.addMVar(shape=(12, ), vtype=GRB.CONTINUOUS, name="u")
# u_given = m.addVar(name="u_given")
# x0 = m.addVar(name="x0")
x1 = m.addVar(name="x1")
obj = m.addVar(name="obj")
u_diff = m.addVar(name="u_diff")
# u_diff = u-np.array([1,0,1,0,1,0,1,0,1,0,1,0])
u_ref = np.array([1,0,1,0,1,0,1,0,1,0,1,0])
obj =0
for i in range(12):
    obj = obj+((u[i]-u_ref[i])*(u[i]-u_ref[i]))
# obj = ( for i in range(12) )
# GRBQuadExpr operator-(GRBQuadExpr u_ref,GRBQuadExpr u)
# obj = gp.norm(u-[1,0,1,0,1,0,1,0,1,0,1,0])
# m.addGenConstrNorm(obj, u_diff, 2.0, "normconstr")
# obj = np.linalg.norm(u-u_ref)**2
# print(obj)
m.setObjective(obj, GRB.MINIMIZE)
# # dynamics constraints
# m.addConstr(x1 ==[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]+u*0.1)
# # # safety constraints
for i,j in range(12):
    m.addGenConstrNorm(np.linalg.norm(x1[i]-x1[j])>1)
# # connectivity constraints
# # m.addConstr(np.linalg.norm(x-x)<Rc)
# # m.addConstr(np.linalg.norm(x-x)>Rdc)


m.optimize()
print(m.SolCount)
for v in m.getVars():
    print("i am here")
    print('%s %g' % (v.VarName, v.X))

print('Obj: %g' % obj.getValue())