import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1 = prt.particle(0.01)
p1.set_initial_conditions(10, 0, 0, 60)
t = np.linspace(0.01, 0.1, 200)  #0.01 je vrijednost od dt
err_lista = []

for i in t:
    p1 = prt.particle(i)
    p1.set_initial_conditions(10, 0, 0, 60)
    p1.range()
    p1.analytical()
    err_lista.append(p1.error())
    p1.reset()

plt.plot(t, err_lista)
plt.show()


