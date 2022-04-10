import math
import numpy as np
import matplotlib.pyplot as plt

class har_osc:
    def __init__(self):
        self.x = []
        self.a = []
        self.v = []
        self.t = []

    def set_initial_conditions(self, m, k, v0, x0, t, dt):
        self.dt = dt
        self.m = m
        self.k = k
        self.v.append(v0)
        self.a.append(-(self.k/self.m)*x0)
        self.x.append(x0)
        self.n = int(t/self.dt)
        self.t = np.linspace(0, t, self.n+1)

    def oscillate(self):
        
        for i in range(self.n):
            self.a.append(-(self.k/self.m) * self.x[-1])
            self.v.append(self.v[-1] + self.a[-1]*self.dt)
            self.x.append(self.x[-1] + self.v[-1]*self.dt)
        
        return self.t, self.x
    
    def reset(self):
        self.__init__(self)
    
    def plot(self):
        plt.plot(self.t, self.x)
        plt.show()

        plt.plot(self.t, self.v)
        plt.show()

        plt.plot(self.t, self.a)
        plt.show()

    def analytical(self):
        self.an = []
        
        for i in self.t:
            self.an.append(self.x[0] * math.sin(math.sqrt(self.k / self.m)*i + math.pi/2))
        
        return self.t, self.an

    def period(self, t):
        self.p = []
        n_ = len(self.x)
        br = 0
        
        for i in range(1, n_):
            self.p.append(self.dt*i)
            br += 1
            if self.x[i] >= self.x[0]:
                break
        t_nova = np.linspace(1, t, br)
        
        return t_nova, self.p
    
    def period_analytical(self, t):
        self.pa = []
        n_ = len(self.x)
        br = 0
        
        for i in range(1, n_):
            self.pa.append(2 * np.pi * math.sqrt(self.m / self.k))
            br += 1
        t_nova = np.linspace(1, t, br)
        
        return t_nova, self.pa