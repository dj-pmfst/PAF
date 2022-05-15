import math
import matplotlib.pyplot as plt 
import numpy as np 

class Projectile():
    def __init__(self):
        self.t = []
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
    
    def set_initial_conditions(self, v0, x0, y0, kut, gustoca, m, povrsina, koeficijent, dt):
        self.v0 = v0
        self.kut = kut
        self.ax.append(0)
        self.ay.append(0)
        self.t.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.vx.append(v0 * np.cos(kut * np.pi/180))
        self.vy.append(v0 * np.sin(kut * np.pi/180))
        self.dens = gustoca
        self.m = m 
        self.area = povrsina 
        self.c = koeficijent
        self.dt = dt
    
    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.x.append(self.x[-1] + self.vx[-1]*self.dt)
        self.y.append(self.y[-1] + self.vy[-1]*self.dt)
        self.vx.append(self.vx[-1] + self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1] + self.ay[-1]*self.dt)
        self.ax.append(- np.sign(self.vx[-1])*(self.dens * self.c * self.area) / (2*self.m) * self.vx[-1]**2)
        self.ay.append(-9.81 - np.sign(self.vy[-1])*(self.dens * self.c * self.area) / (2*self.m) * self.vy[-1]**2)
    
    def range(self):
        while (self.y[-1] >= 0):
            self.__move()
        return self.y
        
    def x_y(self):
        a = plt.plot(self.x, self.y)
        return a

    def reset(self):
        self.__init__()
    
    def ay_r(self, v, x=0, t=0):
        return (-9.81 - np.sign(v)*(self.dens * self.c * self.area)/(2 * self.m)*(v)**2)
    
    def ax_r(self, v, x=0, t=0):
        return (- np.sign(v)*(self.dens * self.c * self.area)/(2 * self.m)*(v)**2)
    
    def R_K(self):
        while (self.y[-1] >= 0):
            x1 = self.vx[-1] * self.dt
            y1 = self.vy[-1] * self.dt 
            #vx1 = (- np.sign(self.vx[-1])*(self.dens * self.c * self.area)/(2 * self.m)*(self.vx[-1])**2) * self.dt
            #vy1 = (-9.81 - np.sign(self.vy[-1])*(self.dens * self.c * self.area)/(2 * self.m)*(self.vy[-1])**2) * self.dt
            vx1 = self.ax_r(self.vx[-1]) * self.dt
            vy1 = self.ay_r(self.vy[-1]) * self.dt

            x2 = (self.vx[-1] + vx1/2) * self.dt  
            y2 = (self.vy[-1] + vy1/2) * self.dt 
            #vx2 = (- np.sign(self.vx[-1] + vx1/2)*(self.dens * self.c * self.area)/(2 * self.m)*(self.vx[-1] + vx1/2)**2) * self.dt
            #vy2 = (-9.81 - np.sign(self.vy[-1] + vy1/2)*(self.dens * self.c * self.area)/(2 * self.m)*(self.vy[-1] + vy1/2)**2) * self.dt
            vx2 = self.ax_r(self.vx[-1] + vx1/2) * self.dt
            vy2 = self.ay_r(self.vy[-1] + vy1/2) * self.dt

            x3 = (self.vx[-1] + vx2/2) * self.dt
            y3 = (self.vy[-1] + vy2/2) * self.dt
            #vx3 = (- np.sign(self.vx[-1] + vx2/2)*(self.dens * self.c * self.area)/(2 * self.m)*(self.vx[-1] + vx2/2)**2) * self.dt
            #vy3 = (-9.81 - np.sign(self.vy[-1] + vy2/2)*(self.dens * self.c * self.area)/(2 * self.m)*(self.vy[-1] + vy2/2)**2) * self.dt
            vx3 = self.ax_r(self.vx[-1] + vx2/2) * self.dt
            vy3 = self.ay_r(self.vy[-1] + vy2/2) * self.dt

            x4 = (self.vx[-1] + vx3) * self.dt
            y4 = (self.vy[-1] + vy3) * self.dt
            #vx4 = (- np.sign(self.vx[-1] + vx3/2)*(self.dens * self.c * self.area)/(2 * self.m)*(self.vx[-1] + vx3/2)**2) * self.dt
            #vy4 = (-9.81 - np.sign(self.vy[-1] + vy3/2)*(self.dens * self.c * self.area)/(2 * self.m)*(self.vy[-1] + vy3/2)**2) * self.dt
            vx4 = self.ax_r(self.vx[-1] + vx3/2) * self.dt
            vy4 = self.ay_r(self.vy[-1] + vy3/2) * self.dt

            self.vy.append(self.vy[-1] + (vy1 + 2*vy2 + 2*vy3 + vy4)/6)
            self.vx.append(self.vx[-1] + (vx1 + 2*vx2 + 2*vx3 + vx4)/6)
            self.y.append(self.y[-1] + (y1 + 2*y2 + 2*y3 + y4)/6)
            self.x.append(self.x[-1] + (x1 + 2*x2 + 2*x3 + x4)/6)
            #print(vy1, " ", vy2, " ", vy3, " ", vy4)   

    def x_y_rk(self):
        b = plt.plot(self.x, self.y)
        return b
    
    def range_rk(self):
        self.R_K()
        return self.x[-1]