import math

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
        self.t.append(0)
        self.x.append(0)
        self.y.append(y0)
        self.vx.append(v0x)
        self.vy.append(0)
        self.ax.append(0)
        self.ay.append(-9.81)

        print("Uspješno stvoren objekt. Početna visina:", y0, ". Početna brzina:", v0x)