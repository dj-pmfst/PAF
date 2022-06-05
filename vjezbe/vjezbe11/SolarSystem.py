import numpy as np 
import math 
import matplotlib.pyplot as plt 

class Object():
    def __init__(self, m, v, p):
        self.m = m 
        self.v = [v] 
        self.p = [p] 
        self.a = []

class Orbit():
    def __init__(self, zemlja, sunce, t):
        self.G = 6.67408 * 10**(-11)
        self.dt = 360
        self.zemlja = zemlja 
        self.sunce = sunce
        self.t_uk = t 
        self.t = [0]
    
    def move(self):
        while self.t[-1] < self.t_uk:
            self.zemlja.a.append(-self.G * self.sunce.m * (self.zemlja.p[-1] - self.sunce.p[-1]) / (np.linalg.norm(self.zemlja.p[-1] - self.sunce.p[-1]))**3)
            self.sunce.a.append(-self.G * self.zemlja.m * (self.sunce.p[-1] - self.zemlja.p[-1]) / (np.linalg.norm(self.sunce.p[-1] - self.zemlja.p[-1]))**3)
            
            self.zemlja.v.append(self.zemlja.v[-1] + self.zemlja.a[-1] * self.dt)
            self.sunce.v.append(self.sunce.v[-1] + self.sunce.a[-1] * self.dt)
            
            self.zemlja.p.append(self.zemlja.p[-1] + self.zemlja.v[-1] * self.dt)
            self.sunce.p.append(self.sunce.p[-1] + self.sunce.v[-1] * self.dt)

            self.t.append(self.t[-1] + self.dt)
 
    def plot(self):
        self.move()
        x1 = []
        y1 = []
        x2 = []
        y2 = []

        for z, s in zip(self.zemlja.p, self.sunce.p):
            x1.append(z[0])
            x2.append(s[0])
            y1.append(z[1])
            y2.append(s[1])
     
        fig, axs = plt.subplots()
        axs.set_aspect("equal", "box")
        axs.plot(x1, y1, color="blue")
        axs.plot(x2, y2, color="yellow")
        plt.show()