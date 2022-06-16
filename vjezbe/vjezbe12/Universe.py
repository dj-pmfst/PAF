import numpy as np 
import math 
import matplotlib.pyplot as plt 
from matplotlib import animation

class Object():
    def __init__(self, m, p, v, boja):
        self.m = m 
        self.v = [v] 
        self.p = [p] 
        self.color = boja
        self.a = []

class SolarSystem():
    def __init__(self, vrijeme):
        self.Objects = []
        self.G = 6.67408 * 10**(-11)
        self.dt = 3600 * 24
        self.t = [0]
        self.t_uk = vrijeme
    
    def add_object(self, objekt):
        self.Objects.append(objekt)
    
    def __move(self):
        for o in self.Objects:
            self.F = np.array([0, 0])
            for e in self.Objects:
                if e != o :
                    self.F = self.F + (-self.G * o.m * e.m * (o.p[-1] - e.p[-1])/(np.linalg.norm(o.p[-1] - e.p[-1]))**3)
                
            o.a.append(self.F/o.m)
            o.v.append(o.v[-1] + o.a[-1] * self.dt)
            o.p.append(o.p[-1] + o.v[-1] * self.dt)
        self.t.append(self.t[-1] + self.dt)
           
    def plot(self):
        while self.t[-1] <= self.t_uk:
            self.__move()
        color = []
        fig, axs = plt.subplots()
        #axs.set_aspect("equal")

        for o in self.Objects:
            x2 = []
            y2 = []
            color.append(o.color)
            for p in o.p:
                x2.append(p[0])
                y2.append(p[1])
            axs.plot(x2, y2, color=o.color)
            axs.plot(x2[-1], y2[-1], "o", color=o.color)
  
        plt.show()
    
    def animate(self):
        while self.t[-1] <= self.t_uk:
            self.__move()

        fig, axs = plt.subplots()
        fig = plt.figure()
        # axs.set_aspect("equal")
        writer = animation.PillowWriter(fps=50)
        n = []
        for o in self.Objects:
            n.append(len(o.p))

        with writer.saving(fig, "ss.gif", 100):
            plt.axis('equal')
            axs.set_aspect("equal")
            axs.set_xlim(-2*1.496 * 10**11, 2*1.496 * 10**11)
            axs.set_ylim(-3*1.496 * 10**11, 3*1.496 * 10**11)
            for i in range(n[1]):
                if i%1 == 0:
                    plt.clf()
                    for o in self.Objects:
                        x = []
                        y = []
                        for p in o.p:
                            x.append(p[0])
                            y.append(p[1])
                        axs.set_aspect("equal")
                        axs.set_xlim(-2*1.496 * 10**11, 2*1.496 * 10**11)
                        axs.set_ylim(-3*1.496 * 10**11, 3*1.496 * 10**11)
                        plt.plot(x[:i], y[:i], color = o.color, linewidth = 1.)
                        plt.plot(x[i], y[i], color = o.color, marker = "o")
                    plt.axis('equal')
                    writer.grab_frame()