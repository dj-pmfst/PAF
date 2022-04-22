import projectile as pr 
import matplotlib.pyplot as plt

a = pr.ProjectileDrop()
a.set_initial_conditions(200, 2000)

t, x, y, vy, ay = a.drop()

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("x-y graf")
plt.show()

plt.plot(t, x)
plt.xlabel('t(s)')
plt.ylabel('y')
plt.title("x-t graf")
plt.show()

plt.plot(t, y)
plt.xlabel('t(s)')
plt.ylabel('y')
plt.title("y-t graf")
plt.show()

plt.plot(t, vy)
plt.xlabel('t(s)')
plt.ylabel('v(m/s)')
plt.title("v-t graf")
plt.show()

plt.plot(t, ay)
plt.xlabel('t(s)')
plt.ylabel('a(m/s^2)')
plt.title("a-t graf")
plt.show()