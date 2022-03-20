import math
import numpy as np
import matplotlib.pyplot as plt
ax = plt.subplot()

def jednoliko_gibanje(F, v, t, m):
    a = F/m
    v_lista = [0]
    x_lista = [0]
    a_lista = [F/m]
    t_lista = [0]
    dt = 0.1
    for i in range (t):
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

def kosi_hitac(v0, t, kut):
    g = -9.81
    x0 = 0
    y0 = 0
    t = np.linspace(0, 10, 500)
    vy_lista = []
    vx_lista = []
    x_lista = [0]
    y_lista = [0]
    t_lista = [0]
    v0x = v0 * np.cos(kut * np.pi/180)
    v0y = v0 * np.sin(kut * np.pi/180)
    vy_lista.append(v0y)
    vx_lista.append(v0x)
    dt = 0.1
    for i in range (200):
        vy = vy_lista[i] + g*i*dt
        y = np.sin(kut * np.pi/180) * vy_lista[i] * i*dt
        x_lista.append(np.cos(kut *np.pi/180) * vx_lista[i] * i*dt)
        y_lista.append(y)
        vx_lista.append(v0x)
        vy_lista.append(vy)
        t_lista.append(i*dt)

    def xt_graf():
        ax.set_xlabel("t(s)")
        ax.set_ylabel("x(m)")
        plt.plot(t_lista, x_lista)
        plt.show()
    def vt_graf():
        ax.set_xlabel("t(s)")
        ax.set_ylabel("v(m/s)")
        plt.plot(t_lista, vy_lista)
        plt.show()
    def yt_graf():
        ax.set_xlabel("t(s)")
        ax.set_ylabel("y(m)")
        plt.plot(t_lista, y_lista)
        plt.show()
    vt_graf()