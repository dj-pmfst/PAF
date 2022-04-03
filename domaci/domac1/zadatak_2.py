import particle as prt
import numpy as np
import matplotlib.pyplot as plt 

p1 = prt.particle(0.01)
kut = np.linspace(0, 90, 90)
t = []
d = []
for i in kut:
    p1.set_initial_conditions(10, 0, 0, i)
    d.append(p1.range())
    t.append(p1.total_time())
#plt.plot(kut, t)
plt.plot(kut, d)
plt.show()