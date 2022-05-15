import Projectile as pr 
import matplotlib.pyplot as plt 
import numpy as np 

m = np.arange(0.3, 30, 0.5)
c = np.arange(0.1, 1.3, 0.1)
p1 = pr.Projectile()
r1 = []
r2 = []

for i in m:
    p1.set_initial_conditions(10, 0, 0, 10, 1.2, i, 2, 0.4, 0.01)
    r1.append(p1.range_rk())
    p1.reset()

for e in c:
    p1.set_initial_conditions(10, 0, 0, 10, 1.2, 10, 2, e, 0.01)
    r2.append(p1.range_rk())
    p1.reset()

plt.plot(m, r1)
plt.show()

plt.plot(c, r2)
plt.show()