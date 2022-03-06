import math
import matplotlib.pyplot as plt
import numpy as np
ax = plt.subplot()
def unos():
    global x1
    global x2
    global y1
    global y2
    global r
    x1 = float(input("X koordinata točke:"))
    y1 = float(input("Y koordinata točke:"))
    r = float(input("Radijus kružnice:"))
    x2 = float(input("X koordinata središta kružnice:"))
    y2 = float(input("Y koordinata središta kružnice:"))
    return x1, x2, y1, y2, r
def funkcija(parametri):
    if x1 > x2:
        veci = x1
        manji = x2
    else:
        manji = x1
        veci = x2
    if y1 > y2:
        veci2 = y1
        manji2 = y2
    else:
        manji2 = y1
        veci2 = y2
    a = plt.Circle((x2, y2), r, color = 'b', fill = False)
    ax.add_patch(a)
    ax.set_xlim(manji *(-2), veci*2)
    ax.set_ylim(manji2 *(-2), veci2*2)
    plt.plot(x1, y1, 'ro')
    naslov = (input("Ime grafa:"))
    uvjet = input("Želite li spremiti?")
    if uvjet == 'da':
        plt.savefig(naslov)
    else:
        plt.show()
    if (x1-x2)**2 + (y1-y2)**2 < r**2 :
        print("Točka se nalazi unutar kružnice.")
        udaljenost()
    elif (x1-x2)**2 + (y1-y2)**2 > r**2 :
        print("Točka se nalazi izvan kružnice.")
        udaljenost()
    else:
        print("Točka se nalazi na kružnici.")
def udaljenost():
    global d 
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print("Točka se nalazi na udaljenosti od kružnice", d)
parametri = unos()
funkcija(parametri)