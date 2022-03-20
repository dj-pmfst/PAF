import math
import numpy as np
import matplotlib.pyplot as plt
ax = plt.subplot()

def pocetno(v0, kut, t):
    g = -9.81
    x0 = 0
    y0 = 0
    vy_lista = []
    vx_lista = []
    x_lista = [0]
    y_lista = [0]
    t_lista = [0]
    v0x = v0 * np.cos(kut * np.pi/180)
    v0y = v0 * np.sin(kut * np.pi/180)
    vy_lista.append(v0y)
    vx_lista.append(v0x)
    dt = 0.1
    
    for i in range (int(t/dt)):
        vy = vy_lista[i] + g*dt
        y = vy_lista[i] * dt + 0.2*g*(dt)**2
        x_lista.append(vx_lista[i] * dt)
        y_lista.append(y)
        vx_lista.append(v0x)
        vy_lista.append(vy)
        t_lista.append(i*dt)
    
    for e in y_lista:
        if e <= 0:
            y_lista = y_lista[:int(e):]
            x_lista = x_lista[:int(e):]
    
    return y_lista, x_lista, vx_lista, vy_lista

def x_y(x_lista, y_lista):
    plt.plot(x_lista, y_lista)
    plt.show()

def max_h(y_lista):
    y_lista.sort(reverse = True)
    print(y_lista[0], "je maksimalna visina.")

def max_x(x_lista):
    x_lista.sort(reverse = True)
    print(x_lista[0], "je maksimalni domet.")

def max_v(vx_lista, vy_lista):
    vy_lista.sort(reverse = True)
    vy_max = vy_lista[0]
    v_max = math.sqrt(vy_max**2 + v0x **2)
    print(v_max, "je maksimalna brzina")

def meta(x, y, r, x_lista, y_lista):
    
    def udaljenost(x, y, x_lista, y_lista):
        global d 
        d =[]
        for x1, y1 in zip(x_lista, y_lista):
            d.append(math.sqrt((x1-x)**2 + (y1-y)**2) - r)
        d.sort(reverse = True)
        print("Najbliža udaljenost od mete", d[0])
    
    for x1, y1 in zip(x_lista, y_lista):
        
        if (x1-x)**2 + (y1-y)**2 <= r**2 :
            print("Objekt je pogodio metu.")
        
        elif (x1-x)**2 + (y1-y)**2 > r**2 :
            print("Objekt nije pogodio metu.")
            udaljenost()
            
    a = plt.Circle((x2, y2), r, color = 'b', fill = False)
    ax.add_patch(a)
    plt.plot(x_lista, y_lista)
    plt.show()