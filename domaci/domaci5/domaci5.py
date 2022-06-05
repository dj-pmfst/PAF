import ElectroMagnetism as em 
import matplotlib.pyplot as plt 
import numpy as np 

# def B_t(t):
#     return np.array((0,0,t/10))

p1 = em.ElectroMagnetism(np.array((0.1,0.1,0.1)), np.array((0,0,0)), -1, np.array((0,0,0)), 0, 1, 20)
p2 = em.ElectroMagnetism(np.array((0.1,0.1,0.1)), np.array((0,0,0)), -1, np.array((0,0,0)), np.array((0,0,1)), 1, 20)
p3 = em.ElectroMagnetism(np.array((0.1,0.1,0.1)), np.array((0,0,0)), 1, np.array((0,0,0)), 0, 1, 20)

x1, y1, z1 = p1.move_rk()
x2, y2, z2 = p2.move_rk()
x3, y3, z3 = p3.move_rk()

figure = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(x1, y1, z1, color = "blue")
ax.plot3D(x2, y2, z2, color = "green")
plt.show()

figure = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(x1, y1, z1, color = "blue")
ax.plot3D(x3, y3, z3, color = "green")
plt.title("putanja elektrona i pozitrona u vremenski promjenjivom magnetnom polju")
plt.show()