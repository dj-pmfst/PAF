import math
import numpy as np 
import matplotlib.pyplot as plt

class ElectroMagnetism():
    def __init__(self, v0, polozaj, q, E, B, m, t):
        self.m = m
        self.p = [polozaj]
        self.v = [v0]
        self.a =[q*(E + np.cross(v0, B))/m]
        self.q = q
        self.E = E
        self.B = B
        self.dt = 0.01
        self.t = np.linspace(0, t, int(t/self.dt))

    def move_e(self):
        for i in self.t:
            self.v.append(self.v[-1] + self.a[-1] * self.dt)
            self.p.append(self.p[-1] + self.v[-1] * self.dt)
            self.a.append(self.q*(self.E + np.cross(self.v[-1], self.B))/self.m)
    
    def plot(self):
        x = []
        y = []
        z = []
        for i in range(len(self.p)):
            x.append(self.p[i][0])
            y.append(self.p[i][1])
            z.append(self.p[i][2])
        return x, y, z
    
    def __acc(self, v):
        return self.q/self.m * (self.E + np.cross(v, self.B))
    
    def move_rk(self):
        x = [0]
        y = [0]
        z = [0]
        for i in self.t:
            v1 = self.__acc(self.v[-1]) * self.dt
            p1 = self.v[-1] * self.dt

            v2 = self.__acc(self.v[-1] + v1 / 2) * self.dt
            p2 = (self.v[-1] + p1 / 2) * self.dt

            v3 = self.__acc(self.v[-1] + v2 / 2) * self.dt
            p3 = (self.v[-1] + p2 / 2) * self.dt

            v4 = self.__acc(self.v[-1] + v3) * self.dt
            p4 = (self.v[-1] + p3) * self.dt

            self.v.append(self.v[-1] + (1 / 6) * (v1 + 2 * v2 + 2 * v3 + v4))

            x.append(x[-1] + (p1[0] + 2*p2[0] + 2*p3[0] + p4[0])/6)
            y.append(y[-1] + (p1[1] + 2*p2[1] + 2*p3[1] + p4[1])/6)
            z.append(z[-1] + (p1[2] + 2*p2[2] + 2*p3[2] + p4[2])/6) 
        
        return x, y, z 