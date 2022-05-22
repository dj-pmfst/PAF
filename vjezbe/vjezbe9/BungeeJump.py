import math
import numpy as np
import matplotlib.pyplot as plt

class BungeeJump():
    def __init__(self):
        self.t = []
        self.h = []
        self.v = []
        self.x = []
        self.Eu = []
        self.Ep = []
        self.Ek = []
        self.El = []
    
    def set_initial_conditions(self, h, gustoca, konstanta_zrak, m, konstanta_el, povrsina, l, t, dt):
        self.h.append(h) 
        self.dens = gustoca
        self.c = konstanta_zrak
        self.k = konstanta_el
        self.m = m 
        self.x.append(0)
        self.dt = dt 
        self.t.append(0)
        self.v.append(0)
        self.area = povrsina
        self.t2 = t
        self.h2 = h
        self.l = l

    def __acc(self, v, y):
        return (-9.81 - ((np.sign(v)) * self.dens * self.c * self.area * v**2/(2 * self.m)) - (self.k * y)/self.m)
    
    def __move(self):
        v1 = self.__acc(self.v[-1], self.h[-1]) * self.dt
        y1 = self.v[-1] * self.dt

        v2 = self.__acc((self.v[-1] + v1 / 2), (self.x[-1] + y1 / 2)) * self.dt
        y2 = (self.v[-1] + y1 / 2) * self.dt

        v3 = self.__acc((self.v[-1] + v2 / 2), (self.x[-1] + y2 / 2)) * self.dt
        y3 = (self.v[-1] + y2 / 2) * self.dt

        v4 = self.__acc((self.v[-1] + v3), (self.x[-1] + y3)) * self.dt
        y4 = (self.v[-1] + y3) * self.dt

        self.v.append(self.v[-1] + (1 / 6) * (v1 + 2 * v2 + 2 * v3 + v4))
        self.h.append(self.h[-1] + (1 / 6) * (y1 + 2 * y2 + 2 * y3 + y4))
        
        self.t.append(self.t[-1] + self.dt)

        # self.a.append(self.__acc(self.v[-1], self.h[-1]))
        # self.v.append(self.v[-1] + self.a[-1] * self.dt)
        # self.h.append(self.h[-1] + self.v[-1] * self.dt)

        self.Ek.append((self.m * self.v[-1]**2) * 0.5)
        self.Ep.append(self.m * self.h[-1] * 9.81)
        self.El.append((self.k * self.x[-1]**2) * 0.5)
        self.Eu.append(self.Ep[-1] + self.Ek[-1] + self.El[-1])
        
    def jump(self):
        self.t_nova = []

        while self.t[-1] < self.t2:
            self.t_nova.append(self.t[-1])
            if self.h[-1] < self.h2 - self.l:
                self.x.append(self.x[-1])
            else:
                #self.__move()
                self.x.append(0)
            
            self.__move()

    def plot(self):
        plt.plot(self.t, self.h)
        plt.show()

        plt.plot(self.t_nova, self.Ek)
        plt.plot(self.t_nova, self.Ep)
        plt.plot(self.t_nova, self.El)
        plt.plot(self.t_nova, self.Eu)
        plt.show()