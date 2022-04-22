import math
import matplotlib.pyplot as plt 
import numpy as np 

class ProjectileDrop:
    def __init__(self, dt = 0.01):
        self.t = []
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.dt = dt
    
    def set_initial_conditions(self, v0x, y0):
        self.v0x = v0x
        self.t.append(0)
        self.x.append(0)
        self.y.append(y0)
        self.vx.append(self.v0x)
        self.vy.append(0)
        self.ax.append(0)
        self.ay.append(-9.81)

        print("Uspješno stvoren objekt. Početna visina:", y0, ". Početna brzina:", v0x)
    
    def change_y(self, y_n):
        self.y = []
        self.y.append(y_n)
        return self.y 
    
    def change_v(self, v_n):
        self.vx = []
        self.vx.append(self.v0x + v_n)
        return self.vx

    #treci zadatak:
    
    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.x.append(self.x[-1] + self.vx[-1]*self.dt)
        self.y.append(self.y[-1] + self.vy[-1]*self.dt)
        self.vx.append(self.vx[-1] + self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1] + self.ay[-1]*self.dt)
        self.ax.append(0)
        self.ay.append(-9.81)

    def drop(self):
        while (self.y[-1] >= 0):
            self.__move()
        return self.t, self.x, self.y, self.vy, self.ay

    #peti zadatak:

    def target(self, x_m, r, v_w):
        y_m = 0  # y koordinata mete
        x_r = np.linspace(x_m, r) # sirina mete na x koordinati
        
        while self.y[-1] >= 0 :
            self.t.append(self.t[-1] + self.dt)
            self.vx.append(self.vx[-1] + v_w + self.ax[-1]*self.dt)
            self.vy.append(self.vy[-1] + self.ay[-1]*self.dt)
            self.ax.append(0)
            self.ay.append(-9.81)
            self.x.append(self.x[-1] + self.vx[-1]*self.dt)
            self.y.append(self.y[-1] + self.vy[-1]*self.dt)

        for x,y in zip(self.x, self.y):
            for i in x_r:
                if (x == i) & (y == 0):
                    print("Meta je pogođena.")