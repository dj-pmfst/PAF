import projectile as pr 
import numpy as np 
import matplotlib.pyplot as plt 

a = pr.ProjectileDrop()
a.set_initial_conditions(200, 2000)
t, x, y, vy, ay = a.drop()
dt = np.linspace(0.001, 0.1, 100)
t2 = []   #lista koja ima jednak broj elemenata kao i dt 

for i in range(100):
    t2.append(t[i])

plt.scatter(dt, t2, s=10)
plt.xlim(0.001, 0.1)
plt.show()