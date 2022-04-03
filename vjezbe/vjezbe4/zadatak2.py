import calculus
import numpy as np
import math
import matplotlib.pyplot as plt

def f1(x):
    return x*x

N_lista = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
koraci = []
trapezni = []
gornja = []
donja = []
for N in N_lista:
    koraci.append(N)
    gornja_s, donja_s = calculus.integral(f1, 0, 2, N)
    gornja.append(gornja_s)
    donja.append(donja_s)
    trapezni.append(calculus.integral_t(f1, 0, 2, N))
    
plt.plot(koraci, [8/3]*len(N_lista), color="black")
plt.ylim(2.663, 2.68)
plt.xlim(10, 900)
plt.scatter(koraci, gornja, color="red")
plt.scatter(koraci, donja, color="yellow")
plt.scatter(koraci, trapezni)
plt.show()