import Projectile as pr 
import matplotlib.pyplot as plt 

p1 = pr.Projectile()
p1.set_initial_conditions(10, 0, 0, 10, 1.2, 10, 2, 0.4, 0.01)
p1.range()
p1.x_y()

p2 = pr.Projectile()
p2.set_initial_conditions(10, 0, 0, 10, 1.2, 10, 2, 0.4, 0.01)
p2.R_K()
p2.x_y_rk()

plt.show()