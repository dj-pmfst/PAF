import Projectile as pr 
import matplotlib.pyplot as plt 

p1 = pr.Projectile()
p1.set_initial_conditions(10, 0, 0, 10, 1.2, 5, 2, 0.4, 0.01)
p1.shape("kocka", 0, 3)
p1.move_cube()

p2 = pr.Projectile()
p2.set_initial_conditions(10, 0, 0, 10, 1.2, 5, 2, 0.4, 0.01)
p2.shape("kugla", 1.5, 0)
p2.R_K()

plt.plot(p2.x, p2.y)
plt.scatter(p1.x, p1.y, s=1)
plt.show()
