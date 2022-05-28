import ElectroMagnetism as em 
import matplotlib.pyplot as plt 
import numpy as np

p1 = em.ElectroMagnetism(np.array((0.1,0.1,0.1)), np.array((0,0,0)), 1, np.array((0,0,0)), np.array((0,0,1)), 1, 20)
p1.move_e()
x1, y1, z1 = p1.plot()

p2 = em.ElectroMagnetism(np.array((0.1,0.1,0.1)), np.array((0,0,0)), 1, np.array((0,0,0)), np.array((0,0,1)), 1, 20)
x2, y2, z2 = p2.move_rk()

figure = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(x1, y1, z1)
ax.plot3D(x2, y2, z2)
plt.show()