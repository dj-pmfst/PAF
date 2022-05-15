import matplotlib.pyplot as plt 
import Projectile as pr 
import numpy as np

dt = np.arange(0.01, 0.4, 0.01)
p1 = pr.Projectile()

#ideja je bila da se petlja zaustavi kad y bude manji od 0 (nefizikalno) te isprinta zadnji dt za koji daje fizikalno rjesenje

for i in dt:
    p1.reset()
    p1.set_initial_conditions(10, 0, 0, 10, 1.2, 10, 2, 0.4, i)
    y = p1.range()
    for e in y:
        if e < 0:
            #print(i)
            break
        else:
            p1.x_y()
plt.show()