import matplotlib.pyplot as plt
import numpy as np
def funkcija():
    x1 = float(input("X koordinata prve točke: "))
    y1 = float(input("Y koordinata prve točke: "))
    x2 = float(input("X koordinata druge točke: "))
    y2 = float(input("Y koordinata druge točke: "))
    a = y2 - y1
    b = x1 - x2
    c = a*(x1) + b*(y1)
    print("Jednadžba pravca je y= -(",a/b,")*x +", c/b)
    if x1 > x2:
        veci = x1
        manji = x2
    else:
        manji = x1
        veci = x2
    x = np.linspace(manji -1, veci +1, 100)
    y = -1*(a/b)*x + c/b
    plt.plot(y)
    naslov = (input("Ime grafa:"))
    uvjet = input("Želite li spremiti kao PDF?")
    if uvjet == 'da':
        filename = ('{}.pdf' .format(naslov))
        plt.savefig(filename)
    else:
        plt.show()
funkcija() 