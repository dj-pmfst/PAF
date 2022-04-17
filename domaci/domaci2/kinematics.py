import matplotlib.pyplot as plt 
import math
import numpy as np 

class kinematics:
    def __init__(self):
        self.a = []
        self.v = []
        self.x = []
        self.t = []
        self.dt = 0.1
    
    def set_initial_conditions(self, F, v0, x0, m, t):
        self.m = m 
        self.F = F
        self.a.append(self.F(v0, x0, self.dt)/self.m)
        self.v.append(v0)
        self.x.append(x0)
        self.t.append(0)
        n = int(t/self.dt)
        self.t_ = np.linspace(0, t, n)

    def __move(self):
        self.a.append(self.F(self.v[-1], self.x[-1], self.t[-1])/self.m)
        self.v.append(self.v[-1] + self.a[-1]*self.dt)
        self.x.append(self.x[-1] + self.v[-1]*self.dt)
        self.t.append(self.t[-1] + self.dt)
    
    def move(self):
        for i in self.t_ :
            self.__move()
        return self.a, self.v, self.x, self.t

    def graph(self):
        plt.plot(self.t, self.x)
        plt.show()
        
        plt.plot(self.t, self.v)
        plt.show()
        
        plt.plot(self.t, self.a)
        plt.show()