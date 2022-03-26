import math
import numpy as np
import matplotlib.pyplot as plt

class particle:
    def __init__(self):
        self.t = []
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.dt = 0.01
    
    def set_initial_conditions(self, v0, x0, y0, kut):
        self.v0 = v0
        self.kut = kut
        self.t.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.vx.append(v0 * np.cos(kut * np.pi/180))
        self.vy.append(v0 * np.sin(kut * np.pi/180))
        self.ax.append(0)
        self.ay.append(-9.81)
    
    def reset(self):
        self.__init__()
    
    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.x.append(self.x[-1] + self.vx[-1]*self.dt)
        self.y.append(self.y[-1] + self.vy[-1]*self.dt)
        self.vx.append(self.vx[-1] + self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1] + self.ay[-1]*self.dt)
        self.ax.append(0)
        self.ay.append(-9.81)

    def range(self):
        while (self.y[-1] >= 0):
            self.__move()
        return(self.x[-1])
        print(x[-1])

    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.show()

    def analytical(self):
        global d
        d = ((self.v0**2)*np.sin(2*self.kut*np.pi/180))/9.81
        return d

    def error(self):
        err = (abs(d - self.x[-1])/d)*100
        return err