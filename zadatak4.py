def funkcija(parametri):
    a = y2 - y1
    b = x1 - x2
    c = a*(x1) + b*(y1)
    print("Jednadžba pravca je y= -(",a/b,")*x +", c/b)
def unos():
    global x1
    global x2
    global y1
    global y2
    x1 = float(input("X koordinata prve točke: "))
    y1 = float(input("Y koordinata prve točke: "))
    x2 = float(input("X koordinata druge točke: "))
    y2 = float(input("Y koordinata druge točke: "))
    return x1, y1, x2, y2
parametri = unos()
funkcija(parametri) 