import numpy as np 
import matplotlib.pyplot as plt 
ax = plt.subplot()
F = float(input("sila:"))
m = float(input("masa:"))
a = F/m
t = np.linspace(0, 10, 500)
v_lista = [0]
x_lista = [0]
a_lista = [F/m]
t_lista = [0]
dt = 0.1
for i in range (100):
    t_lista.append(i*dt)
    v_lista.append(v_lista[i]+a_lista[i]*dt)
    x_lista.append(x_lista[i]+v_lista[i]*dt)
    a_lista.append(F/m)      

def xt_graf():
    ax.set_xlabel("t(s)")
    ax.set_ylabel("x(m)")
    plt.plot(t_lista, x_lista)
    plt.show()
def vt_graf():
    ax.set_xlabel("t(s)")
    ax.set_ylabel("v(m/s)")
    plt.plot(t_lista, v_lista)
    plt.show()
def at_graf():
    ax.set_xlabel("t(s)")
    ax.set_ylabel("a(m/s^2)")
    plt.plot(t_lista, a_lista)
    plt.show()
xt_graf()