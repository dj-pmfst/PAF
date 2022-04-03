import math
import numpy as np
import matplotlib.pyplot as plt

class particle:
    def __init__(self, dt):
        self.t = []
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.dt = dt
    
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
        self.__init__(self.dt)
    
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

    #domaci rad:

    def total_time(self):
        self.t.sort(reverse = True)
        print(self.t[0])
        return self.t[0]
    
    def max_speed(self):
        self.vy.sort(reverse = True)
        vy_max = self.vy[0]
        self.vx.sort(reverse = True)
        vx_max = self.vx[0]
        v_max = math.sqrt(vy_max**2 + vx_max **2)
        print(v_max, "je maksimalna brzina")

    def velocity_to_hit_target(self, x, y, r, kut2):
        v = 0
        self.kut = kut2
        hit = False
        while hit == False:
            self.v0 = v
            self.range()
            for x1, y1 in zip(self.x, self.y):
                if (x1-x)**2 + (y1-y)**2 <= r**2 :
                    hit = True
                else:
                    v += 1
        print(v, "je potrebna brzina da se pogodi meta.")
        
    def angle_to_hit_target(self, x, y, r, v0_2):
        kut = 0
        self.v0 = v0_2
        hit = False
        while hit == False:
            self.kut = kut
            self.range()
            for x1, y1 in zip(self.x, self.y):
                if (x1-x)**2 + (y1-y)**2 <= r**2 :
                    hit = True
                else:
                    kut += 1
        print(kut, "je potreban kut da se pogodi meta.")