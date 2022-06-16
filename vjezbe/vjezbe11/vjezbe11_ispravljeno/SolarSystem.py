import numpy as np 
import math 
import matplotlib.pyplot as plt 

class Object():
    def __init__(self, m, v, p, boja):
        self.m = m 
        self.v = [v] 
        self.p = [p] 
        self.a = []
        self.color = boja

class Orbit():
    def __init__(self, t):
        self.G = 6.67408 * 10**(-11)
        self.dt = 360
        self.Objects = []
        self.t_uk = t 
        self.t = [0]
    
    def add_object(self, objekt):
        self.Objects.append(objekt)
    
    def __move(self):
        while self.t[-1] < self.t_uk:
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
        self.__move()
        color = []
        fig, axs = plt.subplots()
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